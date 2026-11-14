"""Run against a pinned upstream checkout: python test_companion.py CHECKOUT."""
import base64
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, utils
from verify_signature import load_validator, verify

ROOT = Path(sys.argv.pop(1))
REFERENCE = ROOT / "spec/testimony_validate.py"
TV = load_validator(REFERENCE)
BASE = [json.loads(line) for line in (ROOT / "conformance/cases/basis-under-the-digest.jsonl").read_text().splitlines()]


def text(entries):
    return "\n".join(json.dumps(e) for e in entries)


def fixture(algorithm="Ed25519"):
    entries = copy.deepcopy(BASE)
    key = ed25519.Ed25519PrivateKey.generate() if algorithm == "Ed25519" else ec.generate_private_key(ec.SECP256R1())
    message = entries[-1]["digest"].encode()
    if algorithm == "Ed25519":
        signature = key.sign(message)
    else:
        r, s = utils.decode_dss_signature(key.sign(message, ec.ECDSA(hashes.SHA256())))
        signature = r.to_bytes(32, "big") + s.to_bytes(32, "big")
    entries[-1].update(scheme="signature", signature={"signer": "fixture-key", "algorithm": algorithm,
                      "value": base64.b64encode(signature).decode()})
    keys = {"fixture-key": key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode()}
    return entries, keys


class CompanionTests(unittest.TestCase):
    def test_valid_algorithms_preserve_reference_and_scope(self):
        for algorithm in ("Ed25519", "ES256"):
            entries, keys = fixture(algorithm)
            result = verify(text(entries), keys, TV)
            self.assertTrue(result["ok"])
            self.assertFalse(result["identity_established"])
            self.assertFalse(result["effect_established"])
            self.assertEqual(result["reference"], TV.validate(text(entries)).as_dict())
            self.assertEqual(result["signatures"][0]["covers"], entries[-1]["covers"])

    def test_signature_over_other_digest(self):
        for algorithm in ("Ed25519", "ES256"):
            entries, keys = fixture(algorithm)
            entries[-2]["basis"] = "asserted"
            entries[-1]["digest"] = "sha256:" + TV.digest_of(entries[:-1])
            # Rehashing makes reference TR-4 pass; the old signature must fail.
            self.assertEqual(TV.validate(text(entries)).level, "TR-4")
            self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_basis_tamper(self):
        entries, keys = fixture()
        entries[-2]["basis"] = "asserted"
        self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_wrong_key(self):
        entries, _ = fixture()
        _, keys = fixture()
        self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_missing_key(self):
        entries, _ = fixture()
        self.assertFalse(verify(text(entries), {}, TV)["ok"])

    def test_bad_signature_encoding(self):
        entries, keys = fixture()
        entries[-1]["signature"]["value"] = "not-base64!"
        self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_algorithm_confusion(self):
        entries, keys = fixture()
        entries[-1]["signature"]["algorithm"] = "ES256"
        self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_unsigned_is_not_a_pass(self):
        self.assertFalse(verify(text(BASE), {}, TV)["ok"])

    def test_missing_coverage(self):
        entries, keys = fixture()
        entries[-1]["covers"] = []
        self.assertFalse(verify(text(entries), keys, TV)["ok"])

    def test_cli(self):
        entries, keys = fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "record.jsonl").write_text(text(entries))
            (root / "keys.json").write_text(json.dumps(keys))
            args = [sys.executable, str(Path(__file__).with_name("verify_signature.py")), str(root / "record.jsonl"),
                    "--keys", str(root / "keys.json"), "--validator", str(REFERENCE), "--profile", "digest-text-v1"]
            proc = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            self.assertTrue(json.loads(proc.stdout)["ok"])
            entries[-2]["basis"] = "asserted"
            entries[-1]["digest"] = "sha256:" + TV.digest_of(entries[:-1])
            (root / "record.jsonl").write_text(text(entries))
            proc = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 1)
            self.assertFalse(json.loads(proc.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()

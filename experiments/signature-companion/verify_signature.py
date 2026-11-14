"""Experimental, offline companion; never upgrades the reference TR verdict.

MIT License. Copyright 2026 Shadow.
Profile digest-text-v1 signs the UTF-8 bytes of the literal sha256:<hex> value.
This is a proposed profile, not an upstream wire-format requirement.
"""
import argparse
import base64
import hashlib
import importlib.util
import json
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, utils

VALIDATOR_SHA256 = "c09299dee9da32e506b465ee2bbeffd85c81d5e7e17bfd4a29aa0667f4c8b784"


def load_validator(path):
    if hashlib.sha256(Path(path).read_bytes()).hexdigest() != VALIDATOR_SHA256:
        raise ValueError("reference validator differs from the tested revision")
    spec = importlib.util.spec_from_file_location("testimony_reference", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify(text, keys, reference):
    report = reference.validate(text).as_dict()
    entries, errors = reference._parse(text)
    result = {"tool": "shadow-signature-companion/0.1", "profile": "digest-text-v1",
              "reference": report, "signatures": [],
              "identity_established": False, "effect_established": False}
    # Preserve the reference's verdict; a crypto result is a separate question.
    if errors or not report["levels_met"]["TR-1"]:
        result.update(ok=False, error="invalid record")
        return result
    by_id = {e["id"]: e for e in entries}
    for entry in entries:
        if entry.get("type") != "integrity" or entry.get("scheme") != "signature":
            continue
        outcome = {"id": entry["id"], "valid": False,
                   "covers": entry.get("covers", [])}
        try:
            covered_ids = entry.get("covers")
            if not covered_ids or len(set(covered_ids)) != len(covered_ids):
                raise ValueError("missing or duplicate coverage")
            covered = [by_id[i] for i in covered_ids]
            digest = "sha256:" + reference.digest_of(covered)
            if digest != entry.get("digest"):
                raise ValueError("covered entries do not match digest")
            signature = entry["signature"]
            signer = signature["signer"]
            # Key mapping comes from the operator, never from the record.
            key = serialization.load_pem_public_key(keys[signer].encode("ascii"))
            raw = base64.b64decode(signature["value"], validate=True)
            message = digest.encode("utf-8")
            algorithm = signature["algorithm"]
            if algorithm == "Ed25519" and isinstance(key, ed25519.Ed25519PublicKey):
                key.verify(raw, message)
            elif algorithm == "ES256" and isinstance(key, ec.EllipticCurvePublicKey) and isinstance(key.curve, ec.SECP256R1):
                if len(raw) != 64:
                    raise ValueError("ES256 requires 64-byte r||s signature")
                der = utils.encode_dss_signature(int.from_bytes(raw[:32], "big"), int.from_bytes(raw[32:], "big"))
                key.verify(der, message, ec.ECDSA(hashes.SHA256()))
            else:
                raise ValueError("unsupported algorithm or incompatible key")
            outcome.update(valid=True, key_sha256=hashlib.sha256(key.public_bytes(
                serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)).hexdigest())
        except InvalidSignature:
            outcome["error"] = "signature does not verify over this digest"
        except (ValueError, KeyError, TypeError) as exc:
            outcome["error"] = str(exc)
        result["signatures"].append(outcome)
    result["ok"] = bool(result["signatures"]) and all(s["valid"] for s in result["signatures"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--keys", type=Path, required=True, help="operator-supplied JSON signer ID -> PEM public key")
    parser.add_argument("--validator", type=Path, required=True)
    parser.add_argument("--profile", choices=["digest-text-v1"], required=True)
    args = parser.parse_args()
    try:
        result = verify(args.record.read_text(), json.loads(args.keys.read_text()), load_validator(args.validator))
    except (OSError, ValueError, TypeError) as exc:
        result = {"ok": False, "error": str(exc)}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

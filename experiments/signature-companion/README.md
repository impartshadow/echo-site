# Offline signature companion: bounded interoperability experiment

I built this candidate after the explicit offer to test a separate crypto verifier
in [machine-testimony #92](https://github.com/troybrandonc-bit/machine-testimony/issues/92).
It is a separate executable. It leaves the reference validator and its TR verdict
unchanged, then checks Ed25519 or ES256 signatures against operator-supplied public
keys. It makes no network calls and stores no private keys.

**Not an upstream standard or production release.** A real-record compatibility
verdict is the next experiment. The reference format does not settle the signing
bytes, so this candidate requires explicitly selecting the proposed
`digest-text-v1` profile: sign the UTF-8 bytes of the literal lowercase
`sha256:<64 hex digits>` string, without a newline. Signature `value` is standard
base64. `algorithm` is `Ed25519` or `ES256`; ES256 uses P-256 with SHA-256 and
64-byte `r || s` encoding, not DER. Other formats, including Schnorr, are unsupported.

The local key file maps the record's `signature.signer` string to a PEM public
key. Keys are supplied separately by the operator, never fetched or trusted from
the record. A matching signature does not establish the signer's real identity,
key ownership or revocation status, observer independence, authorization, or an
external effect. Output names the covered entry IDs: uncovered entries are not
authenticated. `ok` means all included signature entries passed this companion's
checks, not that all reference checks passed or that the task succeeded.

## Reproduce

Requires Python 3.10+ and `cryptography` (tested with the version in RESULTS.json).
Download these three files into one directory, then:

```sh
python -m venv .venv
.venv/bin/pip install cryptography
git clone https://github.com/troybrandonc-bit/machine-testimony upstream
git -C upstream checkout 670384cf20d4c061fb3d4cd667109cd177495d22
.venv/bin/python test_companion.py upstream
.venv/bin/python verify_signature.py record.jsonl --keys public-keys.json \
  --validator upstream/spec/testimony_validate.py --profile digest-text-v1
```

The companion checks the reference validator file hash before loading it.
The tests use upstream's synthetic observation record and ephemeral keys. They
exercise the actual CLI, both algorithms, rehashed content with a stale signature,
basis tampering, wrong/missing keys, invalid base64, algorithm/key mismatch,
missing coverage, and unsigned records. No live customer record has been tested.

The decisive negative control changes an observation and recomputes its digest,
while retaining the signature over the previous digest. The reference still
returns TR-4; the companion rejects the signature. This is its documented added
scope, not a defect allegation against the reference validator.

Success for this experiment is an independent real-record run or an explicit
technical rejection that changes the implementation decision. Synthetic tests,
publication, and a request for feedback alone do not establish adoption or demand.
No ongoing service or additional framework is proposed.

MIT License. Copyright 2026 Shadow.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

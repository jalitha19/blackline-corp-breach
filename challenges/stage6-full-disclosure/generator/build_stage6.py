from pathlib import Path
import hashlib
import pyzipper


# ============================================================
# Blackline Corp Breach
# Stage 6 - Full Disclosure
# Final archive generator
# ============================================================


BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_DIR = BASE_DIR / "source"
PLAYER_DIR = BASE_DIR / "player"

PLAYER_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Previous-stage fragments
# ------------------------------------------------------------

STAGE1_FRAGMENT = "RAVEN"
STAGE3_FRAGMENT = "NIGHTFALL"
STAGE5_FRAGMENT = "ECHO"


# ------------------------------------------------------------
# Files
# ------------------------------------------------------------

FINAL_EVIDENCE_FILE = SOURCE_DIR / "final_evidence.txt"

OUTPUT_ARCHIVE = PLAYER_DIR / "blackline_final_evidence.zip"


# ------------------------------------------------------------
# Validate source file
# ------------------------------------------------------------

if not FINAL_EVIDENCE_FILE.exists():
    raise FileNotFoundError(
        f"Missing source file: {FINAL_EVIDENCE_FILE}"
    )


# ------------------------------------------------------------
# Build the combination
#
# Stage order:
# Stage 1 | Stage 3 | Stage 5
# ------------------------------------------------------------

combination = (
    f"{STAGE1_FRAGMENT}|"
    f"{STAGE3_FRAGMENT}|"
    f"{STAGE5_FRAGMENT}"
)


# ------------------------------------------------------------
# Derive password
#
# SHA-256 -> lowercase hexadecimal -> first 16 characters
# ------------------------------------------------------------

full_hash = hashlib.sha256(
    combination.encode("utf-8")
).hexdigest()

archive_password = full_hash[:16]


# ------------------------------------------------------------
# Remove an existing archive
# ------------------------------------------------------------

if OUTPUT_ARCHIVE.exists():
    OUTPUT_ARCHIVE.unlink()


# ------------------------------------------------------------
# Create AES encrypted ZIP
# ------------------------------------------------------------

with pyzipper.AESZipFile(
    OUTPUT_ARCHIVE,
    "w",
    compression=pyzipper.ZIP_DEFLATED,
    encryption=pyzipper.WZ_AES,
) as archive:

    archive.setpassword(
        archive_password.encode("utf-8")
    )

    archive.setencryption(
        pyzipper.WZ_AES,
        nbits=256
    )

    archive.write(
        FINAL_EVIDENCE_FILE,
        arcname="final_evidence.txt"
    )


# ------------------------------------------------------------
# Finished
# ------------------------------------------------------------

print()
print("=" * 64)
print("Blackline Corp Breach - Stage 6")
print("Full Disclosure")
print("=" * 64)
print()

print("Stage 6 archive generated successfully.")
print()

print(f"Stage 1 fragment : {STAGE1_FRAGMENT}")
print(f"Stage 3 fragment : {STAGE3_FRAGMENT}")
print(f"Stage 5 fragment : {STAGE5_FRAGMENT}")

print()
print(f"Combination      : {combination}")
print(f"SHA-256          : {full_hash}")
print(f"Archive password : {archive_password}")

print()
print(f"Output archive   : {OUTPUT_ARCHIVE}")

print()
print(
    "IMPORTANT: Combination, password and fragments are "
    "administrator/solution information."
)

print("=" * 64)
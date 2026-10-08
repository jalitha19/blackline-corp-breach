BLACKLINE CORP BREACH
Stage 6 - Full Disclosure

The investigation is almost complete.

Three important case fragments were recovered during earlier stages:

- Stage 1
- Stage 3
- Stage 5

To unlock the final case archive, combine those three fragments in
stage order using the following format:

STAGE1|STAGE3|STAGE5

Example:

ALPHA|BRAVO|CHARLIE

Do not include spaces.

Next:

1. Calculate the SHA-256 hash of the combined string.
2. Convert the hash to lowercase hexadecimal format.
3. Take the FIRST 16 hexadecimal characters.
4. Use those 16 characters as the password for the supplied ZIP archive.
5. Extract the archive.
6. Read the final evidence file.
7. Submit the final BLK{...} flag to CTFd.

Suggested tools:

- PowerShell
- Python
- sha256sum
- 7-Zip
- CyberChef

The fragments themselves are NOT provided in this challenge.
They must be obtained by solving the earlier stages.
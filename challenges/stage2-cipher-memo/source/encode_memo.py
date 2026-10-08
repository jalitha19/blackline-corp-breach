SHIFT = 7

with open("memo_plaintext.txt", "r", encoding="utf-8") as f:
    plaintext = f.read()

def caesar_encrypt(text, shift):
    result = []

    for char in text:
        if char.isupper():
            result.append(
                chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            )

        elif char.islower():
            result.append(
                chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            )

        else:
            result.append(char)

    return "".join(result)

ciphertext = caesar_encrypt(plaintext, SHIFT)

with open("intercepted_memo.txt", "w", encoding="utf-8") as f:
    f.write(ciphertext)

print("[+] Caesar cipher applied")
print(f"[+] Shift: {SHIFT}")
print("[+] Output: intercepted_memo.txt")
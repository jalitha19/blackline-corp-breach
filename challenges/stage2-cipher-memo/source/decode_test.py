SHIFT = 7

with open("intercepted_memo.txt", "r", encoding="utf-8") as f:
    ciphertext = f.read()

def caesar_decrypt(text, shift):
    result = []

    for char in text:
        if char.isupper():
            result.append(
                chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            )

        elif char.islower():
            result.append(
                chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            )

        else:
            result.append(char)

    return "".join(result)

plaintext = caesar_decrypt(ciphertext, SHIFT)

print(plaintext)
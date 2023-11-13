def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = input("Masukkan teks yang ingin didekripsi: ")
shift = int(input("Masukkan nilai pergeseran: "))

decrypted_text = caesar_decrypt(ciphertext, shift)
print("Hasil dekripsi: " + decrypted_text)
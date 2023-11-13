import base64

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def encrypt_message(message, shift):
    encrypted_message = caesar_cipher(message, shift)
    encoded_message = base64.b64encode(encrypted_message.encode()).decode()
    return encoded_message

def send_whatsapp_message(phone_number, encrypted_message):
    # Kode untuk mengirim pesan WhatsApp dapat ditambahkan di sini
    print(f"Message sent to {phone_number}: {encrypted_message}")

if __name__ == "__main__":
    phone_number = "+6285664910794"  # Ganti dengan nomor telepon penerima
    key = 3  # Ganti dengan kunci enkripsi sesuai kebutuhan

    message = input("Masukkan pesan yang akan dikirim: ")

    encrypted_message = encrypt_message(message, key)
    send_whatsapp_message(phone_number, encrypted_message)
if __name__ == "__main__":
    phone_number = "+6285664910794"  # Ganti dengan nomor telepon penerima
    key = 3  # Ganti dengan kunci enkripsi sesuai kebutuhan

    message = input("Masukkan pesan yang akan dikirim: ")

    encrypted_message = encrypt_message(message, key)
    send_whatsapp_message(phone_number, encrypted_message)
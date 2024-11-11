def caesar_decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            decrypted_text += decrypted_char
        elif char.isdigit():
            decrypted_char = str((int(char) - 3) % 10)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

while True:
    ciphertext = input("请输入要解密的密文：")
    plaintext = caesar_decrypt(ciphertext)
    print(f"明文为：{plaintext}")

    again = input("是否再玩一次？（y/n）：")
    if again.lower()!= 'y':
        break
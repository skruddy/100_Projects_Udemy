from Caesar_Logo import logo

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(text, shift):
    encrypted_text = ""
    for character in text:
        if character == ' ' or character == '_' or character == '-':
            encrypted_text += character
            continue
        character_index = alphabets.index(character)+shift
        if character_index > 25:
            character_index -= 26
        encrypted_text += alphabets[character_index]
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for character in text:
        if character == ' ' or character == '_' or character == '-':
            decrypted_text += character
            continue
        character_index = alphabets.index(character)-shift
        if character_index < 0:
            character_index += 26
        decrypted_text += alphabets[character_index]
    return decrypted_text


print(logo)
text = input("Please enter the text!")
encrypted_text_output = encrypt(text, 5)
decrypted_text_output = decrypt(encrypted_text_output, 5)


print(f"Text to encrypt: {text} \nText after encryption: {encrypted_text} \nText after decryption: {decrypted_text}")
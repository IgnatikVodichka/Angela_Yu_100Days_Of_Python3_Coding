

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction, text, shift):
    new_word = ""
    for letter in text:
        if direction == "encode":
            new_position = alphabet.index(letter) + shift
            if new_position > 25:
                new_position -= 26
        elif direction == "decode":
            new_position = alphabet.index(letter) - shift
        new_letter = alphabet[new_position]
        new_word += new_letter
    print(new_word)


caesar(direction, text, shift)


'''
Other methods 
'''
# def encrypt(plain_text, shift_amount):
#     encrypted_word = ""
#     for letter in plain_text:
#         new_position = alphabet.index(letter) + shift_amount
#         if new_position > 25:
#             new_position -= 26
#         new_letter = alphabet[new_position]
#         encrypted_word += new_letter
#     print(f"Ypour encrypted word is {encrypted_word}")


# def decrypt(encrypted_text, shift_amount):
#     decrypted_word = ""
#     for letter in encrypted_text:
#         new_position = alphabet.index(letter) - shift_amount
#         new_letter = alphabet[new_position]
#         decrypted_word += new_letter
#     print(f"your decripted word is {decrypted_word}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)


'''
One more way to make it with list and append function
'''
# def encrypt(plain_text, shift_amount):
#     encrypted_word = []
#     for letter in plain_text:
#         letter = alphabet.index(letter)
#         if letter + shift_amount > 25:
#             letter -= 26
#         encrypted_word.append(alphabet[letter+shift_amount])
#     encrypted_word = "".join(encrypted_word)
#     print(f"The encoded text is {encrypted_word}")


# encrypt(text, shift)


'''
Different approach with just 2 sets of leters in the alphabet.
'''
# new_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# new_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# new_text = input("Type your message:\n").lower()
# new_shift = int(input("Type the shift number:\n"))


# def new_encrypt(plain_text, shift_amount):
#     encrypted_word = ""
#     for letter in plain_text:
#         new_position = new_alphabet.index(letter) + shift_amount
#         new_letter = new_alphabet[new_position]
#         encrypted_word += new_letter
#     print(encrypted_word)


# new_encrypt(new_text, new_shift)

# %%

# Caesar Cipher - 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):

    chiper_text = ""

    for letter in plain_text:
        if alphabet.index(letter) + shift_amount < len(alphabet):
            chiper_text += alphabet[alphabet.index(letter) + shift_amount]
        else:
            chiper_text += alphabet[len(alphabet) - (alphabet.index(letter) + shift_amount)]
    
    print(f"The encoded text in {chiper_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)

# %%

# Caesar Cipher - 2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        plain_text += alphabet[alphabet.index(letter) - shift_amount]
        """ if alphabet.index(letter) - shift_amount > 0:
            plain_text += alphabet[alphabet.index(letter) - shift_amount]
        else:
            plain_text += alphabet[len(alphabet) - (alphabet.index(letter) + shift_amount)] """
    print(f"The decoded text is {plain_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

# %%

# Caesar Cipher - 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(start_text, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "encode":
        for letter in start_text:
            if alphabet.index(letter) + shift_amount < len(alphabet):
                new_text += alphabet[alphabet.index(letter) + shift_amount]
            else:
                new_text += alphabet[len(alphabet) - (alphabet.index(letter) + shift_amount)]
        print(f"The encoded text is {new_text}")
    elif cipher_direction == "decode":
        for letter in start_text:
            new_text += alphabet[alphabet.index(letter) - shift_amount]
        print(f"The decode text is {new_text}")


def caesar2(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")


caesar2(start_text=text, shift_amount=shift, cipher_direction=direction)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# %%

# Caesar Cipher - 4

import art

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü'
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü'
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a new function that calls itself if they type 'yes'.

restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if answer == "no":
        restart = False
    

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Hint: Think about how you can use the modulus (%).

if shift > len(alphabet):
    shift %= len(alphabet)

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# %%

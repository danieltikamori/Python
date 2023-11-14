"""Caesar Cipher"""	
from art import logo
# Used print(), input(), len(), functions, for loop, if/else

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> None:
    """
    Encrypts or decrypts a text using the Caesar cipher algorithm.

    Parameters:
      - start_text (str): The text to be encrypted or decrypted.
      - shift_amount (int): The amount of characters to shift in the alphabet.
      - cipher_direction (str): The direction of the cipher, either "encode" or "decode".

    Returns:
      None
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
        
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if result == "no":
        should_continue = False
        print("Thanks for using the Caesar Cipher program! Goodbye!")

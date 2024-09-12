alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift):
    new_text = ""
    for i in range(len(original_text)):
        for j in range(len(alphabet)):
            if original_text[i] == alphabet[j]:
                if (j + shift + 1) > len(alphabet):
                     new_text += alphabet[(len(alphabet) - (j+1)) - shift]
                else:
                    new_text += alphabet[j + shift]
            if original_text[i] == " ":
                new_text += original_text[i]
    return new_text

print("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
type = input().strip().lower()
repetition = 1
if type == "encode" or type == "decode":
    while repetition == 1:
        print("Type your message: \n")
        message = input().lower()
        print("Type the shift number: \n")
        shift = int(input())
        
        
        result = encrypt(message)
        print(f"Here's the encoded result: {result}")
        print ("Type 'yes' if you want to go again. Otherwise type 'no'.")
else:
    print("Your input was unacceptable!")
 
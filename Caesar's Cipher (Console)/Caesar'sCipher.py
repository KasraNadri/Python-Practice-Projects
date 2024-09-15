alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift):
    new_text = ""
    for i in range(len(original_text)):
        for j in range(len(alphabet)):
            if original_text[i] == alphabet[j]:
                if (j + shift + 1) > len(alphabet):
                     new_text += alphabet[abs(len(alphabet) - (j + shift))]
                else:
                    new_text += alphabet[j + shift]
            if original_text[i] == " ":
                new_text += original_text[i]
    return new_text

repetition = 1
while repetition == 1:
    print("Type 'encode' to encrypt: ")
    type = input().strip().lower()
    if type == "encode":
        print("Type your message: ")
        message = input().lower()
        print("Type the shift number: ")
        shift = int(input())
        
        result = encrypt(message, shift)
        print(f"Here's the encoded result: {result}")
        print ("Type 'yes' if you want to go again. Otherwise type 'no'.")
        yesorno = input().strip().lower()
        if (yesorno  == "no"):
            repetition = 0
            print("Goodbye!")
    else:
        print("Your input was unacceptable!")
 
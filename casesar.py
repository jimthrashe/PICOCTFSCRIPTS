def caesar_decrypt(message, shift):
    decrypted_text = ""




#check the message for capitol or lowercase letters and remove them 
    for char in message:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
# here is the formula for the decryption of a caesar cypher 
            decrypted_char = chr(((ord(char) - base - shift) % 26) + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text



#the following forumula runs caesar_decrypt over and over again with shifts in the range of 1-26
def brute_force_caesar_decrypt(message):
    decrypted_results = []

    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(message, shift)
        decrypted_results.append(decrypted_text)

    return decrypted_results
#enter the message 
message =input("Input: " )
decrypted_texts = brute_force_caesar_decrypt(message)

# Display all decryption attempts
for shift, text in enumerate(decrypted_texts, 1):
    print(f"Shift {shift}: {text}")

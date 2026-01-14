
with open("raw_text.txt", 'r') as file:
    orginal_text = file.read()
    print(orginal_text)
shift1 = int(input('enter a number '))
shift2 = int(input('enter 2nd number'))

# According to the question
#with this method encryption will work but decryption will not work
#because during the encryption method letter in a to m will go in 
#letter in n and z so we can't apply the same encryption metho for decryption



#i have put the alphat with in range during encryption.
# for e.g if letter in range from a-m during encyption 
# it should not enter in n-z because it will brake down 
#during the decryption so if letter in a-m should stay in a-m during
#encryption same contion appy for both capital and lower letter 

def encrypt(original_text, shift1, shift2):
    result = ''
    for char in original_text:
        if char.isalpha():
            # lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    # forward shift within a-m (wrap size 13)
                    # we use mod(%) 13 so letter in range a-m stay with in range a to m 
                    new_char = chr((ord(char) - ord('a') + (shift1 * shift2)) % 13 + ord('a'))
                else: 
                     # n - z
                     #we use mod(%) 13 so letter in range n-z stay with in range n-z
                    # backward shift within n-z (wrap size 13)
                    new_char = chr((ord(char) - ord('n') - (shift1 + shift2)) % 13 + ord('n'))
                result += new_char

            #for the uppercase letters
            else:
                if 'A' <= char <= 'M':
                    # backward shift within A-M (wrap size 13)
                    new_char = chr((ord(char) - ord('A') - shift1) % 13 + ord('A'))
                else:  # N-Z
                    # forward shift within N-Z (wrap size 13)
                    new_char = chr((ord(char) - ord('N') + (shift2 * shift2)) % 13 + ord('N'))
                result += new_char

        # non-alphabet characters remain unchanged
        else:
            result += char
    return result

# to print the excrypted sentence
encrypted_text = encrypt(orginal_text,shift1,shift2)
print(encrypted_text)
# to write the encrypted sentence in the file
with open('encrypted_text.txt', 'w') as file:
    file.write(encrypted_text)

# steps to debug the encrypted file

#1st step we read the encrypted file 
with open('encrypted_text.txt', 'r') as file:
    encrypted_text = file.read()
    print( 'encrypted text',encrypted_text)

def decrypt(encrypted_text, shift1, shift2):
    result = ''
    for char in encrypted_text:
        if char.isalpha():
            # lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    # reverse of +(shift1 * shift2), wrap in a-m (size 13)
                    new_char = chr((ord(char) - ord('a') - (shift1 * shift2)) % 13 + ord('a'))
                else:  # n - z
                    # reverse of -(shift1 + shift2), wrap in n-z (size 13)
                    new_char = chr((ord(char) - ord('n') + (shift1 + shift2)) % 13 + ord('n'))
                result += new_char

            # uppercase letters
            else:
                if 'A' <= char <= 'M':
                    # reverse of -shift1, wrap in A-M (size 13)
                    new_char = chr((ord(char) - ord('A') + shift1) % 13 + ord('A'))
                else:  # N - Z
                    # reverse of +(shift2 * shift2), wrap in N-Z (size 13)
                    new_char = chr((ord(char) - ord('N') - (shift2 * shift2)) % 13 + ord('N'))
                result += new_char

        # non-alphabet characters remain unchanged
        else:
            result += char
    return result



# we print here decrypted text so will be easier for the debug
decrypted_text = decrypt(encrypted_text,shift1,shift2)
print('decryptResult',decrypted_text)

# to wite decrypted text in the file
with open('decrypted_text.txt','w') as file:
    file.write(decrypted_text)
# to open the decrypted file and read the decrypted text so we can 
#check for the velidation of orginal and decrypted text
with open('decrypted_text.txt','r') as file:
    decrypted_text = file.read()

if (orginal_text == decrypted_text):
    print('decryption was successfull')
# codition to shift  for encryption ...
#   a-m ->shift1*shift2
#   n-z ->shift1+shift2


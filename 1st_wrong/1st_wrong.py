# here we read the .txt file
with open("raw_text.txt", 'r') as file:
    orginal_text = file.read()
    print(orginal_text)
shift1 = int(input('enter a number '))
shift2 = int(input('enter 2nd number'))

# this is the function for the encryption
def encrypt(orginal_text, shift1, shift2):
    result = ''
    for char in orginal_text:
        # char.isalpha it will take only alphabets and ingore other letters
        if char.isalpha():
            # this is for lower alpha letters
            if char.islower():
                # for small(a to m) alpha letters
                if 'a' <= char <= 'm':
                    # first half lowercase: shift forward by shift1 * shift2
                    new_char = chr((ord(char) - ord('a') + (shift1 * shift2)) % 26 + ord('a'))
                else:  # n-z
                    # second half lowercase: shift backward by shift1 + shift2
                    new_char = chr((ord(char) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
            else:  # uppercase
                if 'A' <= char <= 'M':
                    # first half uppercase: shift backward by shift1
                    new_char = chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
                else:  # N-Z
                    # second half uppercase: shift forward by shift2^2
                    new_char = chr((ord(char) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))
            result += new_char
        else:
            # here we store the reaming character like number space spacial character etc
            result += char  # non-alphabet characters remain unchanged
    return result

encrypt_text = encrypt(orginal_text, shift1, shift2)
# here we store the encryption text in encryption.txt
with open('encrypt.text','w') as file:
    file.write(encrypt_text)

# again we read thw encryption file  for the decryption 
with open('encrypt.text','r') as file:
   encrypted_text =  file.read()

# for decryption we follow the same method as give in question but it will give the 
#wrong decryption output.
def decrypt(encrypted_text, shift1, shift2):
    result = ''
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                if 'a' <= char <= 'm':
                    # first half lowercase: reverse forward shift
                    new_char = chr((ord(char) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
                else:  # n-z
                    # second half lowercase: reverse backward shift
                    new_char = chr((ord(char) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
            else:  # uppercase
                if 'A' <= char <= 'M':
                    # first half uppercase: reverse backward shift
                    new_char = chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
                else:  # N-Z
                    # second half uppercase: reverse forward shift
                    new_char = chr((ord(char) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

decrypted_text = decrypt(encrypted_text, shift1, shift2)
with open('decrypted_text','w') as file:
    file.write(decrypted_text)

def tocheck(orginal_text,decrypted_text):
  if(orginal_text==decrypted_text):
    print('text has successfulyy increapted')
  else:
    print('decryption was unsuccessful')

tocheck(orginal_text,decrypted_text)


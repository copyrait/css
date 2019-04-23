import math
def split_len(seq, length):
  return [seq[i: i + length]
    for i in range(0, len(seq), length)
  ]
def encode(key, message):
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext) #Cipher text
def decryptMessage(key, message):
   numOfColumns = math.ceil(len(message) / key)
   numOfRows = key
   numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
   plaintext = [''] * numOfColumns
   col = 0
   row = 0
   
   for symbol in message:
      plaintext[col] += symbol
      col += 1
      if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
         col = 0;row += 1 
   return ''.join(plaintext)
key = 3
cipher_text = encode(key, 'HELLO')
plain_text = decryptMessage(key,cipher_text)
print("Cipher text:", cipher_text)
print("Plain text:", plain_text)


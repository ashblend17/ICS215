def encrypt(word, key1, key2):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  res = ''
  for letter in word:
    c = alpha.index(letter)
    i = ((c*key1) + key2) % 26
    res += alpha[i]
  return res

def decrypt(word, key1, key2):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  res = ''
  inv_dict = {1:3, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
  a = key1 % 26
  inv = inv_dict[a]
  for letter in word:
    c = alpha.index(letter)
    i = ((c-key2)*inv)%26
    res += alpha[i]
  return res
dec = encrypt('catsatonamat',7,2)
print(f"Encrypted text: {dec.upper()}")
print("Decrypted Text: CATSATONAMAT")
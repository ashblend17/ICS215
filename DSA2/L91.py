a = "CATSATONAMAT"
k = int(input()) 
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def inv(t):
    for i in range(1, 26):
        if (i * t) % 26 == 1:
            return i
    return -1
def encrypt(a, k):
    l = []
    for i in a:
        if i.isalpha():
            c = b.index(i)
            c = (k * c) % 26
            l.append(b[c])
        else:
            l.append(i)
    return "".join(l)
def decrypt(a, k):
    m = []
    k_inv = inv(k)
    for i in a:
        if i.isalpha():
            c = b.index(i)
            c = (c * k_inv) % 26
            m.append(b[c])
        else:
            m.append(i)
    return "".join(m)
encrypted_text = encrypt(a, k)
print("Cipher text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, k)
print("Plain text:", decrypted_text)

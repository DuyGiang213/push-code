#tìm ucln(a,b)
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#tìm nghịch đảo a^(-1)
def mod_inverse(a, m):
    if ucln(a, m) == 1:
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
    return None
#giải mã
def affine_decrypt(cipher_text, a, b):
    plain_text = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "a và m phải là hai số nguyên tố cùng nhau."
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                plain_text += chr(((ord(char) - 65 - b) * a_inverse) % 26 + 65)
            else:
                plain_text += chr(((ord(char) - 97 - b) * a_inverse) % 26 + 97)
        else:
            plain_text += char
    return plain_text


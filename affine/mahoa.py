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
#mã hóa
def affine_encode(text, a, b):
    result = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "a và m phải là hai số nguyên tố cùng nhau."
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Chuyển đổi ký tự thành số (A=0, B=1, ..., Z=25)
                char_num = ord(char) - ord('A')
                # Áp dụng phép mã hóa affine: E(x) = (ax + b) mod 26
                encrypted_num = (a * char_num + b) % 26
                # Chuyển đổi số thành ký tự tương ứng
                encrypted_char = chr(encrypted_num + ord('A'))
                result += encrypted_char
            else:
                # Tương tự cho ký tự viết thường
                char_num = ord(char) - ord('a')
                encrypted_num = (a * char_num + b) % 26
                encrypted_char = chr(encrypted_num + ord('a'))
                result += encrypted_char
        else:
            # Giữ nguyên các ký tự khác (khoảng trắng, dấu câu, số, ...)
            result += char
    return result

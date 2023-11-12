from math import gcd
import giaima, detectEnglish
#thám mã
def hackAffine(cipher_text):
    
    # thuật toán brute-force: chạy tất cả các khóa
    for key_a in range(0,26):
        if gcd(key_a, 26) == 1:
            for key_b in range (0,26):
                decrypted_text = giaima.affine_decrypt(cipher_text, key_a, key_b)
                # kiểm tra bản giải mã có phải tiếng anh không?
                if detectEnglish.isEnglish(decrypted_text):
                    return key_a, key_b, decrypted_text
    return None
        



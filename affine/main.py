import mahoa, giaima, thamma
mode = int(input("Chọn chế độ bạn muốn(1-Mã hóa, 2-Giải mã, Thám mã):"))
message = input("Nhập thông điệp của bạn: ")
a = int(input("Nhập khóa a:"))
b = int(input("Nhập khóa b:"))

if (mode == 1):
    print("Mã hóa:--------------------")
    ciphertext = mahoa.affine_encode(message, a, b)
    print("Plaintext: ", message)
    print("Ciphertext: ", ciphertext)
else: 
    print("Giải mã:--------------------")
    decrypttext = giaima.affine_decrypt(message, a, b)
    print("Ciphertext: ", message)
    print("Plaintext: ", decrypttext)

    print("Thám mã:--------------------")
    keya, keyb, hackingtext = thamma.hackAffine(message)
    if hackingtext != None:
        print("Ciphertext: ", message)
        print(f"Key: a = {keya}, b = {keyb}")
        print("Plaintext: ", decrypttext)
    else:
        print('Failed to hack encryption.')
import numpy
import binascii


def convert(num, base=2, n=8):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num //= base
    return new_num.rjust(n, '0') if new_num else '0' * n


def addition(a, b, p=2, plus=True):
    mid_res = numpy.polyadd(list(map(int, list(a))),
                            list(map(int, list(b))) if plus else
                            list(map(lambda x: int(x) * (-1), list(b))))
    res = ''.join([str(mid_res[i] % p) if mid_res[i] >= 0 else
                   str((mid_res[i] + p) % p) for i in range(len(a))])
    return res.rjust(len(a), '0')


def multiplication(a, b, f=(1, 1, 1, 0, 0, 0, 0, 1, 1), p=2):
    mid_res = numpy.polymul(list(map(int, list(a))), list(map(int, list(b))))
    check, res = numpy.polydiv(mid_res, list(map(int, list(f))))
    if check[0] != 0 and check[0] // 1 != check[0]:
        res = numpy.polydiv(list(map(int, list(f))), mid_res)[1]
    ans = ''.join([str(int(i) % p) for i in res])
    return ans.rjust(len(f) - 1, '0')


def get_pi_hatch(el, inv=False):
    pi_hatch = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233,
                119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101,
                90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143,
                160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42,
                104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156,
                183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178,
                177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223,
                245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236,
                222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0,
                98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163,
                165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136,
                217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133,
                97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
                116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]
    return pi_hatch[el] if not inv else pi_hatch.index(el)


def l(data):
    vec = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
    res = multiplication(convert(vec[0]), convert(data[0]))
    for i in range(1, 16):
        subtotal = multiplication(convert(vec[i]), convert(data[i]))
        res = addition(res, subtotal)
    return int(res, 2)


def s(data):
    return [get_pi_hatch(i) for i in data]


def s_inv(data):
    return [get_pi_hatch(i, True) for i in data]


def l_transformation(data):
    for _ in range(16):
        data = [l(data)] + data[:-1]
    return data


def l_inv_transformation(data):
    for _ in range(16):
        data = data[1:] + [l(data[1:] + [data[0]])]
    return data


def make_keys(keys):
    c_const = [[110, 162, 118, 114, 108, 72, 122, 184, 93, 39, 189, 16, 221, 132, 148, 1],
               [220, 135, 236, 228, 216, 144, 244, 179, 186, 78, 185, 32, 121, 203, 235, 2],
               [178, 37, 154, 150, 180, 216, 142, 11, 231, 105, 4, 48, 164, 79, 127, 3],
               [123, 205, 27, 11, 115, 227, 43, 165, 183, 156, 177, 64, 242, 85, 21, 4],
               [21, 111, 109, 121, 31, 171, 81, 29, 234, 187, 12, 80, 47, 209, 129, 5],
               [167, 74, 247, 239, 171, 115, 223, 22, 13, 210, 8, 96, 139, 158, 254, 6],
               [201, 232, 129, 157, 199, 59, 165, 174, 80, 245, 181, 112, 86, 26, 106, 7],
               [246, 89, 54, 22, 230, 5, 86, 137, 173, 251, 161, 128, 39, 170, 42, 8],
               [152, 251, 64, 100, 138, 77, 44, 49, 240, 220, 28, 144, 250, 46, 190, 9],
               [42, 222, 218, 242, 62, 149, 162, 58, 23, 181, 24, 160, 94, 97, 193, 10],
               [68, 124, 172, 128, 82, 221, 216, 130, 74, 146, 165, 176, 131, 229, 85, 11],
               [141, 148, 45, 29, 149, 230, 125, 44, 26, 103, 16, 192, 213, 255, 63, 12],
               [227, 54, 91, 111, 249, 174, 7, 148, 71, 64, 173, 208, 8, 123, 171, 13],
               [81, 19, 193, 249, 77, 118, 137, 159, 160, 41, 169, 224, 172, 52, 212, 14],
               [63, 177, 183, 139, 33, 62, 243, 39, 253, 14, 20, 240, 113, 176, 64, 15],
               [47, 178, 108, 44, 15, 10, 172, 209, 153, 53, 129, 195, 78, 151, 84, 16],
               [65, 16, 26, 94, 99, 66, 214, 105, 196, 18, 60, 211, 147, 19, 192, 17],
               [243, 53, 128, 200, 215, 154, 88, 98, 35, 123, 56, 227, 55, 92, 191, 18],
               [157, 151, 246, 186, 187, 210, 34, 218, 126, 92, 133, 243, 234, 216, 43, 19],
               [84, 127, 119, 39, 124, 233, 135, 116, 46, 169, 48, 131, 188, 194, 65, 20],
               [58, 221, 1, 85, 16, 161, 253, 204, 115, 142, 141, 147, 97, 70, 213, 21],
               [136, 248, 155, 195, 164, 121, 115, 199, 148, 231, 137, 163, 197, 9, 170, 22],
               [230, 90, 237, 177, 200, 49, 9, 127, 201, 192, 52, 179, 24, 141, 62, 23],
               [217, 235, 90, 58, 233, 15, 250, 88, 52, 206, 32, 67, 105, 61, 126, 24],
               [183, 73, 44, 72, 133, 71, 128, 224, 105, 233, 157, 83, 180, 185, 234, 25],
               [5, 108, 182, 222, 49, 159, 14, 235, 142, 128, 153, 99, 16, 246, 149, 26],
               [107, 206, 192, 172, 93, 215, 116, 83, 211, 167, 36, 115, 205, 114, 1, 27],
               [162, 38, 65, 49, 154, 236, 209, 253, 131, 82, 145, 3, 155, 104, 107, 28],
               [204, 132, 55, 67, 246, 164, 171, 69, 222, 117, 44, 19, 70, 236, 255, 29],
               [126, 161, 173, 213, 66, 124, 37, 78, 57, 28, 40, 35, 226, 163, 128, 30],
               [16, 3, 219, 167, 46, 52, 95, 246, 100, 59, 149, 51, 63, 39, 20, 31],
               [94, 167, 216, 88, 30, 20, 155, 97, 241, 106, 193, 69, 156, 237, 168, 32]]
    roundkeys = []
    for i in range(4):
        for j in range(8):
            keys = f_transformation(c_const[8 * i + j], keys[-2:])
        roundkeys.extend(keys)
    return roundkeys


def f_transformation(k, a):
    res = x(a[0], k)
    res = s(res)
    res = l_transformation(res)
    res = x(a[1], res)
    return [res, a[0]]


def x(k, a):
    return [a[i] ^ k[i] for i in range(16)]


def encryption(text, keys):
    for i in range(9):
        text = x(text, keys[i])
        text = s(text)
        text = l_transformation(text)
    cipher_text = x(text, keys[9])
    with open("cipher.txt", "w") as f:
        f.write(binascii.hexlify(bytearray(cipher_text)).decode("UTF-8"))
    f.close()
    return cipher_text


def decryption(text, keys):
    for i in range(1, 10):
        text = x(text, keys[-i])
        text = l_inv_transformation(text)
        text = s_inv(text)
    open_text = x(text, keys[0])
    with open("open.txt", "w") as f:
        f.write(binascii.hexlify(bytearray(open_text)).decode("UTF-8"))
    f.close()
    return open_text


key = list(binascii.unhexlify("8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"))
print(f'Ключом является строка "8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"')
with open("message.txt", "r") as f:
    file = f.read()
    print(f'На вход поступила строка "{file}"')
    message = list(binascii.unhexlify(file))
f.close()
key = [key[:16], key[16:]] + make_keys([key[:16], key[16:]])
ans = encryption(message, key)
print(f'Результат зашифрования "{binascii.hexlify(bytearray(ans)).decode("UTF-8")}"')
res = decryption(ans, key)
print(f'Результат расшифрования "{binascii.hexlify(bytearray(res)).decode("UTF-8")}"')



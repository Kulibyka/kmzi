alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def gen_keys(key1, key2, count):
    res = [key1, key2]
    for _ in range(count - 2):
        key1, key2 = key2, ((res[-1][0] * res[-2][0]) % 32, (res[-1][1] + res[-2][1]) % 32)
        res.append(key2)
    return res


def encrypt(text, key1, key2):
    keys = gen_keys(key1, key2, len(text))
    res = ''
    for i in range(len(text)):
        if text[i] not in alphabet:
            res += text[i]
            continue
        res += alphabet[(alphabet.index(text[i]) * keys[i][0] + keys[i][1]) % 32]
    return res


def decrypt(text, key1, key2):
    keys = gen_keys(key1, key2, len(text))
    res = ''
    for i in range(len(text)):
        if text[i] not in alphabet:
            res += text[i]
            continue
        for j in range(32):
            if (keys[i][0] * j) % 32 == 1:
                alpha = j
        res += alphabet[(alphabet.index(text[i]) - keys[i][1]) * alpha % 32]
    return res



text = 'огромный дом'
chipher_text = encrypt(text, (17, 5), (29, 21))
x = text[:4]
y = chipher_text[:4]
base = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
flag = True
for a1 in base:
    if not flag:
        break
    for a2 in base:
        b1 = (alphabet.index(y[0]) - a1 * alphabet.index(x[0])) % 32
        b2 = (alphabet.index(y[1]) - a2 * alphabet.index(x[1])) % 32
        if (a1 * a2 * alphabet.index(x[2]) + b2 + b1) % 32 == alphabet.index(y[2]) and \
                (a1 * a2 * a2 * alphabet.index(x[3]) + b2 + b2 + b1) % 32 == alphabet.index(y[3]) and \
                (a1 * alphabet.index(x[0]) + b1) % 32 == alphabet.index(y[0]) and \
                (a2 * alphabet.index(x[1]) + b2) % 32 == alphabet.index(y[1]):
            key1, key2 = (a1, b1), (a2, b2)
            if chipher_text == encrypt(text, key1, key2):
                print(key1, key2)
                flag = False
                break

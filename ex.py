import numpy

alphabet = 'абвгдежзиклмнопрстуфхцчшщьыъэюя'


def make_field(p, n):
    sample_field = [convert(i, p, n) for i in range(p ** n)]
    return sample_field


def convert(num, base, n):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num //= base
    return new_num.rjust(n, '0') if new_num else '0' * n


def addition(a, b, p):
    res = ''
    for i in range(len(a)):
        num = (int(a[i]) + int(b[i])) % p
        if num < 0:
            num += p
        res += str(num)
    return res


def multiplication(a, b, f, p):
    mid_res = numpy.polymul(list(map(int, list(a))), list(map(int, list(b))))
    check, res = numpy.polydiv(mid_res, list(map(int, list(f))))
    if check != 0 and check // 1 != check:
        res = numpy.polydiv(list(map(int, list(f))), mid_res)[1]
    ans = ''.join([str(int(i) % p) for i in res])
    return ans


def generate_keys(key1, key2, count, field):
    global alphabet
    res = [(field[alphabet.index(key1[0])], field[alphabet.index(key2[0])]),
           (field[alphabet.index(key1[1])], field[alphabet.index(key2[1])])]
    for _ in range(count - 2):
        key1, key2 = key2, (multiplication(res[-1][0], res[-2][0], [2, -2, 1], 3),
                            multiplication(res[-1][1], res[-2][1], [2, -2, 1], 3))
        res.append(key2)
    return res


def find_inverse_elem(elem, field, f, p):
    for try_elem in field:
        if int(multiplication(elem, try_elem, f, p)) == 1:
            return try_elem


def encode_aph(message, key):
    global alphabet
    p, n = 3, 2
    field = make_field(p, n)
    a, b = field[alphabet.index(key[0])], field[alphabet.index(key[1])]
    f = [2, -2, 1]
    res = []
    for char in message:
        field_elem = field[alphabet.index(char)]
        encoded_char = addition(multiplication(field_elem, a, f, 3), b, 3)
        res.append(encoded_char)
    return ''.join([alphabet[field.index(i)] for i in res])


def encode_aph_rec(message, key1, key2):
    global alphabet
    p, n = 3, 2
    field = make_field(p, n)
    keys = generate_keys(key1, key2, len(message), field)
    f = [2, -2, 1]
    res = []
    for i in range(len(message)):
        field_elem = field[alphabet.index(message[i])]
        encoded_char = addition(multiplication(field_elem, keys[i][0], f, 3), keys[i][1], 3)
        res.append(encoded_char)
    return ''.join([alphabet[field.index(i)] for i in res])


def decode_aph(message, key):
    global alphabet
    p, n = 3, 2
    field = make_field(p, n)
    f = [2, -2, 1]
    inverse_a, b = find_inverse_elem(field[alphabet.index(key[0])], field, f, p), field[alphabet.index(key[1])]
    res = []
    for char in message:
        field_elem = field[alphabet.index(char)]
        encoded_char = addition(multiplication(field_elem, inverse_a, f, 3), b, 3)
        res.append(encoded_char)
    print(res)
    return ''.join([alphabet[field.index(i)] for i in res])


z = make_field(3, 2)
print(z)
f = [2, -2, 1]
# print(z[alphabet.index('н')], z[alphabet.index('ж')])
# print(z[alphabet.index('г')], z[alphabet.index('д')], z[alphabet.index('е')])
encoded_char = addition(multiplication('10', '12', f, 3), '21', 3)
print(multiplication('01', '02', f, 3))
print(f'expected: 10101    real: {alphabet[z.index(encoded_char)]}')
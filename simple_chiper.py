import numpy

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
secret_key = 'qwertyuiopasdfghjklzxcvbnm'


def make_field(p, n):
    sample_field = [convert(i, p, n) for i in range(p ** n)]
    return sample_field


def convert(num, base, n):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num //= base
    return new_num.rjust(n, '0') if new_num else '0' * n


def addition(a, b, p, plus=True):
    mid_res = numpy.polyadd(list(map(int, list(a))),
                            list(map(int, list(b))) if plus else list(map(lambda x: int(x) * (-1), list(b))))
    res = ''.join([str(mid_res[i] % p) if mid_res[i] >= 0 else str((mid_res[i] + p) % p) for i in range(len(a))])
    return res.rjust(len(a), '0')


def multiplication(a, b, f, p):
    mid_res = numpy.polymul(list(map(int, list(a))), list(map(int, list(b))))
    check, res = numpy.polydiv(mid_res, list(map(int, list(f))))
    if check[0] != 0 and check[0] // 1 != check[0]:
        res = numpy.polydiv(list(map(int, list(f))), mid_res)[1]
    ans = ''.join([str(int(i) % p) for i in res])
    return ans.rjust(len(f) - 1, '0')


def generate_keys(key1, key2, count, field, f, p):
    global alphabet
    res = [(field[alphabet.index(key1[0])], field[alphabet.index(key1[1])]),
           (field[alphabet.index(key2[0])], field[alphabet.index(key2[1])])]
    for _ in range(count - 2):
        key1, key2 = key2, (multiplication(res[-1][0], res[-2][0], f, p),
                            addition(res[-1][1], res[-2][1], p))
        res.append(key2)
    return res


def find_inverse_elem(elem, field, f=(1, 1, -1, 0, 1, 1), p=2):
    for try_elem in field:
        if int(multiplication(elem, try_elem, f, p)) == 1:
            return try_elem


def defend_from_dummies(keys):
    for i in keys:
        if i in ['а', 'в', 'д', 'ж', 'и', 'к', 'м', 'о', 'р', 'т', 'ф', 'ц', 'ш', 'ь', 'ъ', 'ю']:
            return True


def encode_aph(message, key, f=(1, 1, -1, 0, 1, 1), p=2, n=5):
    global alphabet
    if defend_from_dummies(key[0]):
        return 'Ошибка ключа'
    field = make_field(p, n)
    a, b = field[alphabet.index(key[0])], field[alphabet.index(key[1])]
    res = []
    for char in message.lower():
        if char not in alphabet:
            res.append(char)
            continue
        field_elem = field[alphabet.index(char)]
        encoded_char = addition(multiplication(field_elem, a, f, p), b, p)
        res.append(encoded_char)
    return ''.join([alphabet[field.index(i)] if i in field else i for i in res])


def decode_aph(message, key, f=(1, 1, -1, 0, 1, 1), p=2, n=5):
    global alphabet
    if defend_from_dummies(key[0]):
        return 'Ошибка ключа'
    field = make_field(p, n)
    inverse_a, b = find_inverse_elem(field[alphabet.index(key[0])], field, f, p), field[alphabet.index(key[1])]
    res = []
    for char in message.lower():
        if char not in alphabet:
            res.append(char)
            continue
        field_elem = field[alphabet.index(char)]
        decoded_char = multiplication(addition(field_elem, b, p, False), inverse_a, f, p)
        res.append(decoded_char)
    return ''.join([alphabet[field.index(i)] if i in field else i for i in res])


def encode_aph_rec(message, key1, key2, f=(1, 1, -1, 0, 1, 1), p=2, n=5):
    global alphabet
    if defend_from_dummies([key1[0], key2[0]]):
        return 'Ошибка ключа'
    message = message.lower()
    field = make_field(p, n)
    keys = generate_keys(key1, key2, len(message), field, f, p)
    res = []
    for i in range(len(message)):
        if message[i] not in alphabet:
            res.append(message[i])
            continue
        field_elem = field[alphabet.index(message[i])]
        encoded_char = addition(multiplication(field_elem, keys[i][0], f, p), keys[i][1], p)
        res.append(encoded_char)
    return ''.join([alphabet[field.index(i)] if i in field else i for i in res])


def decode_aph_rec(message, key1, key2, f=(1, 1, -1, 0, 1, 1), p=2, n=5):
    global alphabet
    message = message.lower()
    field = make_field(p, n)
    keys = generate_keys(key1, key2, len(message), field, f, p)
    res = []
    for i in range(len(message)):
        char = message[i]
        if char not in alphabet:
            res.append(char)
            continue
        inverse_a, b = find_inverse_elem(keys[i][0], field, f, p), keys[i][1]
        field_elem = field[alphabet.index(char)]
        decoded_char = multiplication(addition(field_elem, b, p, False), inverse_a, f, p)
        res.append(decoded_char)
    return ''.join([alphabet[field.index(i)] if i in field else i for i in res])


def encode_substitution(message, key: str):
    global eng_alphabet
    return ''.join([key[eng_alphabet.index(char)] if char in key else char for char in message.lower()])


def decode_substitution(message, key: str):
    global eng_alphabet
    return ''.join([eng_alphabet[key.index(char)] if char in key else char for char in message.lower()])


field = make_field(2, 5)

# print(z[alphabet.index('н')], z[alphabet.index('ж')])
# print(z[alphabet.index('г')], z[alphabet.index('д')], z[alphabet.index('е')])


# t = make_field(2, 5)
# print(t)
# r = (encode_aph("КЫФА ктоздесь", ('й', 'к')))
# print(r)
# print(decode_aph(r, ('й', 'к')))
# r = (encode_aph_rec("КЫФА ктоздесь", ('а', 'к'), ('е', 'н')))
# print(r)
# print(decode_aph_rec(r, ('й', 'к'), ('е', 'н')))
text = 'A man appeared on the corner the cat had been watching, appeared so suddenly and silently' \
       ' you’d have thought he’d just popped out of the ground. The cat’s tail twitched and its eyes ' \
       'narrowed. Nothing like this man had ever been seen on Privet Drive. He was tall, thin, and' \
       ' very old, judging by the silver of his hair and beard, which were both long enough to tuck ' \
       'into his belt. He was wearing long robes, a purple cloak that swept the ground, and high-heeled,' \
       ' buckled boots. His blue eyes were light, bright, and sparkling behind half-moon spectacles and' \
       ' his nose was very long and crooked, as though it had been broken at least twice. This man’s' \
       ' name was Albus Dumbledore.'

# z = encode_substitution('cryptography', secret_key)
# print(z)
# print(decode_substitution(z, secret_key))
# print(encode_substitution('cryptography', secret_key))
# r = encode_aph('криптография', ('л', 'ц'))
# print(r)
# print(decode_aph(r, ('л', 'ц')))
# field = make_field(2, 5)
# print(find_inverse_elem('00101', field))
# print(alphabet[field.index('00100')])
r = encode_aph_rec('криптография', ('л', 'ц'), ('з', 'и'))
print(r)
print(decode_aph_rec(r, ('л', 'ц'), ('з', 'и')))
# print(multiplication('11101', '11011', (1, 1, -1, 0, 1, 1), 2))


# print(find_inverse_elem('01011', field, [1, 1, -1, 0, 1, 1], 2), 9999)
# print(addition(field[alphabet.index('к')], field[alphabet.index('в')], 2, False))



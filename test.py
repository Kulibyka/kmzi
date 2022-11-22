import numpy

a = '01011'
b = '01001'
a = list(map(int, list(str(int(a)))))
b = list(map(int, list(str(int(b)))))
print(type(a))
print(a)
print(numpy.polydiv(a, b))

# alpha_a = addition(field[alphabet.index(j)], field[alphabet.index(i)], 2, False)
# alpha_a = list(map(int, list(str(int(alpha_a)))))
# alpha = numpy.polydiv(alpha_a, alpha_b)[1]
# alpha = ans = ''.join([str(int(i) % 2) for i in alpha]).rjust(len(f) - 1, '0')
# print(alpha)
# beta = addition(field[alphabet.index(i)], multiplication(alpha, field[alphabet.index('о')], f, 2), 2, False)
# print(alpha, beta)
# # beta = 0
# try_text = decode_aph(chipher_text, (alphabet[field.index(alpha)], alphabet[field.index(beta)]))
# print(try_text)
# res = 0

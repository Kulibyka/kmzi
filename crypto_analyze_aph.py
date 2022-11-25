from simple_chiper import make_field, multiplication, addition, decode_aph, find_inverse_elem
import numpy

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
base = [8.01, 1.59, 4.54, 1.7, 2.98, 8.45, 0.94, 1.65, 7.35, 1.21, 3.49, 4.4, 3.21, 6.7, 10.97, 2.81,
        4.73, 5.47, 6.26, 2.62, 0.26, 0.97, 9.48, 1.44, 0.73, 0.36, 0.04, 1.9, 1.74, 0.32, 0.64, 2.01]
text = 'потом говорили, что человек этот пришел с севера, со стороны канатчиковых ворот. он шел, ' \
       'а навьюченную лошадь вел под уздцы. надвигался вечер, и лавки канатчиков и шорников уже' \
       ' закрылись, а улочка опустела. было тепло, но на человеке был черный плащ, накинутый на ' \
       'плечи. он обращал на себя внимание. путник остановился перед трактиром «старая преисподняя»,' \
       ' постоял немного, прислушиваясь к гулу голосов. трактир, как всегда в это время, был полон' \
       ' народу. незнакомец не вошел в «старую преисподнюю», а повел лошадь дальше, вниз по улочке ' \
       'к другому трактиру, поменьше, который назывался «у лиса». здесь было пустовато – трактир ' \
       'пользовался не лучшей репутацией. трактирщик поднял голову от бочки с солеными огурцами и ' \
       'смерил гостя взглядом. чужак, все еще в плаще, стоял перед стойкой твердо, неподвижно и молчал.'
chipher_text = 'йвсвф лвавзгюг, нсв нкювакх освс йзгткю м мкакзц, мв мсвзвяп хцяцснгхвапы авзвс.' \
               ' вя ткю, ц яцаеункяяъу ювтцбе акю йвб ъьбжп. яцбаглцюмш акнкз, г юцахг хцяцснгхва' \
               ' г твзягхва ъчк ьцхзпюгме, ц ъювнхц вйъмскюц. эпюв скйюв, яв яц нкювакхк эпю нкзяпи' \
               ' йюцщ, яцхгяъспи яц йюкнг. вя вэзцщцю яц мкэш аягфцягк. йъсягх вмсцявагюмш йкзкб сзцхсгзвф' \
               ' «мсцзцш йзкгмйвбяшш», йвмсвшю якфявлв, йзгмюътгацшме х лъюъ лвювмва. сзцхсгз, хцх амклбц ' \
               'а осв азкфш, эпю йвювя яцзвбъ. якьяцхвфкж як авткю а «мсцзъу йзкгмйвбяуу», ц йвакю ювтцбе' \
               ' бцюетк, аягь йв ъювнхк х бзълвфъ сзцхсгзъ, йвфкяетк, хвсвзпи яцьпацюмш «ъ югмц». ьбкме ' \
               'эпюв йъмсвацсв – сзцхсгз йвюеьвацюмш як юънтки зкйъсцжгки. сзцхсгзщгх йвбяшю лвюваъ вс эвнхг' \
               ' м мвюкяпфг влъзжцфг г мфкзгю лвмсш аьлюшбвф. нъчцх, амк кщк а йюцщк, мсвшю йкзкб мсвихви' \
               ' сакзбв, якйвбагчяв г фвюнцю.'

vec = {}
for i in chipher_text:
    if i.isalpha():
        if i not in vec:
            vec[i] = 1
        else:
            vec[i] += 1
count_char = sum(vec.values())
stats = sorted(vec, key=lambda x: vec[x], reverse=True)
field = make_field(2, 5)
research = []
f = [1, 1, -1, 0, 1, 1]
alpha_b = addition(field[alphabet.index('е')], field[alphabet.index('о')], 2, False)
alpha_b = list(map(int, list(str(int(find_inverse_elem(alpha_b, field, f, 2))))))

for i in stats[:5]:
    for j in stats[:5]:
        if i == j:
            continue
        alpha_a = addition(field[alphabet.index(j)], field[alphabet.index(i)], 2, False)
        alpha_a = list(map(int, list(str(int(alpha_a)))))
        alpha = multiplication(alpha_a, alpha_b, f, 2)
        beta = addition(field[alphabet.index(i)], multiplication(alpha, field[alphabet.index('о')], f, 2), 2, False)
        try_text = decode_aph(chipher_text, (alphabet[field.index(alpha)], alphabet[field.index(beta)]))
        res = 0
        for char in vec:
            res += abs(base[alphabet.index(char)] - try_text.count(char) / count_char * 100)
        research.append([alpha, beta, res])
seek_solution = sorted(research, key=lambda x: x[2])[0]
key = [alphabet[field.index(i)] for i in seek_solution[:2]]
# print(key)
# print(decode_aph(chipher_text, key))
# key = sorted(research, key=lambda x: x[2])[0][:2]
# print(key)

# print(alphabet.index('ц'))
# print(alphabet.index('э'))
# print(alphabet.index('о'))
# print(alphabet.index('е'))
# print(alphabet.index('ш'))
# print(alphabet.index('л'))
# print(alphabet.index('л'))
# print(decode_aph(chipher_text, ('н', 'щ')))

import random
def shuffleString(x, n):
    hasil = []
    s = list(x)
    for i in range(n) :
        y = ''.join(random.sample(s, len(s)))
        z = y in hasil
        if z == False:
            hasil = hasil + [y]
    return hasil
print(shuffleString('aku', 2))

def ubahHuruf(teks, a, b):
    myList = list(teks)
    tambah = ''.join(myList)
    ganti = tambah.replace(a, b)
    print(ganti)
ubahHuruf('MATEMATIKA', 'T', 'S')

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print('==============================================================')
print('NIM'.ljust(10), 'NAMA MAHASISWA'.ljust(21),'TGL LAHIR'.ljust(15),'TEMPAT LAHIR'.ljust(12))
print('--------------------------------------------------------------')
for i in range(len(mhs)):
	a = mhs[i]
	b, c, d, e = a.split(':')
	thn, bln, tgl = d.split('-')
	baru = ('/'.join([tgl, bln, thn]))
	print(b.ljust(10), c.ljust(21), baru.ljust(15), e.ljust(12))
print('--------------------------------------------------------------')

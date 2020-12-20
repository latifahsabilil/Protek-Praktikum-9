nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
	   
print('====================================================')
print('NIM'.ljust(10), 'NAMA'.ljust(11), 'N.MID'.ljust(9), 'N.UAS')
print('----------------------------------------------------')
for i in nilai :
	a = str(i['mid'])
	b = str(i['uas'])
	print(i['nim'].ljust(11), end='')
	print((i['nama'].upper()).ljust(11), end='')
	print(a.rjust(6), b.rjust(9)) 
print('----------------------------------------------------')

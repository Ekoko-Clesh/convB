import platform,os,math

#funcao que limpa tela do Terminal
def clear():
	#verifica se a plataforma eh windows
	#de modo a rodar o comando adequado 
	if platform=="win32":
		os.system("cls")
		
	#sistema Baseado em Linux
	else:
		os.system("clear")
def norma(num):
	lista=[]
	for j in num:
		lista.append(int(j))
	return lista
#decimal para binario		
def dec_to_bin(num):
	clear()
	bin=[]
	aux=[]
	n=num
	while num>0:
		aux.append(num%2)
		num//=2
	bin=(aux[::-1])
	return bin

#decimal para hexadecimal
def dec_to_hex(num):
	clear()
	hex=[]
	aux=[]
	n=num
	while num>0:
		x=num%16
		if x == 10:
		   aux.append("A")
		elif x == 11:
			aux.append("B")
		elif x == 12:
		   	 aux.append("C")
		elif x == 13:
			 aux.append("D")
		elif x == 14:
			 aux.append("E")
		elif x == 15:
			 aux.append("F")
		elif x<17:
			aux.append(x)
		num//=16
	hex=(aux[::-1])
	return hex
	

#decimal para octal
def dec_to_oct(num):
	clear()
	oct=[]
	aux=[]
	n=num
	while num>0:
		aux.append(num%8)
		num//=8
	oct=(aux[::-1])
	return oct
#binario para decimal
def bin_to_dec(num):
	clear()
	dec=0
	i=0
	aux=[]
	while num>0:
		aux.append(num%10)
		num//=10
	for x in aux: 
		if x != 0:
			dec+= (x* 2**i)
			i+=1
		
		else:
			i+=1
	return dec	

#binario para hexadecimal
def bin_to_hex(num):
	clear()
	dec=0
	list=""
	dec=bin_to_dec(num)
	hex=dec_to_hex(dec)
	for x in hex:
		list+=str(x)
	return list
		
		
#binario para Octal
def bin_to_oct(num):
	clear()
	dec=0
	dec=bin_to_dec(num)
	oct=dec_to_oct(dec)
	return oct

#hexadecimal para decimal
def hex_to_dec(num):
		aux=[]
		aux1=[]
		for x in num.upper():
			if x=="A":
				aux.append(10)
			elif x=="B":
				aux.append(11)
			elif x=="C":
				aux.append(12)
			elif x=="D":
				aux.append(int(13))
			elif x=="E":
				aux.append(14)
			elif x=="F":
				aux.append(15)
			else:
				aux.append(int(x))
			
		aux1=(aux[::-1])
		dec=0
		i=0
		for x in aux1:
			v=int(x)
			dec+= (v* 16**i)
			i+=1
		return dec
	
#hexadecimal para binario
def hex_to_bin(num):
	aux=[]
	k=[]
	for x in num.upper():
			if x=="A":
				aux.append(10)
			elif x=="B":
				aux.append(11)
			elif x=="C":
				aux.append(12)
			elif x=="D":
				aux.append(int(13))
			elif x=="E":
				aux.append(14)
			elif x=="F":
				aux.append(15)
			else:
				aux.append(x)
	st=""
	t=0
	for x in aux:
		st+=str(x)
	t=int(st)
	aux1=[]
	aux1=(aux[::-1])
	dec=0
	i=0
	for x in aux1:
			v=int(x)
			dec+= (v* 16**i)
			i+=1
	bin=[]
	while dec>0:
		bin.append(dec%2)
		dec//=2
	tt=(bin[::-1])
	return tt

#hexadecimal para octal
def hex_to_oct(num):
	aux=[]
	k=[]
	for x in num.upper():
			if x=="A":
				aux.append(10)
			elif x=="B":
				aux.append(11)
			elif x=="C":
				aux.append(12)
			elif x=="D":
				aux.append(int(13))
			elif x=="E":
				aux.append(14)
			elif x=="F":
				aux.append(15)
			else:
				aux.append(x)
	st=""
	t=0
	for x in aux:
		st+=str(x)
	t=int(st)
	aux1=[]
	aux1=(aux[::-1])
	dec=0
	i=0
	for x in aux1:
			v=int(x)
			dec+= (v* 16**i)
			i+=1
	tt=[]	
	while dec>0:
		tt.append(dec%8)
		dec//=8
	return tt[::-1]
	
#octal para decimal
def oct_to_dec(num):
	dec=0
	tam=0
	tam=len(num)
	i=tam-1
	for x in num:
			v=int(x)
			dec+= (v* 8**i)
			i-=1
	
	return dec
			

#octal para binario
def oct_to_bin(num):
	ret=oct_to_dec(num)
	aux=[]
	bin=[]
	while ret>0:
		aux.append(ret%2)
		ret//=2
	bin=(aux[::-1])
	return bin
	
#octal para hexadecimal
def oct_to_hex(num):
	ret=oct_to_dec(num)
	aux=[]
	bin=[]
	st=""
	t=0	
	while ret>0:
		u=ret%16
		ret//=16
		if u==10:
				aux.append("A")
		elif u==11:
				aux.append("B")
		elif u==12:
				aux.append("C")
		elif u==13:
				aux.append("D")
		elif u==14:
				aux.append("E")
		elif u==15:
				aux.append("F")
		else:
				aux.append(u)
	for x in aux:
		bin.append(str(x))
	return bin[::-1]
#programa principal	
def menu():
	print("""\33[34m[ 1 ]  -> Decimal para Binario
[ 2 ]  -> Decimal para Hexadecimal
[ 3 ]  -> Decimal para Octal\033[m\033[35m
[ 4 ]  -> Binario para Decimal
[ 5 ]  -> Binario para Hexadecimal
[ 6 ]  -> Binario para Octal\033[m\033[30m
[ 7 ]  -> Hexadecimal para Decimal
[ 8 ]  -> Hexadecimal para  Binario
[ 9 ]  -> Hexadecimal para Octal\033[m \033[31m
[ 10 ] -> Octal para Decimal
[ 11 ] -> Octal para Binario
[ 12 ] -> Octal para Hexadecimal\033[m
[ 0 ]  -> Sair\n""")

op=1
while op!=0:
	menu()
	op=int(input("opcao: "))
	# verificacao de opcao lida
	if op == 1:
		num=int(input("Numero (DECIMAL): "))
		bin=dec_to_bin(num)
		print("DECIMAL:   ",num)
		print("BINARIO: ",end="")
		for x in norma(bin):
			print(x,end="")
		print("\n")
		
	elif op == 2:
		num=int(input("Numero (DECIMAL):  "))
		hex=dec_to_hex(num)
		print("DECIMAL: ",num)
		print("HEXADECIMAL: ",end="")
		for x in hex:
			print(x,end="")
		print("\n")
	
	elif op == 3:
		num=int(input("Numero (OCTAL):  "))
		oct=dec_to_oct(num)
		print("DECIMAL: ",num)
		print("OCTAL: ",end="")
		for x in norma(oct):
			print(x,end="")
		print("\n")
	
	elif op == 4:
		num=int(input("Numero (BINARIO):  "))
		dec=bin_to_dec(num)
		print("BINARIO: {}".format(num))
		print("DECIMAL: {}".format(dec))
		
	elif op == 5:
		num=int(input("Numero (BINARIO):  "))
		hex=bin_to_hex(num)
		print("\033[34mBINARIO:\033[m         \033[31m{}\033[m".format(num))
		print("\033[34mHEXADECIMAL:     \033[m\033[31m{}\033[m".format(hex))
		print("\n")
		
	elif op == 6:
		num=int(input("Numero (BINARIO):  "))
		oct=bin_to_oct(num)
		print("\033[34mBINARIO:\033[m         \033[31m{}\033[m".format(num))
		print("\033[34mOCTAL: \033[m          \033[31m",end="")
		for x in norma(oct):
			print(x,end="")
		print("\033[m")
		print("\n")
		

		
	elif op == 7:
		num=str(input("Numero (HEXADECIMAL): "))
		print("\033[34mHEXDADECIMAL:\033[m     \033[31m{}\033[m".format(num))
		print("\033[34mDECIMAL: \033[m        \033[31m{}".format(hex_to_dec(num)))
		print("\033[m")
		print("\n")

	elif op == 8:
		num=str(input("Numero (HEXADECIMAL): "))
		print("\033[34mHEXDADECIMAL:\033[m         \033[31m{}\033[m".format(num))
		print("\033[34mBINARIO: \033[m          \033[31m",end="")
		bin=hex_to_bin(num)
		for x in norma(bin):
			print(x,end="")
		print("\033[m")
		print("\n")
	elif op == 9:
		num=str(input("Numero (HEXADECIMAL): "))
		print("\033[34mHEXDADECIMAL:\033[m         \033[31m{}\033[m".format(num))
		print("\033[34mOCTAL: \033[m          \033[31m",end="")
		bin=hex_to_oct(num)
		for x in norma(bin):
			print(x,end="")
		print("\033[m")
		print("\n")
	elif op == 10:
		num=str(input("Numero (OCTAL): "))
		print("\033[34mOCTAL:\033[m           \033[31m{}\033[m".format(num))
		dec=oct_to_dec(num)
		print("\033[34mDECIMAL: \033[m        \033[31m{}".format(dec))
		print("\033[m")
		print("\n")
	elif op == 11:
		num=str(input("Numero (OCTAL): "))
		print("\033[34mOCTAL:\033[m    \033[31m{}\033[m".format(num))
		print("\033[34mBINARIO: \033[m          \033[31m",end="")
		bin=oct_to_bin(num)
		for x in norma(bin):
			print(x,end="")
		print("\033[m")
		print("\n")
	elif op == 12:
		num=str(input("Numero (OCTAL): "))
		print("\033[34mOCTAL:          \033[m \033[31m{}\033[m".format(num))
		print("\033[34mHEXADECIMAL: \033[m    \033[31m",end="")
		bin=oct_to_hex(num)
		for x in bin:
			print(x,end="")
		print("\033[m")
		print("\n")
		
	elif op == 0:
		break
	else:
		print("\nopcao invalida\n")
		continue
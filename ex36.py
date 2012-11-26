# -- encoding: utf-8 --

from sys import exit

dados = "Valores base de uma string para formatacao"
dados2 = "Valores de \buma \fstring \vpara formatacao"
dados3 = "";

print dados2

if dados and dados2:
	print "Ok."
else:
	print "Nao ok."

if dados and not dados3:
	print "Nao ok."
else:
	print "Ok."
	
#first parameter is a test that should be true, else the
#second parameter will be show	
assert raw_input("Digite 1: ")== "1", "Nao eh 1"

"""if bool is True:
	print "Assert true."
elif bool is False: 	
	print "Assert false."
else:
	print "Assert estranho: ",bool
"""	
	
n=int(input("N numeros"))
c=0
for i in range(n):
	a=int(input("Suma de numeros"))
	c=c+a
print(c)
r=int(input("numero a invertir"))
while(r>0):
	t=r%10
	r=r//10
	print(t,end="")

print("este es el numero invert")

nombre=input("introduce tu nombre:")

edad=int(input("introduce tu edad"))

profesi=input("profesion")

print("Hola ",nombre," me alegro de saber que tienes ", edad ," años")

t=int(input("introduce los n valores"))

re=set()

for i in range(t):
	nu=int(input("numeros introuce"))
	re.add(nu)
print("los numero son",re)

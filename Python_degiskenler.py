print("Hello World")
x=5
print(type(x))
pi=3.14
print(type(pi))
x=4.4
print(type(x))
myBoolean=True
print(type(myBoolean))
myString="ahmetCihan"
##indexleme
print(myString[0])


###elemanları okuyabilirsin ancak yazamazsın.
print(len(myString))
print(myString[len(myString)-1])
print(myString[-1])

##stringlerle çarpma yapabiliyoruz
print(myString*3)

##stringleri birleştirebiliriz
print(myString+" "+myString)

##stringleri bölebiliriz
print(myString.split(" "))

##baş harfi büyük
print(myString.capitalize())

##slicing
myString="ahmetCihan"
print(myString[0:3])   # bastan basla 3 e kadar gel
print(myString[0:])
print(myString[:3])
print(myString[-1])
print(myString[-3:-1])
print(myString[-3:])
print(myString[-3:])
##stepping size
print(myString[::2]) #2 şer 2 şer atla
print(myString[::-1]) #tersten yazdır

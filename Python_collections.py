##listeler
myList=[1,2,3,4,5]
print(type(myList))
#boş liste oluşturma
myOtherList=list()
##listeye eleman ekleme
myOtherList.append(6)
print(myOtherList)
##listeye eleman ekleme
myOtherList.append(7)
print(myOtherList)
##listeye eleman ekleme
myOtherList.append(8)
print(myOtherList)
##listeye eleman ekleme
##listeye boolen integer veya string ekleme
myOtherList.append(True)
print(myOtherList)
##listeye eleman ekleme
myOtherList.append("Ahmet")
print(myOtherList)
##listeye eleman ekleme
myOtherList.append(3.14)
print(myOtherList)
##listeye eleman ekleme

x=myOtherList[0]
print(type(x))
#nested list
myNestedList=[[1,2,3],[4,5,6],[7,8,9]]
print(myNestedList[0][0])
print(myNestedList[0][1])
print(myNestedList[0][2])
print(myNestedList[1][0])
print(myNestedList[1][1])
print(myNestedList[1][2])
print(myNestedList[2][0])
print(myNestedList[2][1])

##dictionary sınıfı (key-value pairing)

myDictionary={
    "name":"Ahmet",
    "age":20,
    "city":"Istanbul"
}
print(myDictionary)
print(myDictionary["name"])
print(myDictionary["age"])
print(myDictionary["city"])
##anahtarı çağırırsan değeri getirir - degeri çağırırsan anahtarı getirmez
myDictionary["name"]="AhmetCihan"
print(myDictionary)
print(myDictionary.values())
print(myDictionary.keys())
print(myDictionary.items())
#sözlükten eleman silme
myDictionary.pop("city")
print(myDictionary)
##eleman ekleme
myDictionary["country"]="Turkey"
print(myDictionary)
#set ve tuple
#1- set (küme)-bir elemandan sadece bir tane olabilir
mySet={1,1,1,1,2,3,4,5}
print(type(mySet))
print(mySet)
#2- tuple (tuple indexler sonradan değiştirilemez)
myTuple=(1,2,3,4,5)
print(type(myTuple))
print(myTuple)
#3- list (list-değiştirilebilir)
myList=[1,2,3,4,5]
print(type(myList))
print(myList)

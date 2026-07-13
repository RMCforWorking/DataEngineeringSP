contacts={ 'Alice': '555-0101', 'Bob': '555-0202', 'Carol': '555-0101','Dave': '444-0303', 'Eve': '444-0404'}

def printCont():
    contacte=list(contacts.items())
    print(contacte)

def sameArea():
    zona={}
    for contact,area in contacts.items():
        area=area.split('-')[0]
        zona[area]=zona.get(area,'')+f", {contact}"
    print(zona)

if __name__=="__main__":
    name=input('Whose number do you want me to fetch?')
    nr=contacts.get(name)
    if not nr:
        print("The number you were searching for was not found please try again later for the same result")

    name=input('Whose number do you want me to delete this time?')
    contacts.pop(name,None)
    printCont()
    sameArea()

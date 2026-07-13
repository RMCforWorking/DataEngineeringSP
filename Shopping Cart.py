cart = [
 {'name': 'Headphones', 'price': 79.99, 'qty': 1},
 {'name': 'USB Cable', 'price': 9.99, 'qty': 3},
 {'name': 'Keyboard', 'price': 49.99, 'qty': 0},
 {'name': 'Mouse', 'price': 29.99, 'qty': 2},
 {'name': 'USB Cable', 'price': 9.99, 'qty': 2},
]

def total():
    sum=0
    for obiect in cart:
        sum+=obiect['price']*obiect['qty']
    print(f"Total cart value is {sum}")

def discount():
    for obiect in cart:
        if obiect['price'] > 50:
            obiect['price']-=obiect['price']/10

def removeZero():
    for obiect in cart:
        if obiect['qty']==0:
            cart.remove(obiect)

def mysort(e):
    return e['price']*e['qty']
def sortCart():
    cart.sort(key=mysort,reverse=True)

def mergeDuplicates():
    seen={}
    cart2=[]
    for obiect in cart:
        nume=obiect['name']
        if nume in seen:
            seen[nume]['qty']+=obiect['qty']
        else:
            seen[nume]=obiect
            cart2.append(obiect)
    cart[:]=cart2

if __name__ == "__main__":
    total()
    discount()
    removeZero()
    sortCart()
    mergeDuplicates()
    print(cart)


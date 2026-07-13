inventory = {
 'P001': {'name': 'Notebook', 'qty': 50, 'price': 3.99},
 'P002': {'name': 'Pen', 'qty': 0, 'price': 0.99},
 'P003': {'name': 'Stapler', 'qty': 12, 'price': 7.49},
 'P004': {'name': 'Tape', 'qty': 0, 'price': 1.49},
 'P005': {'name': 'Highlighter','qty': 34, 'price': 2.29},
}

def totalValue():
    total = 0
    for value in inventory.values():
        total += value['qty'] * value['price']
    print(f"\nValoarea totala a inventarului: {round(total, 2)}")
    return total

def sorty(e):
    return e['price']

def mostExpensiveInStock():
    in_stock = [value for value in inventory.values() if value['qty'] > 0]
    most_expensive = max(in_stock, key=sorty)
    print(f"\nCel mai scump produs in stoc: {most_expensive['name']} - {most_expensive['price']}")

if __name__=='__main__':
    for item ,value in inventory.items():
        if value['qty']==0:
            print(item)

    restock=[('P002', 20), ('P004', 15), ('P999', 5)]
    for product_id, qty_to_add in restock:
        if product_id in inventory:
            inventory[product_id]['qty'] += qty_to_add
        else:
            print(f"Atentie: {product_id} nu exista")
    totalValue()
    mostExpensiveInStock()

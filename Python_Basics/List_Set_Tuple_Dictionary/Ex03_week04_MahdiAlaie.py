inventory ={
    "CPU":
       {"price": 35,
         "stock": 5},
    "Ram": 
        {"price": 10, 
        "stock": 2},
    "Mouse": 
        {"price": 5, 
         "stock": 10}, 
    "Hard": 
        {"price": 12, 
        "stock": 0} 
     }
orders = ["CPU", "Ram", "Ram", "Ram", "Hard", "Mouse","Mouse"]
PurchasedItems=[]
FaildItems={

}
CusBudjet=100

for i in orders:

    if CusBudjet >= inventory[i]["price"]:
        if inventory[i]["stock"]> 0:
            PurchasedItems.append(i)
            inventory[i]["stock"] -= 1
            CusBudjet -= inventory[i]["price"]
        else:
            FaildItems[i]={"reason":"there is not in inventory"}
    else:
        FaildItems[i]={"reason":"your money is not enough"}

for i , s in inventory.items():
    print(f"{i} stock:{s["stock"]}")

print(f"{CusBudjet} left form your money")
print(f"you purchased {PurchasedItems} succesfully")
print(f"you could not buy {FaildItems}")



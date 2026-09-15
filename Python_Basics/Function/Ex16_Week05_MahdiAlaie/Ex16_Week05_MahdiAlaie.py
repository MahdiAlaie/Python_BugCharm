def CheckinDict (dict):
    if "status" in dict.keys()== True:
        return "YES"
    else:
        return "NO"
    
inventory={
    "hard":{
        "price":2000,
        "stock":4,
        "garanted":True
    },
    "ram":{
        "price":5000,
        "stock":6,
        "garanted":True
    },
    "cpu":{
        "price":9000,
        "stock":3,
        "garanted":True
    }
}
check=CheckinDict(inventory)
print(check)
def Prouductcounter(dict,stock):
    SumStock=0
    for i in dict:
        SumStock+= dict[i][stock]
    print(SumStock)

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
Prouductcounter(inventory,"stock")
BuyList=[
    {"berenj": 3000000},{"roghan":500000},{"ton":240000},{"pnair":50000}
]

def SumBuy (list):
    sum=0
    for i in list:
        for x in i:
            sum += i[x]
    if sum > 1000000:
        sum = sum * 0.9
    print(sum)

SumBuy(BuyList)
import numpy as np
from matplotlib import pyplot as plt




class seller:

    def __init__(self):
        self.price = np.random.randint(5000,10000)
        self.customer_count = 0
        self.total_customer_count = 0

    def manage_price(self):
        if self.customer_count > 10:
            self.price = self.price * 1.1
        
        elif self.customer_count < 5:
            self.price =  max(self.price * 0.95,5000)
        
        self.customer_count = 0



class customer:
    def __init__(self):
        self.budget = np.random.randint(5000,10000)

    def purchase(self,sellers):
        selected_seller = None
        lowest_price = None
        
        for seller in sellers:
            
            if self.budget >= seller.price:
                
                if lowest_price is None:
                    lowest_price = seller.price
                    selected_seller = seller
                
                elif seller.price < lowest_price:
                    selected_seller = seller
                    lowest_price = seller.price

        if selected_seller is not None:
            selected_seller.customer_count += 1
            selected_seller.total_customer_count += 1

            return True
            
        return False


run_steps = 365


sellers_list = [seller()]

price_history = [[]]
seller_start_step =[0]

customer_count = 0

customers = []
for i in range(10):
    customers.append(customer())
   
for step in range(run_steps):
    
    for c in customers:
        if c.purchase(sellers_list):   
            customer_count += 1
            
  
    if step % 10 == 0:
        if customer_count > 15:
            for i in range(3):
                customers.append(customer())


    for s in sellers_list:

        if step % 15 == 0:
            s.manage_price()


    if customer_count > 200 and len(sellers_list)<5:
        sellers_list.append(seller())
        price_history.append([])
        seller_start_step.append(step)
        customer_count = 0

    for n in range(len(sellers_list)):
        price_history[n].append(sellers_list[n].price)

   
sellers_customer = []

for count in sellers_list:
    sellers_customer.append(count.total_customer_count)

seller_names = [f"Seller {i+1} \n ({sellers_list[i].total_customer_count})" for i in range(len(sellers_list))]


fig , axes = plt.subplots(2,1,figsize=(8,8))
   
for p in range(len(sellers_list)):
    start = seller_start_step[p]
    x = range(start, start + len(price_history[p]))
    axes[0].plot(x,price_history[p],label=f"Seller {p+1}")
   
axes[0].set_title("Price Overview")
axes[0].set_xlabel("Step")
axes[0].set_ylabel("Price")
axes[0].legend()
axes[0].grid(True)

axes[1].bar(seller_names,sellers_customer)
   
axes[1].set_title("Sellers Customer Count")
axes[1].set_xlabel("Seller")
axes[1].set_ylabel("Customer Count")
axes[1].legend()
axes[1].grid(False)

plt.tight_layout()
plt.show()



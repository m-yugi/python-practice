supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}
totalval=0
subsum=0
for key,value in supermarket.items():
    if(isinstance(value,dict)):
        for i,j in value.items():
            if(i=="quantity"):  
                subsum+=j
            else:
                subsum*=j
        totalval+=subsum
        subsum=0
print(totalval)

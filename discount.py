

def student_discount(price):

    price = price - (price*10) / 100
    return price

def additional_dicount(newprice):
    newprice = newprice - (newprice*5) / 100

    return newprice

selling_price = 100

print(additional_dicount(student_discount(selling_price)))

result = (lambda x : x*(x+5)^2)(5)
print(result)

#Considor i list which include prices of all store items

storepricelist = [100, 200, 300, 400]

#Build function to discount the price of all the product by 10%

discounted_prices = list(map(lambda x : x - (x*10) /100,storepricelist)) 

print(discounted_prices)

sale_tax = 9
shipping = 20 

def Amazon_shop_list():
    global shipping 
    shipping = 35
    television32_price = 350
    television44_price = 475
    
    final_price = (television32_price + sale_tax)+(television44_price + sale_tax) + shipping
    print(f"El precio total de la compra es de {final_price} dolares.")
    print(shipping)
    return final_price


credit_money = Amazon_shop_list()
print(f"{credit_money} dolares sumados a Su tarejeta de Credito.")
price=float(input("enter the price:"))
quality=float(input("enter the quality:")) 
Delivary_charge=float(input("enter the Delivary charge:"))
total=price*quality
if total>=2000:
    discount=total*10/100
else:
    discount=0    
final_bill=total-discount
if final_bill>=1500:
    print("the bill is greater:")
else:
    print("the bill is not greater:")
if price >0 and quality >0:
    print("valide")
else:
    print("not valide")   
if quality==1 or quality > 10:
    print("quality")    
else:
    print("no quality") 
if quality % 2==0:
    print("even")
else:
    print("odd")
final_bill+=50
final_bill-=discount
print("price",price)
print("quality",quality)
print(Delivary_charge)
print("total",total)
print(final_bill)
               


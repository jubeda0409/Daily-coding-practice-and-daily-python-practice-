products=["laptop","books","pen","shoes","cloths"]
products.append("phone")
products.append("spect")
products.remove("books")
products[2]="headphone"
products.sort()
if "laptop"in products:
    print("yes")
else:
    print("no")
print("product:",products)        

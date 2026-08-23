customer_name=input("enter the customer_name:")
balance=int(input("enter the balance:"))
withdrawal_amount=int(input("enter the withdrawal_amount:"))
PIN=int(input("enter the PIN:"))
correct_PIN=2554
if PIN==correct_PIN:
    print("pin is correct")
else:
    print("incorrect")
if withdrawal_amount > 0 and withdrawal_amount<=balance:
    balance-=withdrawal_amount 
    balance+=withdrawal_amount 
print("remaning balance:")
print("customer_name",customer_name)
print("balance",balance)
print("withdrawal_amount",withdrawal_amount)

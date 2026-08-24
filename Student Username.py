name=input("enter the name:")
name=name.strip()
character=len(name)
name=name.lower()
words=name.split()
first_letter=words[0][0]
last_letter=words[-1]
username=first_letter+"_"+last_letter
contains_digits=any(char.isdigit()for char in username)
print("username:",username)
print("character:",character)
print("words:",len(words))
print("contains digits:",contains_digits)

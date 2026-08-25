marks=[65,45,54,85,75,65,95,83,64]
maximum=max(marks)
minimum=min(marks)
total=sum(marks)
average=total/9
count=0
for marks in marks:
    if marks>average:
        count+=1
print("maxmimum:",maximum) 
print("minimum:",minimum)  
print("total:",total)     
print("average",average)
print("student above average=",count)
print("marks:",marks)

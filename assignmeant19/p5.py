str=input("enter a string:")
li=[w for w in str.split() if len(w)<5]
print(li)
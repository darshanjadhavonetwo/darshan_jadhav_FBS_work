#remove vowels string
v=input("enter a string:")
str=[ch for ch in v if ch not in "aioue"]
print("".join(str))
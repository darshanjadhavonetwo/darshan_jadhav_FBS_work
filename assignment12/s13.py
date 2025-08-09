str="12darshan3"
chr=0
dig=0
for i in str:
   if i.isalpha():
    chr+=1
   elif i.isdigit():
     dig+=1
print("letter",chr)
print("digit",dig)
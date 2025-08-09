def palindrome(n):
    num=0   
    while(num<=n):
        if str(n)==str(n)[::-1]:
            yield n
            num+=1

n=int(input("enter the number:"))
print("palindrome numbers up to ",n,"are:")
for i in palindrome(n):
    print(i,end=" ")

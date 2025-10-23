l = n%10 
same = True
while n> 0:
    x = n%10
    if x!=l:
        same = False
        break
    n = n//10
if same:
    print("Yes")
else:
    print("No")

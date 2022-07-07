#
#n: int = int(input("Enter number:"))
m: int = int(input("Enter number:"))
k: int = int(input("Enter number:"))
for i in range(101):
    if i % m == 0 and i > k:
       print(i)
        if i<=50:
            continue
        else:
            print("It's last number")

# while i % m == 0 and i > k:
#    print(i)
#    if counter != 6:
#        continue
#   break

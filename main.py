n = int(input("Enter a number: "))
length = len(str(n))

temp = n
sum = 0

while n>0:
    digit =n%10
    sum = sum + digit**length
    n=n//10

if temp == sum:
    print(temp, "is an armstrong number.")
else:
    print(temp, "is not an armstrong number.")
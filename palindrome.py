#Check number is palindrome or not

number=int(input("Enter the Number "))
temp=number

reverse=0
i=0

while i<number:
    last_num=number%10
    reverse=(reverse*10)+last_num
    number=number//10

if(reverse==temp):
    print("Your Number is a Palindrome")
else:
    print("Your Number is Not a Palindrome")
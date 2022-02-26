#Sort the list 

l1 = [3, 1, 4, 2, 5]
l1.sort()
print("List : ",l1)


#print the squares of all the number in the list 

l2 = [3, 1, 4, 2, 5]

print("Squares of all the number : ")
for i in l2:
    print(i*i)


#print all the elements in the list 
l3 = [
    (105, "d"),
    (21, "z"),
    (0, "v")
]
print("Elements in the list : ")

for x in l3:
    for y in x:
        print(y,end=" ")
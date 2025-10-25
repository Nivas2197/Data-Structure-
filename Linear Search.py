# defining varibles 
array = list(map(int,input("enter the numbers - ").split()))
key = int(input("enter the key - "))

# linear searching method 1

if key in array: 
    print("key exists")
else:
    print("it does not exist")

# linear searching method 2 

for i in range(0,len(array)):
    if array[i] == key:
        print("key exists")

#method 3 
for num in array:
    if key == num:
        print("key exists")      
#time complexity O(n)
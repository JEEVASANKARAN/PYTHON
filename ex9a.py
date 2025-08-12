n = int(input("Enter the number of elements: "))
arr = [int(input("Enter array element: ")) for _ in range(n)]

key = int(input("Enter the key element to search: "))

if key in arr:
    print("Key found...!")
else:
    print("Element not found")

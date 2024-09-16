# Program to find HCF(GCD)
# Enter two numbers
numberLargest = int(input("Enter largest number:"))
numberSmallest = int(input("Enter smallest number:"))

# Using Eucliden algorithms
while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print("HCF is:", numberLargest)     

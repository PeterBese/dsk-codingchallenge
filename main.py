count = int(input("How many number would you like to summarize?"))
sum = 0 
for i in range (count):
  number = int(input(f"Enter number {i+1}: "))
  sum += number 
print(f"The sum of the numbers is: {sum}")
##### STUDENT ID: 10961661 #####

print("Enter any number greater than 2")


user1 = int(input("Enter your number : "))
sum = 0


if user1 <= 2:
    print("Sum of all prime numbers less than", user1, ":", 0)

#iterate through to find prime numbers
for num in range(2, user1 - 1):
    i = 2
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    #If the number is prime then add it.
    if i != num:
        sum += num
    
print("Sum of all prime numbers less than", user1, ":", sum)
import random

#Create an empty list to store the ticket numbers
ticket_num = []

#Generate 5 random numbers between 1 and 69 which will be the ticket numbers
for num in range(1,6):
    ticket_num.append(random.randint(1,69))

#Generate 1 random number between 1 and 26 which will be the powerball number
powerball_num = random.randint(1,26)
print(f"ticket number:{ticket_num}\npowerball number:{powerball_num}")

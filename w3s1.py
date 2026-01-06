# # get number from user
# n = int (input("enter a number:"))
# # print the 5 multiplication table
# for i in range (1, 11):
#     # print(n, "x", i, "=", n * i)
#     print(f"{n} X {i} = {n*i}")

# sum = 0
# n = int (input("enter a number:"))
# total = 0
# for i in range (1, n + 1):
#     total = total + i
# print ("sum from 1 to", n, "is", total)

# #ask user for a word
# word = input ("enter a word:")
# # ask user for a number
# n= int (input ("enter a number:"))
# for i in range (1, n+1):
#     print (f"{i} : {word}")

# x = int(input("enter a number:"))
# for i in range (1, 11):
#     print (f"{i} * {x} = {i*x}")

#  # ask user for a sentence
# sentence = input("enter a sentence")
# count = 0
# for i in sentence:
#     if i != " ":
#         count = count + 1
# print (f"the character count is {count}")

# # Ask how many marks will be entered
# n = int(input("How many marks will you enter? "))
#
# # Read the first mark and assume it is the maximum
# max_mark = int(input("Enter mark 1: "))
#
# # Use a for loop to read remaining marks
# for i in range(2, n + 1):
#     mark = int(input(f"Enter mark {i}: "))
#     if mark > max_mark:
#         max_mark = mark
#
# # Print the highest mark
# print("The highest mark is:", max_mark)

# n = int(input("How many marks will you enter? "))
#
# passed_count = 0
#
# for i in range(n):
#     mark = int(input("Enter mark: "))
#     if mark >= 40:
#         print(mark)
#         passed_count += 1
#
# print("Number of students who passed:", passed_count)

# word = input("Enter a word: ")
#
# reversed_word = ""
#
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
#
# print("Reversed word:", reversed_word)

# # Ask how many names to enter
# n = int(input("How many names do you want to enter? "))
# # Store names in a list
# names = []
# for i in range(n):
#     name = input(f"Enter name {i + 1}: ")
#     names.append(name)
# # Ask for the letter to search
# letter = input("Enter a letter to search for: ").lower()
# # Count how many names contain the letter (case-insensitive)
# count = 0
# for name in names:
#     if letter in name.lower():
#         count += 1
# # Print the result
# print(f"Number of names containing '{letter}': {count}")


# # Ask for number of students
# n = int(input("Enter the number of students: "))
# total_marks = 0
# distinction_count = 0
# # Input marks and calculate statistics
# for i in range(n):
#     mark = int(input(f"Enter mark for student {i + 1}: "))
#     total_marks += mark
#     if mark >= 70:
#         distinction_count += 1
# # Calculate average
# average = total_marks / n
# # Print results
# print("Total marks:", total_marks)
# print("Average mark:", average)
# print("Number of distinctions:", distinction_count)
# # Ask how many numbers to enter
# count = int(input("How many numbers do you want to enter? "))
# numbers = []
# # Input positive integers
# for i in range(count):
#     num = int(input(f"Enter positive integer #{i + 1}: "))
#     numbers.append(num)
# # Print the bar chart
# for num in numbers:
#     print("*" * num)

# Ask how many numbers to enter
count = int(input("How many numbers do you want to enter? "))

numbers = []

# Input positive integers
for i in range(count):
    num = int(input(f"Enter positive integer #{i + 1}: "))
    numbers.append(num)

# Print the bar chart
for num in numbers:
    print("*" * num)



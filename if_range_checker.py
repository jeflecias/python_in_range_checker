# PLD
# ask the user to input a number from 1-50, and keep asking
# if the user's input is invalid, display how many numbers are in the following ranges
# 1-10, 11-20, 21-30, 31-40, 41-50

range_10_counter = 0
range_20_counter = 0
range_30_counter = 0
range_40_counter = 0
range_50_counter = 0

while True:
    try:
        num_input = int(input("Please enter a number from 1-50. "))
        if num_input >= 1 and num_input <= 10:
            range_10_counter += 1
        elif num_input >= 11 and num_input <= 20:
            range_20_counter += 1
        elif num_input >= 21 and num_input <= 30:
            range_30_counter += 1
        elif num_input >= 31 and num_input <= 40:
            range_40_counter += 1
        elif num_input >= 41 and num_input <= 50:
            range_50_counter += 1
        else:
            raise
        break
    except:
        print("Invalid input! Now displaying numbers in the following ranges. ")
        print(f"In the range of 1-10, there are {range_10_counter} numbers.")
        print(f"In the range of 11-20, there are {range_20_counter} numbers.")
        print(f"In the range of 21-30, there are {range_30_counter} numbers.")
        print(f"In the range of 31-40, there are {range_40_counter} numbers.")
        print(f"In the range of 41-50, there are {range_50_counter} numbers.")
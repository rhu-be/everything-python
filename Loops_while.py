# while loop in python executes as long as a condition is true.
# It is suitable when a set number of iterations is not predetermined.
# Iteration - in programming repeatedly executing a code block until a certain condition is met.
'''
Elements of a proper loop
1. Initialization- starting value.
2. condition - decides if the loop runs(True or false).
3. Loop body - code that runs each iteration.
4. State change (Update) - changes a value affecting the condition.
5. Exit strategy - (optional) break | return.
'''
#
'''
num = 1
while num < 10:
    print(num)
    num += 1
'''

#01

attempts = 2
max_attempts = 3
winning_num = 2
while attempts < max_attempts:
    num = int(input("what is your number: "))
    print(f"I am number {num}.")
    if num > 5:
         print("Try again !!!")

    if num == winning_num:
        print('BINGO!!!')
        break

    #if num == winning_num:
        print('BINGO!!!')
        won = True
        break

    #if not won:
        print("You are not eligible to play, wait for the next round.")

    else:
        print("Not a bingo number.")
        attempts += 1  # attempts = attempts + 1

else: #use while...else when you trust your break, otherwise use a variable flag.
    print("You are not eligible to play, wait for the next round.")


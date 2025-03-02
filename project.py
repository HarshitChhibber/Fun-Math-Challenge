import random
from math import expm1
import time

Operators = ["+", "-", "*"]
Min_Operand = 3
Max_Operand = 15
Total_Problems = 10

def Generate_Problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

expr, answer = Generate_Problem()

wrong = 0
input("Press Enter to Start!")
print("---------------------------")

start_time = time.time()

for i in range(Total_Problems):
    expr, answer = Generate_Problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":  "  + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
time_taken = round(end_time - start_time, 2)

print("-----------------------------")
print("Nice Work! You finished in", time_taken, "seconds!")
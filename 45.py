'''What is an Algorithm?
An algorithm is a finite sequence of well-defined steps used to solve a particular problem and produce the required output.
How an algorithm works
Takes input — accepts the required data.
Processes the input — performs a sequence of logical steps.
Produces output — gives the required result.
Example: Algorithm to add two numbers
Step 1: Start
Step 2: Read A and B
Step 3: Calculate SUM = A + B
Step 4: Display SUM
Step 5: Stop


'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

print("Largest =", largest)

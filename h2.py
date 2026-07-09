# Program starts from here
if __name__ == '__main__':

    # Take input from the user and convert it to an integer
    n = int(input().strip())

    # Check if the number is odd
    if n % 2 != 0:
        print("Weird")

    # Check if the number is even and between 2 and 5
    elif 2 <= n <= 5:
        print("Not Weird")

    # Check if the number is even and between 6 and 20
    elif 6 <= n <= 20:
        print("Weird")

    # If the number is even and greater than 20
    else:
        print("Not Weird")

def fizzbuzz(first, second):
    """
    Prints the numbers from 'first' to 'second' (inclusive).
    Add "Fizz" for multiples of 3, "Buzz" for multiples of 5.

    Args:
    first (int): The starting integer of the range. (1-100)
    second (int): The ending integer of the range. (1-100)
    """

    if not (1 <= first <= 100 and 1 <= second <= 100):
        raise ValueError("Both numbers must be between 1 and 100 inclusive.")
    
    if first > second:
        raise ValueError("The first number must be less than or equal to the second number.")
    
    for i in range(first, second + 1):
        output = str(i)

        if i % 3 == 0:
            output += " Fizz"
        if i % 5 == 0:
            output += " Buzz"
        print(output)

def main():
    print("Please enter two numbers between 1 and 100: ")

    try:
        first = int(input("First number: "))
        second = int(input("Second number: "))
        fizzbuzz(first, second)
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")

if __name__ == "__main__":
    main()
        
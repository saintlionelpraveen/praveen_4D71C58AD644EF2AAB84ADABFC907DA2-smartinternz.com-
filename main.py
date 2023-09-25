def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                raise ValueError("The number must be non-negative.")
            break
        except ValueError as e:
            print("Invalid input:", e)
    
    print("The factorial of", num, "is", factorial(num))

if __name__ == "__main__":
    main()

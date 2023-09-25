def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    while True:
        try:
            year = int(input("Enter a year: "))
            if year < 0:
                raise ValueError("The year must be non-negative.")
            break
        except ValueError as e:
            print("Invalid input:", e)
    
    if is_leap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()

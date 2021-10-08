import sys

def main():
    start = input("Enter the start date (dd/mm/yyyy): ")
    start_date = start.split("/")
    start_jdn = jdn(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    end = input ("Enter the end date (dd/mm/yyyy): ")
    end_date = end.split("/")
    end_jdn = jdn(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    result = end_jdn - start_jdn
    if result <= 0:
        result *= -1
    else:
        result -= 1
    print(str(result)+" days")

def jdn(d,m,y):
    return (1461 * (y + 4800 + (m - 14) // 12))//4 + (367 * (m - 2 - 12 * ((m - 14) // 12)))//12 - (3 * ((y + 4900 + (m - 14) // 12) // 100)) // 4 + d - 32075

if __name__ == "__main__":
    main()
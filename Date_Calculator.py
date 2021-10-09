import sys

#Date Interval Calculator:
#Calculate the interval between two given dates (between 01-01-1901 and 31-12-2999)
#Input: Two valid dates (between 01-01-1901 and 31-12-2999)
#Output: #No. of days between the two dates

def main():

    #Transform start date into Julian day
    while True:
        start = input("Enter the start date (dd/mm/yyyy): ")
        start_date = start.split("/")
        if len(start_date) != 3:
            print("Please enter a valid date between 01-01-1901 and 31-12-2999")
            continue
        else:
            result = valid_date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            if not result:
                print("Please enter a valid date between 01-01-1901 and 31-12-2999")
                continue
            else:
                start_jdn = jdn(int(start_date[0]), int(start_date[1]), int(start_date[2]))
                break

    #Transform end date into Julian day
    while True:
        end = input ("Enter the end date (dd/mm/yyyy): ")
        end_date = end.split("/")
        if len(end_date) != 3:
            print("Please enter a valid date between 01-01-1901 and 31-12-2999")
            continue
        else:
            result = valid_date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
            if not result:
                print("Please enter a valid date between 01-01-1901 and 31-12-2999")
                continue
            else:
                end_jdn = jdn(int(end_date[0]), int(end_date[1]), int(end_date[2]))
                break

    #Calculate interval and print result
    result = end_jdn - start_jdn
    if result <= 0:
        result *= -1
    else:
        result -= 1
    print(str(result)+" days")

#Transform Gregorian day format into Julian day format
def jdn(d,m,y):
    return (1461 * (y + 4800 + (m - 14) // 12))//4 + (367 * (m - 2 - 12 * ((m - 14) // 12)))//12 - (3 * ((y + 4900 + (m - 14) // 12) // 100)) // 4 + d - 32075

#Check if certain date is valid
def valid_date(d,m,y):
    if y < 1901 or y > 2999:
        return False
    elif m < 1 or m > 12:
        return False
    elif m == 2 and leap_year(y):
        if d < 1 or d > 29:
            return False
    elif m == 2 and not leap_year(y):
        if d < 1 or d > 28:
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d < 1 or d > 30:
            return False
    else:
        if d < 1 or d > 31:
            return False 
    return True

#Check if year is leap year
def leap_year(year):
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
    

if __name__ == "__main__":
    main()
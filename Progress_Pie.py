import sys
import math

#Progress Pie:
#Given a 2-d graph from (0,0) to (100,100) with a circle centered at (50,50) with 50 pixels radius
#Determine if a certain point is within the progress pie after certain %
#Input: T (Amount of iterations)
#Input: P X Y (Progress %, X Coordinate, Y Coordinate)
#Output: White (Not in the Progress Pie)
#Ouput: Black (In the Progress Pie)

def main():

    total = input("Enter the total number of queries: ")
    try:
        total = int(total)
    except ValueError:
        print("Please enter a valid number (1-1000) of queries.")
        sys.exit()
    if total < 1 or total > 1000:
        print("Please enter a valid number (1-1000) of queries.")
        sys.exit()

    
    i = 1
    while (i <= total):
        curr = input("Query #"+str(i)+": ")
        coordinates = curr.split(" ")
        if (len(coordinates) != 3):
            print("Enter query in the format of 3 integers between 0-100. e.g. 0 55 25")
            continue
        try:
            p = int(coordinates[0])
            x = int(coordinates[1])
            y = int(coordinates[2])
            if (p < 0 or p > 100 or x < 0 or x > 100 or y < 0 or y > 100):
                print("Enter query in the format of 3 integers between 0-100. e.g. 0 55 25")
                continue
        except ValueError:
            print("Enter query in the format of 3 integers between 0-100. e.g. 0 55 25")
            continue

        #if distance to center is greater than radius
        if distance(x,y) > 50:
            print("Case #"+str(i)+": white")

        else:
            result = angle(x,y)
            progress_angle = p*360/100
            if (result < progress_angle):
                print("Case #"+str(i)+": black")
            else:
                print("Case #"+str(i)+": white")

        i += 1

#Calculate the Cartesian Distance between two coordinates
def distance(x,y):
    return math.sqrt(((x - 50) ** 2) + ((y - 50) ** 2))

#Calculate the angle between a given point and the center of the circle (50,50)
def angle(x,y):
    distance_x = x-50
    distance_y = y-50
    beta = math.acos(abs(distance_x) / math.sqrt((distance_x ** 2) + (distance_y ** 2))) * 180 / math.pi
    if (distance_x > 0):
        if (distance_y < 0):
            return beta + 90
        else:
            return abs(beta-90)
    else:
        if (distance_y < 0):
            return abs(beta - 90) + 180
        else:
            return beta + 270

if __name__ == "__main__":
    main()
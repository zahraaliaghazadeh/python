def main():
     
    import math
    x1 = float(input("Enter the x coordinate of the first point: "))
    y1 = float(input("Enter the y coordinate of the first point: "))
    x2 = float(input("Enter the x coordinate of the second point: "))
    y2 = float(input("Enter the y coordinate of the second point: "))
    distance = math.sqrt(float((x1-x2)**2)+(y1-y2)**2)
    print("The Euclidean distance will be {}".format(round(distance, 3)))


main() 

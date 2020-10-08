def main():
     
    import math
    angle = float(input("Enter an angle: "))
    cos = math.cos(math.radians(angle))
    sin = math.sin(math.radians(angle))
   
    print("The Cos is: {}".format(round(cos, 5)))
    print("The Sin is: {}".format(round(sin, 5)))


main() 
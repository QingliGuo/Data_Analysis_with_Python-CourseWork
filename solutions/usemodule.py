#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
#    triangle.hypothenuse()
    print ("Area of right-angled triangle with side1 = 3, side2 = 4 is: ",triangle.area (3,4))
    print ("Hypothenuse of right-angled triangle with side1 = 3, side2 = 4 is: ", triangle.hypothenuse(3,4))
if __name__ == "__main__":
    main()

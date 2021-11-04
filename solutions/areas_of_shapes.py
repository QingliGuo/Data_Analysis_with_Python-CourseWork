#!/usr/bin/env python3

import math

def triangle (base, height):
    return base * height / 2

def rectangle (width, height):
    return width * height

def circle (radius):
    return radius ** 2 * math.pi

def input_taker_checker (shape,parameter):    
    "Asking for parameter(s) for the the given shape; It automatically check if the input is usable for calculation or not; It will keep asking to input a correct format value to carry on"
    while True:
        x = input (f"Give {parameter} of the {shape}: ")

        if x.isdigit():
            return float (x)
            break
        else:
            print (f"\n** Anteeksi! **\n** Please enter a number for the {parameter} of your {shape}! **\n")

def main():
    "Compute areas of three shapes, triangles, rectangles and circles; Watch out!! This is an endless loop..."

    while True:
        shape = input ("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = input_taker_checker (shape, "base")
            height = input_taker_checker (shape, "height")
            print (f"The area is {triangle(base, height):.6f}")

        elif shape == "rectangle":
            width = input_taker_checker (shape, "width")
            height = input_taker_checker (shape, "height")
            print (f"The area is {rectangle(width, height):.6f}")

        elif shape == "circle":
            radius = input_taker_checker (shape, "radius")
            print (f"The area is {circle(radius):.6f}")
        elif shape == "":
            break
        else:
            print ("Unknown shape!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Adwok Adiebo

# Date: Feb 24, 2025

# This program calculates and displays the area and the perimeter of the rectangle

# The rectangle has a length of 12cm and width of 6cm


def main():
    # The rectangle here has a length of 12 cm and width of 6cm which are the dimensions of the rectangle.
    print("A rectangle has  length of 12cm and width of 6cm.")
    # The code below solves our Area for the rectangle, we must multiply the 12cm with 6 cm  in this case it is (12*6)cm^2
    print("The Area of this rectangle is: {}cm^2".format(12 * 6))
    # The code below solves our perimeter for the rectangle, we must find the sum of all sides in this case it is (L+L+W+W)cm
    print("The Perimeter of this rectangle is: {}cm".format((2 * 12) + (2 * 6)))


if __name__ == "__main__":
    main()

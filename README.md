# Regular Polygon Drawer

This is a Python program that uses the `turtle` module to draw regular polygons with a variable number of sides.

## Usage

1. Run the program.
2. Enter the number of sides for the polygon you want to draw (must be between 3 and 14).
3. Watch as the turtle draws the polygon in a random color.

## How it Works

The program first creates a `Turtle` object and sets its shape and color. Then, for each polygon to be drawn, it calculates the internal angle between the sides using the formula `(sides - 2) * 180 / sides`. It then iterates over each side of the polygon, drawing it using the `forward()` and `left()` methods of the `Turtle` object. The turtle changes color randomly for each polygon drawn.

## Requirements

- Python 3.x
- `turtle` module
- `colour` module

## Installation

1. Clone the repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install the required modules by running the following command in your terminal: `pip install -r requirements.txt`.
4. Run the program using `python polygon_drawer.py`.


# General Description of the Solution
This project is a console-based calculator designed to compute the area and perimeter of various geometric shapes such as circles, squares, and triangles.
The program allows users to input the name of the shape, select the function (to calculate either the area or perimeter), and provide the necessary
parameters (e.g., radius for a circle, side length for a square, or three sides for a triangle).
The program utilizes built-in mathematical functions to perform the calculations and displays the result to the user.

# Key functionalities of the program include:

1. User input through the console.
2. Validation of input data (shape name, function, and dimensions).
3. Utilization of mathematical formulas to compute the area and perimeter.
4. Output of results to the console.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Description of Each Function with Examples

1. `calc(fig, func, size)`
This function performs the core calculation of either the area or the perimeter for the shape selected by the user.

Arguments:

fig (str): The name of the figure, e.g., "circle", "square", "triangle".
func (str): The type of calculation – "area" or "perimeter".
size (list): A list of parameters for the shape, such as radius, side length, or the lengths of all sides.
Example of usage:

>>> calc('circle', 'area', [5])
area of circle is 78.54
>>> calc('triangle', 'perimeter', [3, 4, 5])
perimeter of triangle is 12

2. `area(r)`
This function calculates the area of a circle based on the given radius.

Arguments:

r (float): The radius of the circle.
Example of usage:

>>> area(5)
78.54

3. `perimeter(r)`
This function calculates the perimeter (circumference) of a circle based on the given radius.

Arguments:

r (float): The radius of the circle.
Example of usage:

>>> perimeter(5)
31.42

4. `area(a)`
This function calculates the area of a square based on the given side length.

Arguments:

a (float): The length of the square's side.
Example of usage:

>>> area(4)
16

5. `perimeter(a)`
This function calculates the perimeter of a square based on the given side length.

Arguments:

a (float): The length of the square's side.
Example of usage:

>>> perimeter(4)
16

6. `area(a, b, c)`
This function calculates the semi-perimeter of a triangle, which is used to further compute the area using Heron's formula.

Arguments:

a (float): The length of the first side of the triangle.
b (float): The length of the second side of the triangle.
c (float): The length of the third side of the triangle.
Example of usage:

>>> area(3, 4, 5)
6.0

7. `perimeter(a, b, c)`
This function calculates the perimeter of a triangle based on the three given sides.

Arguments:

a (float): The length of the first side of the triangle.
b (float): The length of the second side of the triangle.
c (float): The length of the third side of the triangle.
Example of usage:

>>> perimeter(3, 4, 5)
12

# History project commits

- Hash: b5b0fae — L-04: Update docs for calculate.py
- Hash: d76db2a — L-04: Add calculate.py
- Hash: 51c40eb — L-04: Doc updated for triangle
- Hash: d080c78 — L-04: Triangle added
- Hash: d078c8d — L-03: Docs added
- Hash: 8ba9aeb — L-03: Circle and square added

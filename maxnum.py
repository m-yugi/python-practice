import math 
def circle(r): 
 area = math.pi*r*r 
 return area 
def rectangle(l,b): 
 area = l*b 
 return area 
def square(side): 
 area = side*side 
 return area 
def triangle(a,b,c): 
 s = (a+b+c)/2 
 area = math.sqrt(s*(s-a)*(s-b)*(s-c)) 
 return area 
print("1. Circle area\n2. Rectangle area\n3. Square area\n4. Triangle area") 
n = int(input("Enter your choice: ")) 
if n==1: 
 radius = int(input("Enter radius of circle: ")) 
 area = circle(radius) 
 print("Area of circle = ",area) 
elif n==2: 
 l = int(input("Enter lenght of rectangle: ")) 
 b = int(input("Enter breadth of rectangle: ")) 
 area = rectangle(l,b) 
 print("Area of rectangle = ",area) 
elif n==3: 
 side = int(input("Enter side of square: ")) 
 area = square(side) 
 print("Area of square = ",area) 
elif n==4: 
 a = int(input("Enter first side of triangle: ")) 
 b = int(input("Enter second side of triangle: ")) 
 c = int(input("Enter third side of triangle: ")) 
 area = triangle(a,b,c) 
 print("Area of triangle = ",area) 
else: 
 print("Invalid choice")
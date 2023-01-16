'''
@author: Armend Veseli.
'''
from math import nan, sqrt
from math import pi
from math import exp
from math import log2
from math import sin
from math import cos
from math import atan2


#Get the rise over run of a line.
def linear_slope(m: float, x: float, b: float) -> float:
    return m * x + b


#Interpolate a linear function.
def linear_interpol(m: float, x1: float, x2: float, b: float) -> float:
    return (linear_slope(m, x1, b) + linear_slope(m, x2, b)) / 2.0


#Get the n-th root of a number.
def nth_root_of_x(n: float, x: float) -> float:
    return x ** (1.0 / n)


#Get the b-th base logarithm of a number.
def log_base_b_of_a(b: float, a: float) -> float:
	return log2(a) / log2(b)


#Get the median of a set.
def avg(iterator):
    return sum(iterator) / len(iterator)


#Get the standard deviation of a set.
def std_dev(iterator, population = False):
    average = avg(iterator)
    result = 0

    for i in range(len(iterator)):
        result += (iterator[i] - average) * (iterator[i] - average)

    if population:
        return sqrt(result / (len(iterator)))

    return sqrt(result / (len(iterator)-1))


#Get the normal distribution of a number.
def std_norm_distrib(x):
    return 1.0 / sqrt(2.0 * pi) * exp(-.5 * x * x)


#Get the normal distribution of a number with a mean and a standard deviation.
def general_norm_distrib(x, micro, sigma):
    sigma *= sigma

    return 1.0 / sigma * std_norm_distrib((x - micro) / sigma)


#Get the area of a triangle with a base and a height.
def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height


#Get the perimeter of a triangle using three sides.
def triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3


#Get the perimeter of a triangle using three sides, but in a way that makes sure it's a valid triangle.
def triangle_perimeter_valid(side1: float, side2: float, side3: float) -> float:
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return side1 + side2 + side3

    return 0


#Get the value under the square root in the quadratic formula.
def quadratic_discriminant(a: float, b: float, c: float) -> float:
    return b * b - 4.0 * a * c


#Get the quadratic roots.
def quadratic_roots(a: float, b: float, c: float) -> tuple:
    discriminant = quadratic_discriminant(a, b, c)

    if discriminant < 0.0:
        return None

    if discriminant == 0.0:
        return (-b + sqrt(discriminant)) / (2.0 * a)

    return ((-b + sqrt(discriminant)) / (2.0 * a), (-b - sqrt(discriminant)) / (2.0 * a))


#Get the volume of a cube
def cube_volume(side: float) -> float:
    return side * side * side


#Get the surface area of a cube
def cube_surface_area(side: float) -> float:
    return 6 * side * side


#Get the diagonal length of a cube from two opposite corners.
def cube_diagonal(side: float) -> float:
    return sqrt(side * side + side * side + side * side)


#Get the circumfrence of a circle.
def circle_circumfrence(radius: float) -> float:
    return 2.0 * pi * radius


#Get the area of a circle.
def circle_area(radius: float) -> float:
    return pi * radius * radius


#Get the surface area of a sphere.
def sphere_surface_area(radius: float) -> float:
    return 4.0 * pi * radius * radius


#Get the volume of a sphere.
def sphere_volume(radius: float) -> float:
    return 4.0 / 3.0 * pi * radius * radius * radius


#Get the volume of a cylinder.
def cylinder_volume(radius: float, height: float) -> float:
    return circle_area(radius) * height


#Get the sinusiodal function.
def sin_wave(x: float, amplitude: float, frequency: float, phase: float, vertical_shift: float) -> float:
    return amplitude * sin(frequency * x + phase) + vertical_shift


#Get the cosinusiodal function.
def cos_wave(x: float, amplitude: float, frequency: float, phase: float, vertical_shift: float) -> float:
    return amplitude * cos(frequency * x + phase) + vertical_shift


#Get the growth rate of a population.
def population_growth_rate(initial_population: float, final_population: float, time: float) -> float:
    return (final_population - initial_population) / time


#Get the angle between two lines points.
def get_angle_between(x1, y1, x2, y2):
    return atan2(y2 - y1, x2 - x1)


#Get the arc length of a semi-circle.
def get_arc_length(radius, angle):
    return radius * angle


#Get the weighted average of a set of numbers.
def weighted_average(values, weights) -> float:
    return sum([values[i] * weights[i] for i in range(len(values))]) / sum(weights)


#Get the area of any triangle using three side lengths.
def heron_triangle_area(a, b, c):
    s = (a + b + c) / 2.0
    return sqrt(s * (s - a) * (s - b) * (s - c))


#Get the derivative of a polynomial.
def polynomial_derivative(coefficients, bases, powers):
    if len(coefficients) == len(bases) == len(powers):
        terms_sum = 0
        for i in range(len(coefficients)):
            terms_sum += powers[i] * coefficients[i] * (bases[i] ** (powers[i] - 1))
    else:
        return nan


#Get the antiderivative of a polynomial.
def polynomial_integral(coefficients, bases, powers):
    if len(coefficients) == len(bases) == len(powers):
        terms_sum = 0
        for i in range(len(coefficients)):
            terms_sum += powers[i] * coefficients[i] * (bases[i] ** (powers[i] + 1)) / (powers[i] + 1)
    else:
        return nan
import math


def area_circle(radius=None, diameter=None):
    """
    Aah.. tough to remember me :
    Pie Are Squared... But they are round
    Enter the radius, diameter, circumference or area of a Circle to find the other three. The calculations are
    done "live":
    --------------
    if radius is given
    A = π r2
    π = 3.14159...

    if diameter is given
    A = (π/4) * D2
    --------------
    :param diameter:
    :param radius:
    :return: float
    """
    if radius is not None:
        area_by_radius = math.pi * (radius * radius)
        return area_by_radius
    if diameter is not None:
        area_by_diameter = (math.pi / 4) * (diameter * diameter)
        return area_by_diameter
    return None


result = area_circle(diameter=2.4)
print(result)

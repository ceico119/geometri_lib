import math


def area(r):
    """
    Вычисляет площадь круга на основе его радиуса.
	
	Параметры:
		    r (float): радиус круга.
	Возвращаемое значение:
		    float: площадь круга, вычисляемая по формуле math.pi * r * r.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга на основе его радиуса.

	Параметры:
		    r (float): радиус круга.
        Возвращаемое значение:
		    float: периметр круга, вычисляемый по формуле 2 * math.pi * r.
    """
    return 2 * math.pi * r

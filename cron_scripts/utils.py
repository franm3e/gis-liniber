import random
from shapely.geometry import Point


def logger(type, message, error=None, exception=None):
    model = '[{level}]: {message}'
    if type == 'l':
        print(model.format(level='LOG', message=message))
    elif type == 'e':
        print(model.format(level='ERROR', message='Causa: {0} - Error: {1} - Exception: {2}'.format(message, error, exception)))
    else:
        logger('e', 'Tipo ({0}) no válido para mostrar el mensaje {1}'.format(type, message))


def get_random_point_in_polygon(poly):
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if poly.contains(p):
            return p

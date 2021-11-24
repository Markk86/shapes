import sys
import os
from math import pi
import yaml


class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def calculate_area(self):
        return pi * self._radius ** 2

    @property
    def radius(self):  # Public access for_radius: read only
        return self._radius

    def __call__(self):
        return "I am a circle"

    def __str__(self):
        string = yaml.dump({
            'circle': {
                'radius': self._radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        })
        return string

    @classmethod
    def from_yaml(cls, string):
        """create a circle from YAML string"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj


class Quad:
    def __init__(self, width, height, fill='red', stroke='black'):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke


class Canvas:
    def __init__(self, width, height, bg='orange'):
        self._width = width
        self._height = height
        self._bg = bg


def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")
    #print(f"area = {circle.area}")
    print(circle())
    circle2 = Circle(8.0)

    my_dict = {
        'key': {
            'inside_dict': [5, 6, 7, 8]
        }
    }
    my_yaml = yaml.dump(my_dict)
    print(my_yaml)

    print(circle)

    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red"""
    my_circle = Circle.from_yaml(yaml_circle)

    return 0


if __name__ == "__main__":
    sys.exit(main())

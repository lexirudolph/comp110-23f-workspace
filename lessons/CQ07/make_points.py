"""Testing methods for correctness."""

__author__ = "730416818"


from lessons.CQ07.point import Point

my_point: Point = Point()

my_point = Point(10.0, 10.0)

another_point = my_point.scale_by(2)
one_more_point = my_point.scale(3)
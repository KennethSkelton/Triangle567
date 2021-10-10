# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_scalene_traingles_b(self):
        self.assertEqual(classify_triangle(27, 43, 59), 'Scalene', '27,43,59 is Scalene triangle')

    def test_isoceles_triangles_a(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isoceles', '2,2,3 is Isoceles triangle')

    def test_isoceles_triangles_b(self):
        self.assertEqual(classify_triangle(2, 3, 2), 'Isoceles', '2,3,2 is Isoceles triangle')

    def test_not_a_triangle_a(self):
        self.assertEqual(classify_triangle(1, 1, 10), 'NotATriangle', '1,1,10 is NotATraingle')

    def test_not_a_triangle_b(self):
        self.assertEqual(classify_triangle(10, 1, 1), 'NotATriangle', '10,1,1 is NotATraingle')

    def test_not_a_triangle_c(self):
        self.assertEqual(classify_triangle(1, 10, 1), 'NotATriangle', '1,10,1 is NotATraingle')

    def test_invalid_input_a(self):
        self.assertEqual(classify_triangle(-1, -2, -3), 'InvalidInput', '-1,-2,-2 is Invalid Input')

    def test_invalid_input_b(self):
        self.assertEqual(classify_triangle(201, 202, 203), 'InvalidInput', '201,202,203 is Invalid Input')

    def test_invalid_input_c(self):
        self.assertEqual(classify_triangle(4.5, 1.1, 7.8), 'InvalidInput', '4.5,1.1,7.8 is Invalid Input')

    def test_invalid_input_d(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 is Invalid Input')

    def test_invalid_input_e(self):
        self.assertEqual(classify_triangle(1, 0, 0), 'InvalidInput', '1,0,0 is Invalid Input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

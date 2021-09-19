# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTrainglesB(self):
        self.assertEqual(classifyTriangle(27,43,59),'Scalene','27,43,59 is Scalene triangle')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 is Isoceles triangle')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 is Isoceles triangle')

    def testNotATriangle1A(self):
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1,1,10 is NotATraingle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','10,1,1 is NotATraingle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1,10,1),'NotATriangle','1,10,1 is NotATraingle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1,-2,-3),'InvalidInput','-1,-2,-2 is Invalid Input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,202,203),'InvalidInput','201,202,203 is Invalid Input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(4.5,1.1,7.8),'InvalidInput','4.5,1.1,7.8 is Invalid Input')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is Invalid Input')
    
    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(1,0,0),'InvalidInput','1,0,0 is Invalid Input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


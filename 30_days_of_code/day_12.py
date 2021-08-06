import time
import math
import os
import random
import re
import sys


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.set_scores(scores)

    def set_scores(self, value):
        self._scores = value

    def get_scores(self):
        return self._scores

    def calculate(self):
        result = 0
        for elem in self.get_scores():
            result += elem
        result = result / len(self.get_scores())
        if result >= 0 and result < 40:
            return 'T'
        elif result >= 40 and result < 55:
            return 'D'
        elif result >= 55 and result < 70:
            return 'P'
        elif result >= 70 and result < 80:
            return 'A'
        elif result >= 80 and result < 90:
            return 'E'
        else:
            return 'O'






    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
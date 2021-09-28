# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:11:56 2021

@author: jyanc
"""
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def identify_self(self):
        print("This is a " + self.year + " " + self.make + " " + self.model + ".")
        
Serena=Car("Subaru","Outback","2012")
Serena.identify_self()

Jeff=Car("Jeep","Grand Cherokee","2015")
Jeff.identify_self()

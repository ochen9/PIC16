#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:37:28 2019

@author: oliviachen
"""

def draw_ngon(n):
    window = turtle.Screen()
    window.bgcolor("white")
    
    t=turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    
    angle = (360/n)
    
    for i in range(n):
        t.right(angle)
        t.forward(100)
    
    window.exitonclick()
    
    
print "What is n?"
n= input()
draw_ngon(n)
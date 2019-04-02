#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:25:08 2019

@author: oliviachen
"""

import Tkinter as Tk
import numpy as np


class RectangleGUI:
    
    
    def __init__(self, root, n):
        self.visited = np.zeros([n, n])
        self.n = n
        self.d=100  #length of side of a square
        self.x = 0
        self.y = 0
        
        self.canvas = Tk.Canvas(root, width = self.n * self.d, height = self.n * self.d)
        self.lastposition_x = self.x
        self.lastposition_y = self.y
        
        
        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(i*self.d, j*self.d, i*self.d+self.d, j*self.d+self.d, fill="white")
        
        self.canvas.create_rectangle(0,0,self.d,self.d,fill = "orange")
        
        self.canvas.pack()
        
        self.canvas.bind('<Button-1>', self.mouse_click)
        
        
    def draw_rec(self, x, y, fill):
            self.canvas.create_rectangle(x,y,x+self.d, y+self.d, fill=fill)
        
        
    def mouse_click(self,ev):  #ev is event
        square_x = (ev.x/self.d)*self.d
        square_y = (ev.y/self.d)*self.d
        if(self.is_valid(square_x, square_y)):
            self.draw_rec(square_x, square_y,"orange")
            self.draw_rec(self.lastposition_x, self.lastposition_y, "blue")
            self.lastposition_x=square_x
            self.lastposition_y=square_y
    
    def is_valid(self, s_x, s_y):
        
        #print s_x, s_y
        if(abs(s_x - self.lastposition_x)/self.d==2 and abs(s_y - self.lastposition_y)/self.d==1) or (abs(s_x - self.lastposition_x)/self.d==1 and abs(s_y - self.lastposition_y)/self.d==2):
            return True
        else:
            return False
        
        
    
def knights_tour(n):
    root = Tk.Tk()
    gui = RectangleGUI(root,n)
    root.mainloop()
    
knights_tour(7)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:42:18 2019

@author: oliviachen
"""

import numpy as np
import matplotlib.pyplot as plt

dataset = []

with open("heart.csv") as F:
    count = 0
    for i in F:
        count += 1
        try:
            dataset.append(map(lambda x: int(x)-1,i.split(",")))
        except:
            pass
        
        if count==100:
            break
            
dataset_np = np.zeros((np.max(dataset)+1,np.max(dataset)+1))
for i in dataset:
    dataset_np[i[0], i[1]] = 1
    
print dataset_np

pos_x = []
pos_y = []

for i in range(dataset_np.shape[0]):
#     pos_x.append(np.random.random()*100)
#     pos_y.append(np.random.random()*100)
    
    pos_x.append(np.cos(2*np.pi/dataset_np.shape[0]*i)*100)
    pos_y.append(np.sin(2*np.pi/dataset_np.shape[0]*i)*100)
    
    
s = map(lambda x: 100*(x+1), np.sum(dataset_np,axis=1))
plt.figure(figsize=(10,10))
plt.scatter(pos_x,pos_y, s=s)

for i in range(dataset_np.shape[0]):
    plt.annotate(i, [pos_x[i],pos_y[i]],fontsize=20)
    
for i in range(dataset_np.shape[0]):
    for j in range(dataset_np.shape[0]):
        if dataset_np[i,j]==1:
            plt.plot([pos_x[i],pos_x[j]],[pos_y[i],pos_y[j]], 'r', markersize=10)
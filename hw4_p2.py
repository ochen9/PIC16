#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:32:27 2019

@author: oliviachen
"""

#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


d = pd.read_csv('heart.csv')
age = d['age']
chol = d['chol']


plt.hist(age, bins=20)
plt.xlabel("Age (years)")
plt.ylabel("Cholesterol Level")

plt.title('Age vs. Cholesterol Levels')
plt.show()


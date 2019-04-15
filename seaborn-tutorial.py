# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:29:05 2019

@author: Kelly

https://seaborn.pydata.org/tutorial.html
"""

# Visualizing statistical relationships

import numpy as np
import pandas as pd
import maplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')

# scatterplot
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips)

# color based on smoker
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)

# change the mark type based on smoker
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)

# vary the mark type and color based on different fields
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)

# if the hue variable is categorical, a categorical color scale will be used
# if the hue variable is continuous, a continuous color scale will be used
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)

# use a different sequential palette
# ch = cubehelix
# r = rotation
# l = lightness
sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", 
            data=tips)

# vary the size of the marks
sns.relplot(x="total_bill", y="tip", size="size", data=tips)

# point sizes are normalized into a range
# customized range
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15,200), data=tips)            
            
            
            
            
            
            
            
            tips)
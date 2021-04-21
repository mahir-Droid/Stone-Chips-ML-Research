# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:48:23 2020

@author: mahir
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100, 3))


print(df.size)

from scipy import stats
df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]





print(df.size)
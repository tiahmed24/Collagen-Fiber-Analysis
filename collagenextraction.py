# -*- coding: utf-8 -*-
"""CollagenExtraction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u5i6BQScHnaRVx36aqc3PZl2gNotmIgH
"""

import sys
import pandas as pd
import numpy as np

filename = sys.argv[1]
df = pd.read_csv(filename, sep = "\t", header = None)
print(filename, df[1].iloc[6])

# call python CollagenExtraction.py /pathtofile in bash
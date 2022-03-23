#Pandas 
import pandas as pd
import numpy as np

idx = pd.date_range('2000', '2005', freq='d', closed='left')
datas = pd.DataFrame({'Color':  [ 'green' if x> 1 else 'red' for x in np.random.randn(len(idx))], 
         'Measure': np.random.randn(len(idx)), 'Year': idx.year},
          index=idx.date)
datas.head()

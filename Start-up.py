import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)

def fxn():
    warnings.warn("deprecated", DeprecationWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

    
    
    
    
    
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                            Pandas df.iterrow 平行處理
# ========================================================================================

import multiprocessing

#指定主機有多少CPU，並把df 平均分配size
num_processes = multiprocessing.cpu_count()
chunk_size = int(df.shape[0]/num_processes)

#將df 拆解成 num_processes 個 chunk 的df list
chunks = [df.ix[df.index[i:i + chunk_size]] for i in range(0, df.shape[0], chunk_size)]

#定義 function
def myfunc(d):
   return d * d

pool = multiprocessing.Pool(processes=num_processes)
result = pool.map(myfunc, chunks)
# ========================================================================================
# ========================================================================================
# ========================================================================================



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                            pandas iterrows with tqdm
# ========================================================================================
' for jupyter notebook'
from tqdm import tqdm_notebook as tqdm
' for prompt'
from tqdm import tqdm

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
   print("index",index)
# ========================================================================================
# ========================================================================================
# ========================================================================================



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                            second max()
# ========================================================================================
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:m1, m2 = x, m1            
            else:m2 = x
    return m2 if count >= 2 else None
# ========================================================================================
# ========================================================================================
# ========================================================================================





# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       pandas_profiling DataFrame 詳細資料分析視覺化
# ========================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling as pdp
pd.set_option('display.max_columns', 500)

from sklearn.datasets import load_boston

data = load_boston()
df_boston = pd.DataFrame(data = data.data , columns= data.feature_names)
pdp.ProfileReport(df_boston)

pfr = pdp.ProfileReport(df_boston)
pfr.to_file('report.html')

# ========================================================================================
# ========================================================================================
# ========================================================================================








# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       "月"加減
# ========================================================================================
def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta
   
def monthadd(sourcedate,months):
     month = sourcedate.month - 1 + months
     year = sourcedate.year + month // 12
     month = month % 12 + 1
     day = min(sourcedate.day,monthrange(year,month)[1])
     return date(year,month,day)
# ========================================================================================
# ========================================================================================
# ========================================================================================


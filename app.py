import pandas as pd
#import numpy as np
import json
import uuid

def proccess_data(df):
  jsonStr = df.to_json(orient='records')
  #print('jsonStr: \n', jsonStr)
  
  jsonObj = json.loads(jsonStr)
  
  #for item in jsonObj:
    #print(item)
    #for attribute, value in item.items():
        #print(attribute, value) # example usage


messagegroup = str(uuid.uuid1()).replace('-', '')
print('messagegroup: ', messagegroup)

try:
  df = pd.read_csv("data.csv", sep = ",")
  #print(df)
except Exception as error:
  print('Erro ao ler o CSV: ', error)

#Criando lotes para inserção no banco e envio para a fila SQS
try:
  #sz = 10
  #chunk_size = int(df.shape[0] / sz)
  chunk_size = int(10)
  print('chunk_size: \n', chunk_size)
  for start in range(0, df.shape[0], chunk_size):
      df_subset = df.iloc[start:start + chunk_size]
      print('df_subset: ', df_subset)
      try:
        proccess_data(df_subset)
      except Exception as error:
        print('Erro ao processar o chunk: ', error)
except Exception as error:
  print('Erro criar chunks com o dataframe: ', error)

"""
try:
  n = 10
  chunks = [df[i:i+n] for i in range(0,df.shape[0],n)]
  #print('chunks: ', chunks)
except Exception as error:
  print('Erro criar chunks com o dataframe: ', error)

try:
  np_df = df.to_numpy()
  print(np_df)
except Exception as error:
  print('Erro ao converter o dataframe em array numpy: ', error)

try:
  np.split(np_df)
except Exception as error:
  print('Erro ao fazer o split do array: ', error)
"""
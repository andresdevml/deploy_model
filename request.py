
# aqui haremos las peticiones y verificaremos todo anda bien 

import requests
import pandas as pd 
import numpy as np

url = 'http://127.0.0.1:2205/predict'

# extraemos data para hacer una verificacion de servidor 

data=pd.read_csv(
		filepath_or_buffer='./in/data.csv',
		index_col=False).sample(5)

# Preparamos la data 

X=data.drop(columns='target', axis=1).to_numpy()
Y=data['target'].to_numpy()

input_data=X.tolist()

response= requests.post(url,json={'data':input_data})

print(np.array(response.json()['y_pred'])==Y)
print(Y)

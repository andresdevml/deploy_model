

# implementacion de la API que dara servicio

from flask import Flask
from flask import jsonify
from flask import request
import pickle
import numpy as np 


app=Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
	# input_data sera un json, para comodidad del usuario servido 
	
	try:
	
		input_data=np.array(request.get_json(force=True)['data'])
	
		prediction = model.predict(input_data).tolist()
	
		return jsonify(y_pred=prediction)
		
	except:
		print('\n\nHubo un error')
	
if __name__=='__main__':
	
	filename='./pipeline_model.pkl'
	
	model = pickle.load(open(filename, 'rb'))
	
	app.run(port=2205,debug=True)
	
	

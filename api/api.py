from flask import Flask, request,jsonify

import logging


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)



@app.route('/')
def home():
	return {'message':'container b - flask app - route /'}

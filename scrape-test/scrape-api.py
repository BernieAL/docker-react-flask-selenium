from flask import Flask, request,jsonify

import scraper
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)

scraping_status = "in_progress"

@app.route('/')
def home():
	return {'message':'at scrape-api /'}

@app.route('/scrape',methods=['GET','POST'])
def scrape_route():
	
	global scraping_status
	result = scraper.scrape_func(scraping_status)
	if result['success'] == False:
		scraping_status ="DID NOT COMPLETE"
	else:
		scraping_status = "COMPLETED"
		# # return {'message':'at scrape-api /scrape'}
	return jsonify(result)



@app.route('/scrape/status',methods=['GET'])
def get_scraping_status():
	global scraping_status
	return jsonify({'status':scraping_status}),200


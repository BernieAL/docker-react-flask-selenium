from flask import Flask,jsonify 
import requests
import scraper
import logging
import asyncio


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)

scraping_status = "in_progress"

@app.route('/')
def home():
	return {'message':'at scrape-api /'}

@app.route('/scrape',methods=['GET','POST'])
async def scrape_route():
	
	scrape_result = await scraper.scrape_func()
	
	requests.post('http://127.0.0.1:5000/scrape_api/scraped_data',json={'result':'some text'})

	




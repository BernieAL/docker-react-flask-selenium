from flask import Flask,jsonify,render_template
import requests
import os
import psycopg2
import logging

from dotenv import load_dotenv
load_dotenv


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)



def get_db_connection():
    conn = psycopg2.connect(host='pgsql',
                            database='test',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/api')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({'books': books})

@app.route('/check_for_vehicle' ,methods=['POST'])
def check_for_vehicle():

	"""
	to simulate api requst from react front end
	put query params in the url
	"""
	#check if veh submitted on form is in db
	#if in db, return data to front end
	#if not in db perform scrape

	#get params of request
	make = request.args.get('make')
	model = request.args.get('model')
	year = request.args.get('year')

	data = DB_execute_queries


	


# @app.route('/scrape_api/scrape', methods=['GET'])
# def trigger_scrape():
	
# 	requests.post('http://127.0.0.1:7777/scrape')
	

# @app.route('/scrape_api/scraped_data',methods=['GET','POST'])
# def scrape_result():

# 	data = request.json
# 	print(data)





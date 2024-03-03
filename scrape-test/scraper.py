import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger(__name__)

def scrape_func():
	
	output_file = "output.csv" #relative path
	success_result = False

	logger.info("starting scrape_func")

	try:
		chrome_options = Options()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-dev-shm-usage')
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
		
		url = f'https://www.neuralnine.com/'
		driver.get(url)

		soup = BeautifulSoup(driver.page_source,'lxml')
		headings = soup.find_all('h2',{'class':'elementor-heading-title'})
		content = [str(heading) for heading in headings]

		with open(output_file, mode='w') as file:

			for line in content:
				file.write(line + '\n')

		#if eveything successful
		success_result = True
		logger.info("scraping and file writing completed successfully")
	
	except:
		logger.error(f"Error Occured {str(e)}")

	finally:
		# time.sleep(10)
		driver.quit()

	return success_result


if __name__ == '__main__':
	scrape_func()
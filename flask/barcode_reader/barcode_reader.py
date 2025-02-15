
import requests
from bs4 import BeautifulSoup

class BarcodeReader:

	def __init__(self):
		pass

	def scanItem(self):
		pass

	def getItemName(self, upc:int):
		req = requests.get(f'https://go-upc.com/search?q={upc}')
		soup = BeautifulSoup(req.text, features='html.parser')
		name = soup.find(class_='product-name').text

	def addItem(self, item):
		pass

if __name__ == "__main__":
	reader = BarcodeReader()
	reader.getItemName(180854000309)
import json
import requests

items = {"tritanium": 34, 
	"pyerite": 35,
	"mexallon": 36,
	"isogen": 37,
	"nocxium": 38,
}	

class DataCollector():
	def load_info(self):
		url = build_url()

		response = requests.get(url)

		data = json.loads(response.content)

		
	def build_url(self):
		base = "http://api.eve-central.com/api/marketstat/json?"
		
		for key in items.iteritems():	
			base = base + "typeid=" + items[key] 

		return base




import json
import requests

items = {"tritanium": 34, 
	"pyerite": 35,
	"mexallon": 36,
	"isogen": 37,
	"nocxium": 38,
}	

inv_items = { v: k for k, v in items.items() }

class DataCollector(object):
	def load_info(self):
		url = self.build_url()

		response = requests.get(url)

		self.data = json.loads(response.content)
		for item in self.data:
			print self.inv_items[item["buy"]["forQuery"]["types"][0]] + ": " + str(item['buy']['fivePercent'])

		
	def build_url(self):
		base = "http://api.eve-central.com/api/marketstat/json?regionlimit=10000002&"
		
		for key in self.items:
			base = base + "typeid=" + str(self.items[key]) + "&"
	
		return base


	def __init__(self):
		self.items = items
		self.inv_items = inv_items


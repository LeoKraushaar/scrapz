from mongo.mongo_manager import MongoManager
from constants import *
from pprint import pprint

class RecipeFinder:

	def __init__(self, mongo:MongoManager):
		self.mongo = mongo

	def findRecipe(self):
		pass

	def suggestRecipe(self):
		pass

	def getOwnedItems(self):

		self.mongo.pipeline += self.mongo.match(
			[{'categoryLabel':'food'}, {'quantity_owned':{'$gt':0}}],
			match_all=True
		)
		self.mongo.pipeline += self.mongo.project(
			['label', 'quantity_owned']
		)
		print(self.mongo.pipeline)
		items = self.mongo.executePipeline(ITEMS)
		pprint(items)

if __name__ == '__main__':
	finder = RecipeFinder(MongoManager(DB))
	finder.getOwnedItems()
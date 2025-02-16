from mongo.mongo_manager import MongoManager

class RecipeFinder:

	def __init__(self, mongo:MongoManager):
		self.mongo = mongo

	def findRecipe(self):
		pass

	def suggestRecipe(self):
		pass

	def getOwnedItems(self):
		items = 

if __name__ == '__main__':
	finder = RecipeFinder()
	finder.getOwnedItems()
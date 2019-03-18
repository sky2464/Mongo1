from pymongo import MongoClient
import pandas as pd 


class MongoDB():
	"""docstring for MongoDB"""
	def __init__(self):
		super(MongoDB, self).__init__()
		self.client = MongoClient('127.0.0.1', 27017)
		self.db = self.client['Spring19']
		self.user_collection = self.db ['users']

		
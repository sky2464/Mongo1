import pymongo
import py2neo
import os

class MainMenu():
	"""docstring for Men"""
	#def __init__(self):
		#self.MongoDB = MongoDB ()

	def menu(self):
		print("1 for connection")
		print("2 query MongoDB")
		print("3 query Neo4j")
		print("4 history")
		print("5 quit")

	def choice(self, choice):
		if( choice =="1"):
			print(" connection\n")
		if (choice =="2"):
			print("query MongoDB\n")
		if (choice == "3"):
			print ("query Neo4j\n")
		if (choice =="4"):
			print ("history\n")
		if (choice == "5"):
			quit()

	def run(self):
		print ("Welcome to Colloborate.NEt")
		while (True):
			self.menu()
			theChoice = input("choice: ")
			self.choice(theChoice)


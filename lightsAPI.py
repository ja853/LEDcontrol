#!/usr/bin/python3

import cgitb  # Common Gateway Interface TraceBack
#import pymysql
import lights
import getLEDStatus

from flask import Flask
import json

app = Flask(__name__)

lights.setup()

@app.route("/toggle")
def Toggle():
    #lights.main1() # worked
    status = getLEDStatus.getStatus()
    print(status)
    lights.toggle(status)
    return "hello there"


"""
connection = pymysql.connect(
    #db='testDB',
    db='recipeTest',
    #user='james@james-XPS-15',
    user='james',
    passwd='mysql',
    host='localhost')

@app.route('/getIngred/<ingredientToFind>', methods=['GET'])
def getSpecific(ingredientToFind):
	tableName = "recipeCard"
        get = "id,ingredients"
	idNumber = "3"
	ingredientToFind = "more"
	cursor = connection.cursor()
	#cursor.execute("SELECT " + get + " FROM " + tableName + " WHERE id = " + idNumber)
	cursor.execute("SELECT " + get + " FROM " + tableName)

	#newDict = {}
	ids = ""
	idList = []
	for result in cursor.fetchall():
		for item in result[1].split(";"):
			if ingredientToFind in item.split("-"):
				ids += str(result[0]) + ","
				idList.append(result[0])
				#newDict.add 

	ids = ids[:-1]
	print(ids)
	#ids = json.dumps(ids)
	#return ids	

#	cursor.execute("SELECT * FROM " + tableName + " WHERE id = " + str(idList))
	print("SELECT * FROM " + tableName + " WHERE id = (" + ids + ")" )
	cursor.execute("SELECT * FROM " + tableName + " WHERE id IN (" + ids + ")" )
	newDict = {}
	newList = []
	i = 0
	for result in cursor.fetchall():
	    #data += result
		#newList = result
		newDict.update({i:result})
		i+=1
		#newList.append(result)
	
	dataToSend = json.dumps(newDict)
	#dataToSend = json.dumps(newList)
	return dataToSend

	ids = ids[:-1]
	ids = json.dumps(ids)
	return ids
	return stringReturn
	
	dataToSend = json.dumps(newDict)
	return dataToSend

@app.route('/getAll', methods=['GET'])
def echo_msg():
    #pythonDictionary = {'name': 'Bob', 'age': 44, 'isEmployed': True}
    #dictionaryToJson = json.dumps(pythonDictionary)
    #return dictionaryToJson

	cursor = connection.cursor()

	cursor.execute("SELECT * FROM numbers")
	#print([result for result in cursor.fetchall()]) # Gives [] around result
	newDict = {}
	for result in cursor.fetchall():
	    #data += result
		newDict.update({result[0]:result[1]})
	

	dataToSend = json.dumps(newDict)
	#print(result)

	
	#thing().do_GET()

	return dataToSend
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0')


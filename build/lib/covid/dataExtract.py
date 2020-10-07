import os 
import csv
from datetime import datetime
import json

# Function to convert a CSV to JSON 
# Takes the file paths as arguments 
def make_json(csvFilePath, jsonFilePath): 
	
	# create a dictionary 
	data = {} 
	
	# Open a csv reader called DictReader 
	with open(csvFilePath, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		# Convert each row into a dictionary 
		# and add it to data 
		for rows in csvReader: 
			
			# Assuming a column named 'No' to 
			# be the primary key 
			key = rows['Country_Region'] 
			data[key] = rows 

	# Open a json writer, and use the json.dumps() 
	# function to dump data 
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 

def extract():
	try:
		date = int(datetime.today().date().day) - 1
		month = datetime.today().date().month
		year = datetime.today().date().year

		if int(date) < 10:
			date = '0' + str(date) 

		elif int(date) <= 0:
			if int(month) in [1,2,4,6,8,9,11]:
				date = 31
				month = int(month) -1

			elif int(month) in [5,7,10,12]:
				date = 30
				month = int(month) -1

			elif int(month) == 3:
				date = 28
				month = int(month) -1
				
		if int(month) < 10:
			month = '0' + str(month) 

		dpath = '/'.join(__file__.split('/')[0:-2])
		os.system(f'cd {dpath}/data && wget https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{date}-{year}.csv?raw=true')
		os.system(f'cd {dpath}/data && mv {month}-{date}-{year}.csv?raw=true {month}-{date}-{year}.csv')

		cdv = f'{month}-{date}-{year}.csv'
		csvFilePath = f'{dpath}/data/{cdv}'
		jsonFilePath = f'{dpath}/data/data.json'
		# Call the make_json function 
		make_json(csvFilePath, jsonFilePath)
		os.system(f'rm -fr {csvFilePath}')

	except FileNotFoundError:
		date = int(datetime.today().date().day) - 2
		month = datetime.today().date().month
		year = datetime.today().date().year

		if int(date) < 10:
			date = '0' + str(date) 

		elif int(date) == 0:
			if int(month) in [1,2,4,6,8,9,11]:
				date = 31
				month = int(month) -1

			elif int(month) in [5,7,10,12]:
				date = 30
				month = int(month) -1

			elif int(month) == 3:
				date = 28
				month = int(month) -1

		elif int(date) == -1:
			if int(month) in [1,2,4,6,8,9,11]:
				date = 30
				month = int(month) -1

			elif int(month) in [5,7,10,12]:
				date = 29
				month = int(month) -1

			elif int(month) == 3:
				date = 27
				month = int(month) -1

		if int(month) == 0:
			month = 12
			year = int(year) - 1
				
		if int(month) < 10:
			month = '0' + str(month)

		

		dpath = '/'.join(__file__.split('/')[0:-2])
		os.system(f'cd {dpath}/data && wget https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{date}-{year}.csv?raw=true')
		os.system(f'cd {dpath}/data && mv {month}-{date}-{year}.csv?raw=true {month}-{date}-{year}.csv')

		cdv = f'{month}-{date}-{year}.csv'
		csvFilePath = f'{dpath}/data/{cdv}'
		jsonFilePath = f'{dpath}/data/data.json'
		# Call the make_json function 
		make_json(csvFilePath, jsonFilePath)
		os.system(f'rm -fr {csvFilePath}')

if __name__ == "__main__":
	extract()
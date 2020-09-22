import os 
import csv
from datetime import datetime
import json


date = datetime.today().date().day - 1
month = datetime.today().date().month
year = datetime.today().date().year

if int(date) < 10:
    date = '0' + str(date) 

if int(date) == 0:
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



os.system(f'cd /home/divyessh/Desktop/covid/Covid19Api/data && wget https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{date}-{year}.csv?raw=true')
os.system(f'cd /home/divyessh/Desktop/covid/Covid19Api/data && mv {month}-{date}-{year}.csv?raw=true {month}-{date}-{year}.csv')

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

    
		

cdv = f'{month}-{date}-{year}.csv'
csvFilePath = f'/home/divyessh/Desktop/covid/Covid19Api/data/{cdv}'
jsonFilePath = r'/home/divyessh/Desktop/covid/Covid19Api/data/data.json'
# Call the make_json function 
make_json(csvFilePath, jsonFilePath)
os.system(f'rm -fr {csvFilePath}')
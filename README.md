# Covid19

This contains files for an API that is used for getting the updates of covid 19 from jhu - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

# Instructions and more

The main logic can be divided in three parts. 
First is the data extraction that is done by dataExtract.py
Then comes converting our obtained csv to json that is done by jso.py
And then we create an api for calling the data.json 
At last we have our main.py that runs all of them together.
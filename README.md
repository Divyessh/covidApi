# Covid19

This contains files for an API that is used for getting the updates of covid 19 from jhu - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

# Instructions and more

We need to run main.sh and it will collect the latest data as well as run our api. 
For that we can add a cronjob:

enter the following command in your command prompt:
crontab -e 

then at bottom write :

10 16 * * * /bin/sh {/path/to/main.sh}
import os
import time
while True:
    os.system(f'python3 Covid19Api/covid/dataExtract.py')
    os.system(f'cd /home/divyessh/Desktop/covid/Covid19Api/covid/ && uvicorn fastApi:app --reload')
    break

source cov/bin/activate
python3 Covid19Api/covid/dataExtract.py
cd /home/divyessh/Desktop/covid/Covid19Api/covid/ && uvicorn fastApi:app --reload
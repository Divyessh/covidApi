from os import system as s

fpath = '/'.join(__file__.split('/')[0:-1])

s(f'python3 {fpath}/dataExtract.py && uvicorn fastApi:app --reload')

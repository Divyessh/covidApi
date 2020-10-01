from os import system as s

s.('cd [path/to/cloned folder]/covid/')
s.('python3 dataExtract.py')
s.('uvicorn fastApi:app --reload')
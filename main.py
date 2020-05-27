from pymongo import MongoClient

url = 'mongodb://sungjin:1234abc@ds149593.mlab.com:49593/heroku_n8ns22rl?retryWrites=false'
client = MongoClient(url)
db = client['heroku_n8ns22rl']
collection = db['test']

collection.insert_one({'a':'b'})

rows = collection.find({})
for row in rows:
  print(row)






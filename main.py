from pymongo import MongoClient

url = 'mongodb://sungjin:1234abc@ds149593.mlab.com:49593/heroku_n8ns22rl?retryWrites=false'
client = MongoClient(url)
db = client['heroku_n8ns22rl']
collection = db['test']

collection.insert_one({'name': 'bobby', 'age': 21})

collection.insert_one({'name': 'kay', 'age': 27})

collection.insert_one({'name': 'john', 'age': 30})

# Q1 : 이름이 bobby인 document(item)를 찾기
rows = collection.find({})
for row in rows:
    if 'name' in row:
        if row['name'] == 'bobby':
            print(row)

# Q2 나이가 21살보다 큰 document(item)를 찾기
rows = collection.find({})
for row in rows:
    if 'age' in row:
        if row['age'] > 21:
            print(row)

# Q3 : 나이가 21살 보다 큰 사람 중 가장 나이가 많은 document(item)를 찾기
rows = collection.find()
# rows = list(collection.find()) 이렇게 한줄만 쓰면 제너레이터를 계속 호출 안해도 쓸 수 있음.

result = []  # 리스트를 통해서 잠시 저장한다.

for row in rows:
    if 'age' in row:
        if row['age'] > 21:
            result.append(row['age'])

max_age = max(result)

rows = collection.find()

for row in rows:
    if 'age' in row:
        if row['age'] == max_age:
            print(row)

# Q4. 나이가 21살 보다 큰 사람 중 가장 나이가 많은 document(item)의 개수를 찾기

0. 무언가의 개수를 찾을 땐 잠시 리스트를 써서 저장한다. Q3에서 result를 쓴것과 동일!!

1. 리스트의 개수를 뽑아낼 땐 len(max_age_result) 를 통해서 구한다.


rows = collection.find()
# rows = list(collection.find())

result = []  # 리스트를 통해서 잠시 저장한다.

for row in rows:
    if 'age' in row:
        if row['age'] > 21:
            result.append(row['age'])

max_age = max(result)

rows = collection.find()

max_age_result = []

for row in rows:
    if 'age' in row:
        if row['age'] == max_age:
            max_age_result.append(row)

print(len(max_age_result))





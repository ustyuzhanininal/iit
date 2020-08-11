from db import connection

with connection.cursor() as result:
    query = """
    	SELECT DISTINCT (country) FROM logs
    """
    result.execute(query)
    data = []
    for row in result:
        data.append(row)

        arr = []
        with connection.cursor() as result2:
        	for value in data:
        		code = value['country']
        		query = "SELECT COUNT(country) as country_count FROM logs WHERE country='{0}'".format(code)
        		result2.execute(query)
        		rows = result2.fetchall()
        		temp = dict()
        		temp['count'] = int(rows[0]['country_count'])
        		temp['code'] = code
        		arr.append(temp)

arr = list(reversed(sorted(arr, key = lambda i: i['count'])))

for i in range(len(arr)):
	print(arr[i])


connection.close()
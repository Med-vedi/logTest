
import re
from collections import Counter
import csv


def reader(filename):

	regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

	with open(filename) as f:
		log = f.read()

		ips_list = re.findall(regexp, log)

	return ips_list
	

def count(ips_list):
	return Counter(ips_list)


def result(count):
	counter = Counter(count)

	max_req_ip = count.most_common(1)[0][0]
	max_req = count.most_common(1)[0][1]

	min_req_ip = count.most_common()[-1][0]
	min_req = count.most_common()[-1][1]

	clicks = sum(count.values())

	mean = clicks/len(count)

	


	print(max_req_ip, '-made-', max_req)
	print(min_req_ip, '-made-', min_req)

	print('Unique IP registered: ',len(count))

	print('Clicks registered: ', clicks)

	print('Mean of requests:', round(mean))






	


# def write_csv(count):
# 	with open('count_l.csv', 'w') as csvfile:

# 		writer = csv.writer(csvfile)

# 		header = ['IP', 'Frequency']

# 		writer.writerow(header)

# 		for item in count:
# 			writer.writerow( (item, count[item]) )

if __name__  == '__main__':
	# reader('dummy-access.log')

	result(count(reader('dummy-access.log')))




import csv

first_file = open('src.csv','r')
second_file = open('data.dat','r')

def task_solving(d1,d2,s1):
	l1 = [(i,d2[key]) for i in s1 for key in d2.keys() if key == i[:len(key)]]
	s2 = set([i for i in s1 for key in d2.keys() if key == i[:len(key)]])
	l2 = [(i,d1[key]) for i in s1.difference(s2) for key in d1.keys() if key == i[:len(key)]]
	l1.extend(l2)
	return l1

def write_in_file(func):
	def wrapper(*args):
		l = func(*args)
		result_file = open('result.txt', 'w')
		for i in l:
			result_file.write('{} => {},{}\n'.format(i[0],i[1][0],i[1][1]))
		result_file.close()
	return wrapper

@write_in_file
def read_files(ff,sf):
	f = [line.strip().split(',') for line in ff]
	s = [line.strip() for line in sf]
	s1 = set(s)
	nl = [len(i[0]) for i in f] 
	d1 = dict([(f[i][0],f[i][1:]) for i in xrange(len(f)) if len(f[i][0])== max(nl)])
	d2 = dict([(f[i][0],f[i][1:]) for i in xrange(len(f)) if len(f[i][0])== min(nl)])
	return task_solving(d1,d2,s1)
		
read_files(first_file,second_file)
first_file.close()
second_file.close()


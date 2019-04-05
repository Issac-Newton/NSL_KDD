import random
def random_num(Max,Count):
	numbers = []
	while len(numbers) < Count:
		a = random.randint(0,Max-1)
		while a in numbers:
			a = random.randint(0,Max-1)
		numbers.append(a)

	return numbers

def get_data(rf,wf,Count):
		all_data = rf.readlines()
		all_data_no = random_num(len(all_data),Count)
		for i in all_data_no:
			print(all_data[i],file=wf,end='')

if __name__ == '__main__':
	rf = open('Split/Normal.txt','r')
	wf = open('Normal_3K.txt','w')
	get_data(rf,wf,3000)
	rf = open('Split/Dos.txt','r')
	wf = open('Dos_1K.txt','w')
	get_data(rf,wf,1000)
	rf = open('Split/Probe.txt','r')
	wf = open('Probe_1K.txt','w')
	get_data(rf,wf,1000)
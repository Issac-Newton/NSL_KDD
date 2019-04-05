import sys
sys.path.append('../Train/')
import T_Extract as T_E

u2r = ['buffer_overflow','loadmodule','perl','rootkit']
r2l = ['ftp_write','guess_passwd','imap','multihop','phf','spy','warezmaster','warezclient']

def get_data_all(attack,wf):
	with open('../KDDTest+.txt','r') as rf:
		all_data = rf.readlines()
		for line in all_data:
			features = line.split(',')
			if features[41] in attack:
				print(line,file=wf,end='')

def get_data_1K(rf,wf):
	all_data = rf.readlines()
	all_data_no = T_E.random_num(len(all_data),1000)
	for i in all_data_no:
		print(all_data[i],file=wf,end='')

if __name__ == '__main__':
	wf = open('R2L_All.txt','w')
	get_data_all(r2l,wf)
	wf = open('U2R_All.txt','w')
	get_data_all(u2r,wf)
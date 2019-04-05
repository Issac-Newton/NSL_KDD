normal = ['normal']
dos = ['back','land','neptune','pod','smurf','teardrop']
probe = ['ipsweep','nmap','portsweep','satan']
u2r = ['buffer_overflow','loadmodule','perl','rootkit']
r2l = ['ftp_write','guess_passwd','imap','multihop','phf','spy','warezmaster','warezclient']

f_normal = open('Train/Split/Normal.txt','a+')
f_dos = open('Train/Split/Dos.txt','a+')
f_probe = open('Train/Split/Probe.txt','a+')
f_u2r = open('Train/Split/U2R.txt','a+')
f_r2l = open('Train/Split/R2L.txt','a+')

with open('KDDTrain+.txt','r') as f:
	lines = f.readlines()
	print(len(lines))
	k = 0
	for line in lines:
		features = line.split(',')
		if features[41] in normal:
			to_file = f_normal
		elif features[41] in dos:
			to_file = f_dos
		elif features[41] in probe:
			to_file = f_probe
		elif features[41] in u2r:
			to_file = f_u2r
		elif features[41] in r2l:
			to_file = f_r2l
		else:
			k = k + 1
		print(line,file=to_file,end='')

	print(k)
import email,os,sys,base64,quopri,re,html,time
from nltk.util import ngrams

import pandas as pd



def SetFrequency(ngram:list,n:int,frequency:dict):	
	s=[''.join(i).replace(' ','') for i in ngram]	

	if n>1:	
		s=[i for i in s if len(i)==n]

	for word in s:
		# getting key's value if the key is empty,set value to zero
		count=frequency.get(word,0) 
		frequency[word]=count+1


def NgramSample(string:str,n:int):
	return list(ngrams(string,n,pad_left=True, pad_right=True, left_pad_symbol='',right_pad_symbol=''))

def FrequencyTester(emlstring:str):		
	# remove url by http domain form for english
	s=re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', emlstring)
	s=re.sub(r'[^a-z]', ' ', s)

	tokens=[token for token in s.split(' ') if token!=""]	
	frequency={}
	frequencycollecter={}


	#################
	##### ngram #####
	#################

	# for i in range(1,6): #ngram
	# 	for j in tokens:
	# 		n_gram=NgramSample(j,i)
	# 		SetFrequency(n_gram,i,frequency)		
	# 	for key,value in frequency.items():
	# 		count=frequencycollecter.get(key,0)
	# 		frequencycollecter[key]=count+value
	# 	frequency={}

	#################
	##### word ######
	#################

	for word in tokens:
		count=frequencycollecter.get(word,0)
		frequencycollecter[word]=count+1
	
	return frequencycollecter

def RemoveTag(htmlcode:str):
	s=re.sub(r'(<([^>]+)>)', ' ', htmlcode)
	return s

def ContentDecoder(emlstring:str,filename:str):
	emlform=email.message_from_string(emlstring)
	emlstring=''

	if emlform.is_multipart():
		emlform=emlform.get_payload()[0]

	if emlform['Content-Transfer-Encoding']=='base64':
		try:
			emlstring=base64.b64decode(emlform.get_payload())
		except:
			#base64 form error in eml 1
			try:
				emlstring=emlform.get_payload()
				emlstring=emlstring + '='*(4-len(emlstring)%4)
				emlstring=base64.b64decode(emlstring)
			except:
				#base64 form error in eml 2
				print(filename)
				emlstring=emlform.get_payload()+'=='
				emlstring=base64.b64decode(emlstring)
		if type(emlstring)!=str:
			try:
				emlstring=emlstring.decode(''.join(emlform.get_charsets()))		
			except UnicodeDecodeError: # shift_jis error
				emlstring=emlstring.decode('cp932')

	elif emlform['Content-Transfer-Encoding']=='quoted-printable':
		emlstring=emlform.get_payload()
		if emlform.get_charsets()!=[None]:
			try:
				emlstring=quopri.decodestring(emlstring).decode(''.join(emlform.get_charsets()))
			except:
				emlstring=quopri.decodestring(emlstring).decode('utf-8')
		else:
			try:
				emlstring=quopri.decodestring(emlstring).decode('ansi')
			except UnicodeDecodeError:
				emlstring=quopri.decodestring(emlstring).decode('cp932')


	if emlform.get_content_type()=='text/html':
		emlstring=RemoveTag(emlstring)
		emlstring=html.unescape(emlstring)
		if emlform.get_charsets()[0]=='shift_jis':
			emlstring=emlstring.encode('utf-8').decode('shift_jis',errors='ignore')
	else: # text/plain
		emlstring=emlform.get_payload()
		emlstring=html.unescape(emlstring)
		if emlform.get_charsets()[0]=='shift_jis':
			emlstring=emlstring.encode('utf-8').decode('shift_jis',errors='ignore')

	# Using only debug
	# print(filename)
	# print(emlform['Content-Transfer-Encoding'])
	# print(emlform.get_charsets())
	# print(emlform.get_content_type())
	# print(emlstring)

	return emlstring.lower()

def EldiaWord(folder:str):

	filelist = os.listdir(folder)
	frequencycollecter={}
	nounlist=[]
	number=1

	for file in filelist:
		if number % 1000 == 0:
			print(number,'\n',file)
		if number % 50000 == 0: # available 50000files
			break
		number+=1

		filepath = os.path.join(folder, file)
		f=open(file_path,encoding='utf-8').read()
		emlstring=ContentDecoder(f,filepath)
		frequency=FrequencyTester(emlstring) # one's file frequnecy

		for key,value in frequency.items(): # getting a word
			count=frequencycollecter.get(key,0)
			frequencycollecter[key]=count+value

	nounlist=sorted(frequencycollecter.items(),reverse=True,key=lambda item:item[1])	


	for i in range(len(nounlist)):
		nounlist[i]=nounlist[i]+(len(nounlist[i][0]),)

	df = pd.DataFrame(nounlist,columns=['words','frequency','ngram'])
	df.to_csv('./English_words_50000_v2.csv',encoding='utf-8-sig')

if __name__=="__main__":

	start=time.time()
	print('start time: ',time.strftime('%Y/%m/%d - %H:%M:%S'))	

	EldiaWord('./your directory/') # input directory path

	print('end time: ',time.strftime('%Y/%m/%d - %H:%M:%S'))		
	print('execution time:',time.time()-start)


import email,os,sys,base64,quopri,re,html,time
from nltk.util import ngrams

import pandas as pd


def SetFrequency(ngram:list,n:int,frequency:dict):	
	s=[''.join(i).replace(' ','') for i in ngram]	

	if n>1:	
		s=[i for i in s if len(i)==n]

	for word in s:
		count=frequency.get(word,0) 
		frequency[word]=count+1


def NgramSample(string:str,n:int):
	return list(ngrams(string,n,pad_left=True, pad_right=True, left_pad_symbol='',right_pad_symbol=''))

def FrequencyTester(emlstring:str):			
	s=re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', emlstring)
	
	# 언어별로 주석풀어서 사용 할 것
	# s=re.sub(r'[^가-힣ㄱ-ㅎ]', ' ', s)	# korean
	# s=re.sub(r'[^\u3041-\u3096\u30A0-\u30FF\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A\u2E80-\u2FD5\uFF5F-\uFF9F\u3000-\u303F\u31F0-\u31FF\u3220-\u3243\u3280-\u337F]', ' ', s)	# japanese	 
	# s=re.sub(u'[^⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', ' ', s)	# hanja

	tokens=[token for token in s.split(' ') if token!=""]	
	frequency={}
	frequencycollecter={}

	for i in range(1,6): #ngram 1~5 gram
		for j in tokens:
			n_gram=NgramSample(j,i)
			SetFrequency(n_gram,i,frequency)		
		for key,value in frequency.items():
			count=frequencycollecter.get(key,0)
			frequencycollecter[key]=count+value
		frequency={}

	return frequencycollecter

def RemoveTag(htmlcode:str):
	s=re.sub(r'(<([^>]+)>)', ' ', htmlcode)
	return s

def ContentDecoder(emlstring:str,filename:str):
	emlform=email.message_from_string(emlstring)

	if emlform.is_multipart():
		emlform=emlform.get_payload()[0]

	if emlform['Content-Transfer-Encoding']=='base64':
		try:
			emlstring=base64.b64decode(emlform.get_payload())
		except:
			#base64 내부 에러 1
			try:
				emlstring=emlform.get_payload()
				emlstring=emlstring + '='*(4-len(emlstring)%4)
				emlstring=base64.b64decode(emlstring)
			except:
				#base64 내부 에러 2
				emlstring=emlform.get_payload()+'=='
				emlstring=base64.b64decode(emlstring)

		if type(emlstring)!=str: #base64를 하고 str이 아닐 경우
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
				try: 
					print('cp932',filename)
					emlstring=quopri.decodestring(emlstring).decode('cp932')
				except:
					print('utf8',filename)
					emlstring=quopri.decodestring(emlstring).decode('euc-kr',errors='ignore')
	else:
		emlstring=emlform.get_payload()
	
	
	if emlform.get_content_type()=='text/html':
		emlstring=RemoveTag(emlstring)
		emlstring=html.unescape(emlstring)
		if emlform.get_charsets()[0]=='shift_jis':
			emlstring=emlstring.encode('utf-8').decode('shift_jis',errors='ignore')	
		elif emlform.get_charsets()[0]=='iso-2022-jp':
			emlstring=emlstring.encode('utf-8').decode('iso-2022-jp',errors='ignore')
	else: # text/plain
		emlstring=RemoveTag(emlstring)
		emlstring=html.unescape(emlstring)
		if emlform.get_charsets()[0]=='shift_jis':
			emlstring=emlstring.encode('utf-8').decode('shift_jis',errors='ignore')	
		elif emlform.get_charsets()[0]=='iso-2022-jp':
			emlstring=emlstring.encode('utf-8').decode('iso-2022-jp',errors='ignore')

	return emlstring.lower();

def EldiaWord(folder:str):

	filelist = os.listdir(folder)
	frequencycollecter={}
	nounlist=[]
	number=1

	for file in filelist:
		if number % 1000 == 0:
			print(number,'\n',file)
		if number % 100001 == 0: # available 100000 files
			break
		number+=1

		filepath = os.path.join(folder, file)
		emlstring=open(filepath,encoding='utf-8').read()
		emlstring=ContentDecoder(emlstring,filepath)
		frequency=FrequencyTester(emlstring) # one's file frequnecy

		for key,value in frequency.items(): # getting a word
			count=frequencycollecter.get(key,0)
			frequencycollecter[key]=count+value

	nounlist=sorted(frequencycollecter.items(),reverse=True,key=lambda item:item[1])	

	for i in range(len(nounlist)):
		nounlist[i]=nounlist[i]+(len(nounlist[i][0]),)

	df = pd.DataFrame(nounlist,columns=['words','frequency','ngram'])
	df.to_csv('./result_100000.csv',encoding='utf-8-sig')

if __name__=="__main__":

	start=time.time()
	print('start time: ',time.strftime('%Y/%m/%d - %H:%M:%S'))	

	EldiaWord('./eml/')

	print('end time: ',time.strftime('%Y/%m/%d - %H:%M:%S'))			
	print('execution time:',time.time()-start)


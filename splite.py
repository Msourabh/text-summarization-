import re
import pickle
text = ''.join(open('J:\mtech\others\irws code\presentation\data\pw_s.txt').readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
#print sentences
dic={}
for i in range(len(sentences)):
    dic[i+1]=sentences[i]


    
pickle.dump(dic,open('pwh.pickle','wb'))

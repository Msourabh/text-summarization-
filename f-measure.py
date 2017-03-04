import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import pickle
import string
from collections import Counter
WORD = re.compile(r'\w+')
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
stop_word=set(stopwords.words("english"))
stemmer=PorterStemmer()
text = ''.join(open('J:\mtech\others\irws code\presentation\data\pw.txt').readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

def clear_punctuation(s):
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string
def fm(vec1,vec2):
    ls=vec1.keys()
    ls1=vec2.keys()
    intersection=len(set(ls)&set(ls1))
    
    if not len(ls):
        pre=0
    else:
        pre=float(intersection)/len(ls)
    if not len(ls1):
        re=0
    else:
        re=float(intersection)/len(ls1)
    if not  (pre)+(re):
        return 0
    else:
        return (2*pre*re)/(pre+re) 
stem=[]
ls=[]
st=''
for i in sentences:
    new=[]
    punch=clear_punctuation(i)
    words=word_tokenize(punch)
    for w in words:
        if w not in stop_word:
            new.append(w)
            
            #new.append(stemmer.stem(w))
    strng=' '.join(new)
    #print strng
    ls.append(strng)
#print new            
#print ls

dic={}
i=1
for i in range(len(ls)):
    dic[i+1]=ls[i]
#print dic
result={}
x=1
for i in range(len(dic)):
    result[x]=text_to_vector(dic[x])
    x+=1
#print result    
final={}
for i in range(len(dic)):
    count=0
    for j in range(len(dic)):
        if i+1 is j+1:
            continue
        else:
            r=fm(result[i+1],result[j+1])
            count+=r
    final[i+1]=count
#print final
lis=list(final.values())
lis.sort()
lis.reverse()
summery={}
x=1
for i in lis:
    for j in range(len(lis)):
        if i is final[j+1]:
            summery[x]=j+1
            
        else:
            continue
    x+=1
#print summery
doc={}
l=1
for i in range(int(.30*len(dic))):
    #print sentences[summery[i+1]-1]
    doc[l]=sentences[summery[i+1]-1]
    l+=1
    #print '\n'
    
pickle.dump(doc,open('f_measurepw.pickle','wb'))          
#hell=pickle.load(open('f-measure.pickle','rb'))
#print hell

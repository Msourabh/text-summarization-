import math
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import string
from collections import Counter
WORD = re.compile(r'\w+')
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

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
            r=get_cosine(result[i+1],result[j+1])
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
last={}
for i in range(int(.30*len(dic))):
    last[i]= sentences[summery[i+1]-1]
    #print '\n'
pickle.dump(last,open('cosine_news.pickle','wb'))    
            

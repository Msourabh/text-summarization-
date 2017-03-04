import math
import pickle
from collections import Counter
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
def intersection(a,b):
     count=0
     for i in a:
          if i in b:
               count+=1
          else:
               continue
          
     return count

def fm(vec1,vec2):
    ls=vec1.values()
    ls1=vec2.values()
    intersections=intersection(ls,ls1)
    #print intersections
    if not len(ls):
        pre=0
    else:
        pre=float(intersections)/len(ls)
        
    if not len(ls1):
        re=0
    else:
        re=float(intersections)/len(ls1)
        
    if not  (pre)+(re):
        return 0
    else:
        
        return (2*pre*re)/(pre+re) 
ms=pickle.load(open('ms.pickle','rb'))
cosine=pickle.load(open('cosine.pickle','rb'))
f_measure=pickle.load(open('f-measure.pickle','rb'))
coper=pickle.load(open('copernic.pickle','rb'))
result=fm(cosine,ms)
print "cosine overlap with ms-genrated extracts\t\t",result
result1=fm(f_measure,ms)
print "f_measure overlap with ms-genrated extracts\t\t",result1
result1=fm(f_measure,cosine)
print "f_measure overlap with cosine-genrated extracts\t\t",result1
result1=fm(cosine,f_measure)
print "cosine overlap with f_measure-genrated extracts\t\t",result1
result1=fm(f_measure,coper)
print "f_measure overlap with copernic-genrated extracts\t\t",result1
result1=fm(cosine,coper)
print "cosine overlap with copernic-genrated extracts\t\t",result1

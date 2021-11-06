import pandas as pd
import numpy as np
print('Please select one out of 5 databases')
which_db=input('Enter 1 for Amazon \nEnter 2 for BestBuy \nEnter 3 for kmart \nEnter 4 for Nike \nEnter 5 for Supremo.\n')

if int(which_db)==1:
    data=pd.read_excel('Amazon.xlsx')
elif int(which_db)==2:
    data=pd.read_excel('BestBuy.xlsx')
elif int(which_db)==3:
    data=pd.read_excel('kmart.xlsx')
elif int(which_db)==4:
    data=pd.read_excel('Nike.xlsx')
elif int(which_db)==5:
    data=pd.read_excel('Supremo.xlsx')
else:
    print('Accepted values are only 1 to 5, else the default database Amazon would be read')
    data=pd.read_excel('Amazon.xlsx')
    
import ast
rows=data['Transaction']
uniques=[]
temp=[]
for eachrow in rows:
    for eachelement in ast.literal_eval(eachrow):
        temp.append(eachelement)
uniques=set(temp)
dicts={'Element': [each for each in uniques],
      'Count':[temp.count(each) for each in uniques]}
print('Count of each items :  \n')

iteration1=pd.DataFrame(dicts)
print(iteration1)

print('This is a database of 20 transactions.Enter any value of support and confidence between 10 to 100%')

support_in_percent=int(input('Enter the support in percent: '))
confidence_in_percent =int(input('Enter the confidence in percent: '))
               
Min_support=int(np.floor((support_in_percent/100)*len(data['Transaction'])))
Min_confidence=confidence_in_percent/100

print('Minimum support in quantity is ', Min_support)
print('Minimum confidence is ', Min_confidence)

OneItem_set = iteration1[iteration1.Count >= Min_support]
print('Items with counts that satisfies the minimum support')
print(OneItem_set)
Combined=[]
import itertools
for i in range(1, len(OneItem_set)+1):
    x=list(itertools.combinations(OneItem_set.Element, i))
    Combined.append(x)
    
#print(Combined)

# K-implies Iitemset containing set of 1, 2, 3...K elements iteratively
import ast
filtered=[]
k=len(Combined)
count=0
elements=[]
counts=[]
#print(set(Combined[2][0]))
for i in range(k):
    for j in range(len(Combined[i])):
        for each in rows:
            each=ast.literal_eval(each)
            #print(each)
            if set(list(Combined[i][j])).issubset(each):
                count=count + 1
        counts.append(count)
        elements.append(list(Combined[i][j]))
        count=0
                
x={'Items': elements,
    'Support': counts}
datalist=pd.DataFrame(x)
#print('Possible Set of items')
#print(datalist)

datalist=datalist[datalist.Support >= Min_support]
print('Possible set of items meeting the minimum support')
print(datalist)
import itertools
y=list(itertools.combinations(datalist.Items, 2))
finalList=[]
for i in range(len(y)):
    x=list(y[i])
    finalList.append(x)
#print(finalList)
FL=[]
for i in range(len(finalList)):
    a=finalList[i][0]
    b=finalList[i][1]
    if not any(x in a for x in b):
        FL.append(finalList[i])  
print('\n\n')
freq1item=[]
if len(FL)==0:
    print('Frequent items are as below:\n\n',datalist['Items'])
else:
    for i in range(len(FL)):
        for j in range(len(FL[i])):
            if ((FL[i][j] not in freq1item) and len(FL[i][j])==1):
                freq1item.append(FL[i][j])


    freq1item.append(FL)
    print('Frequent items are as below:\n\n',freq1item)

#Defining support and confidence
mylist=[]
flatlist=[]
def supportboth(item):
    counts=0
    for j in range(len(data['Transaction'])):
        flatlist=[ j for i in item for j in i]
        flatlistset=set(flatlist)
        #print(flatlistset)
        everyrow=ast.literal_eval(data['Transaction'][j])
        row=set(everyrow)
        is_subset=flatlistset.issubset(row)
        if is_subset:
            counts=counts + 1
    num=counts
    denom= len(data['Transaction'])
    return num/denom
def supportfirst(item):
    counts=0
    for j in range(len(data['Transaction'])):
        itemset=set(item)
        everyrow=ast.literal_eval(data['Transaction'][j])
        row=set(everyrow)
        is_subset=itemset.issubset(row)
        if is_subset:
            counts=counts + 1
    num=counts
    denom= len(data['Transaction'])
    return num/denom
def confidence(items):
    conf=supportboth(items)/supportfirst(items[0])
    return conf
def confidenceReverse(items):
    conf=supportboth(items)/supportfirst(items[1])
    return conf

confidence_levels_rev=[]
confidence_levels=[]
for each in FL:
    confidence_levels.append(confidence(each))
    confidence_levels_rev.append(confidenceReverse(each))
    

dict_temp={'Items':FL,
           'Confidence':confidence_levels,
           'ConfidenceOfreverse':confidence_levels_rev
          }
x=pd.DataFrame(dict_temp)
print(x)

x1=x[x.Confidence >= Min_confidence]
x2=x[x.ConfidenceOfreverse >= Min_confidence]

if (len(x)==0):
    print('No Association found between items with given support and confidence, Try with lesser support or confidence ')
    
elif(len(x1)==0 and len(x2)==0):
        print('No Association can be found at the given confidence')
        
else:
    print('Association rules found are:\n')
    ya=x1.Items.tolist()
    yb=x2.Items.tolist()
    conf=x1.Confidence.tolist()
    confrev=x2.ConfidenceOfreverse.tolist()
    for i in range(len(ya)):
        print(ya[i][0],' --> ',ya[i][1],'    C =', format(conf[i],".2f"))
    for i in range(len(yb)):
        print(yb[i][1],' --> ',yb[i][0],'    C =', format(confrev[i],".2f"))


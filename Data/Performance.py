import sys
import math

def get_blast(filename):
    flist=[]
    d={}
    f=open(filename)
    for line in f:
        v=line.rstrip().split()
        d[v[0]]=d.get(v[0],[])
        d[v[0]].append([float(v[1]),int(v[2])])
    for v in d.values():
        v.sort()
        flist.append(v[0])
    return flist

# def get_data(filename):
#     ldata=[]
#     f=open(filename)
#     for line in f:
#         v=line.rstrip().split()
#         ldata.append([float(v[1]),int(v[2])])
#     return(ldata)

def get_cm(data,th):      #generation of the confuion matrix #0 NEGATIVE , 1 POSITIVE --> Data is a list with in 0 the treshold and in 1 the class (0) or (1)
    cm=[[0.0,0.0],[0.0,0.0]]
    for i in data:
        if i[0]<th and i[1]==1: #this is a TRUE POSITIVE, the class of the positi it's 1 and if it's lower than the treshold is predicted as a positive
            cm[0][0]=cm[0][0]+1
        if i[0]>=th and i[1]==1: #This will be a FALSE NEGATIVE
            cm[1][0]=cm[1][0]+1 #
        if i[0]<th and i[1]==0: #FALSE POSITIVE --> Becasue the model has predicted them as positive, but we know that they are NEGATIVE (the class is 0) so it's a FALSE POSITIVE. So the control
                                                   #take the e-value that hmmsearch had predicted. If this is lower (better) respec to the th that we are looping we say that it is a positive, BUT it comes from the NEGATIVE set --> It is a FALSE POSITIVE
            cm[0][1]=cm[0][1]+1
        if i[0]>th and i[1]==0: #This is a TRUE NEGATIVE
            cm[1][1]=cm[1][1]+1
    return cm

def get_acc(cm):
    return float(cm[0][0]+cm[1][1])/(sum(cm[0])+sum(cm[1]))

def mcc(m):
    d=((m[0][0]+m[1][0])*(m[0][0]+m[0][1])*(m[1][1]+m[1][0])*(m[1][1]+m[0][1]))
    return (m[0][0]*m[1][1]-m[0][1]*m[1][0])/math.sqrt(d)

if __name__=="__main__":
    filename=sys.argv[1]  #This will take in input the file with positives or negatives
    #th=float(sys.argv[2]) #e-value treshold You have to un-comment if you want to test the performance on a particular e-value
    data=get_blast(filename)
    for i in range(20):  #And run an e-value treshold that start from 10e-0 to 10e-20
        th=10**-i   #We loop the th because we want to know what are the poerformance for different thershold
        cm=get_cm(data,th) #If I want to generate the threshold with the loop I have to indentate this one.
        print("TH",th,"ACC",get_acc(cm),"MCC",mcc(cm),cm) #And calculate threshold, accuracy and matthew correlation coefficient

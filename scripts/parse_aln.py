import sys
import numpy as np

def get_aln(alnfile):
    d_aln={}
    f=open(alnfile)
    for line in f:
        if line.find("sp")!=0: continue # will skip the line if it doesn't begn with "sp"
        l=line.split()
        sid=l[0]
        seq=l[1]
        d_aln[sid]=d_aln.get(sid, "")+seq # call the dictionary and check if the key of the dictionary exist. And if not it will return as "error" The empty string
    return(d_aln)

def get_profile(d_aln):
    profile=[]
    l=list(d_aln.values())
    n=len(l[0]) #this will be the lenght of the alignment
    print(n)
    sids=d_aln.keys() #Sequence ID
    print(d_aln)
    for i in range(n):
        aas=[]
        for j in sids:
            aas.append(d_aln[j][i])
            print(i,j,d_aln[j][i]) #I will get for every position the letter of the five sequences.
        vaas=get_iprofile(aas)
        tot=float(vaas[:20].sum())
        print(i,aas,vaas,vaas[:20].sum())
        #vaas[:20]/tot
        for j in range(20):
            vaas[j]=vaas[j]/tot
        profile.append(vaas)
        #print(i,vaas)
    return (profile)

def get_iprofile(aas,aa_list="ACDEFGHIKLMNPQRSTVWY-"):
    v=np.zeros(len(aa_list)) #generate a list/vector of 0s of len equal to all --> zeros is a specific function of numpy
    for aa in aas:
        pos=aa_list.find(aa)
        if pos > -1: # I don't know the meaning
            v[pos]=v[pos]+1
    #r=vpos
    return(v)

def print_profile(profile,aa_list="ACDEFGHIKLMNPQRSTVWY-"):
    n=len(profile)
    for i in range(n):
        pi=profile[i][:20]
        s=np.sum(-pi*np.log(pi))
        pm=pi.argmax()
        print(i,s,pi[pm],aa_list[pm])

if __name__=="__main__":
    alnfile=sys.argv[1]
    d_aln=get_aln(alnfile)
    profile=get_profile(d_aln)
    print_profile(profile)
    # for sid in d_aln.keys():
    #     print(sid.split("|")[1],d_aln[sid])

# CCCFFCRRRCCSSSSFSFRRFFSSFSCSRRS CFFFRCRCRCFSCSRFSFRRFCSSFRCSR
import sys, random
import numpy as np

def get_alphabet(seq):
    alpha=[]
    for a in seq:
        if a not in alpha:
            alpha.append(a)
    alpha.sort()
    #return(alpha)
    return("".join(alpha))

def get_tmatrix(seq,alpha):
    n=len(alpha)
    tm=np.zeros((n,n))
    l=len(seq)
    for i in range(l-1):
        p1=alpha.find(seq[i])
        p1=alpha.find(seq[i+1])
        if p1>-1 and p2>-1:
            tm[p1][p2]+=1
    for i in range(n):
        print(alpha[i],np.sum(tm[i,:]))
    return(tm)

def get_prob(seq,tm,alpha):
    p=1.0
    l=len(seq)
    for i in range(l-1):
        pos1=alpha.find(seq[i])
        pos2=alpha.find(seq[i+1])
        if pos1>-1 and pos2>-1:
            p=p*tm[pos1][pos2]
    return(p)

def print_logp(p):
    if p>0:
        lp=-np.log10(p)
    else:
        lp=np.inf
    return(lp)

def get_shuffle(seq):
    l=[i for i in seq]
    random.shuffle(l)
    return("".join(l))

if __name__=="__main__":
    seq=sys.argv[1]
    tseq=sys.argv[2]
    alpha=get_alphabet(seq)
    print(seq)
    tm=get_tmatrix(seq,alpha)
    print(tm)
    p=get_prob(seq,tm,alpha)
    tp=get_prob(tseq,tm,alpha)
    print(print_logp(p))
    print(print_logp(tp))
    for i in range(200):
        nseq=get_shuffle(seq)
        np=get_prob(nseq,tm,alpha)
        print(nseq,print_logp(np))
        #print(print_logp(np))

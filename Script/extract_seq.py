# !/usr/bin/python
import sys

def get_ids(idfile):
    ids=open(idfile).read().rstrip().split("\n")
    return(ids)

def print_seqs(ids,dbfile):
    with ope(dbfile, "r") as fdb: #IDK the meaning of the sintaxt "with open..."
        for line in fdb:
            if line[0]==">":
                #pid=line.split("|")[1]
            if pid in ids:
                print(line.rstrip())

if __name__=="__main__":
    idfile=sys.agv[1]
    dbfile=sys.argv[2]
    ids=dis_ids(idfile)

# Built a method for structural superimposition
import sys
from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np

def getCa(pdbfile,chain,rlist,atom="CA"):
    fpdb=open(pdbfile)
    l_coord=[]
    for line in fpdb:
        #line.rstrip() #rstreap -> beacuse you remove the blanckspace to the RIGHT
        if line[:4]== "ATOM" and line[21]== chain and line[22:26].strip() in rlist and line[13:16].strip() == atom:
            x=float(line[30:38])
            y=float(line[38:46])
            z=float(line[48:54])
            l_coord.append([x,y,z])
        #print(line.rstrip())
    return(l_coord)

def get_rmsd(coord1,coord2):
    if len(coord1)!=len(coord2):
        print >> sys.stderr.write("ERROR: The set of Coordinate have different size.")
        sys.exit(1)
    svd=SVDSuperimposer()
    svd.set(np.array(coord1), np.array(coord2))
    svd.run()
    rmsd=svd.get_rms()
    #rot,tran=svd.get_rotran()
    T=svd.get_rotran()
    print("R", T[0])
    print("T", T[1])
    return(rmsd)

if __name__ == "__main__":
    #print(sys.argv) #Print the path of the element that i give as input
    pdbfile1=sys.argv[1]
    pdbfile2=sys.argv[2]
    chain1=sys.argv[3]
    chain2=sys.argv[4]
    list1=sys.argv[5].split(",")
    list2=sys.argv[6].split(",")
    l_coord1=getCa(pdbfile1,chain1,list1)
    l_coord2=getCa(pdbfile2,chain2,list2)
    print("COORD1 :",l_coord1)
    print("COORD2 :",l_coord2)
    #print(pdbfile1,pdbfile2)
    rmsd=get_rmsd(l_coord1,l_coord2)
    print("RMSD", rmsd)

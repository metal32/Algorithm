"""""""" ##TOWER OF HANOBI """"""""
""""""""                 """"""""

def towerOfHanobi(size,fromstack,tostack,sparestack):
    count=0   
    if size==1:
        print "Move disk from {} to {}.".format(fromstack,tostack)
    else:
        towerOfHanobi(size-1,fromstack,sparestack,tostack)
        towerOfHanobi(1,fromstack,tostack,sparestack)
        towerOfHanobi(size-1,sparestack,tostack,fromstack)
towerOfHanobi(5,"A","B","C")
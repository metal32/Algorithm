from pylab import *
import random

def FlipTrial(numFlips):
    heads, tails=0, 0
    for i in xrange(numFlips):
        coin=random.randint(0,1)
        if coin==0: 
            heads+=1
        else: 
            tails+=1
    return heads, tails

def simFlip(numFlips,numTrials):
    diffs=[]
    for i in xrange(0,numTrials):
        heads, tails=FlipTrial(numFlips)
        diffs.append(abs(heads-tails))
    diffs=array(diffs)
    meandiffs=sum(diffs)/len(diffs)
    percentdiff=((diffs)/float(numFlips))*100
    percentmean=sum(percentdiff)/len(percentdiff)
    hist(diffs,bins=15)
    axvline(meandiffs, label='Mean')
    legend()
    titlestring=str(numFlips)+' Flips '+str(numTrials)+' Trials'
    title(titlestring)
    xlabel('Difference between Head and Tails')
    ylabel('Number of trials')
    figure()
    plot(percentdiff)
    axhline(percentmean, label='Mean')
    legend()
    title(titlestring)
    ylabel('Percent difference between Head and Tails')
    xlabel('Trial Number')
    

#simFlip(500,100)
#figure()
simFlip(1000,100)
show()


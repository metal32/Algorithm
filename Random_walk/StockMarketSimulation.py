# if you have a lot of money and wants to invest in stock market. 
# You can invest through indexed portfolio or thorugh managed portfolio
# Efficient market hypothesis theory is being used to model it, so this model is also know as memory less as it doesn't depend on the 
# past performances of stocks (Random Walk Model)
import pylab
import random
class Stock(object):
    def __init__(self,price, distribution):
        self.price=price
        self.history=[price]
        self.distribution=distribution
        self.lastchange=0
    def setPrice(self, price):
        self.price=price
        self.history.append(price)
    def getPrice(self):
        return self.price
    def makeMove(self, mktBias, mo): 
        oldprice=self.price
        basemove=self.distribution()+mktBias
        self.price=self.price*(1.0+basemove)
        if mo:
            self.price=self.price+random.gauss(.5,.5)*self.lastchange ## To add the momentum in stocks
        if self.price<0.01:
            self.price=0.0
        self.history.append(self.price)
        self.lastchange=self.price-oldprice
    def showHistory(self,figNum):
        pylab.figure(figNum)
        pylab.plot(self.history)
        pylab.title('Closing Price, Test ' + str(figNum))
        pylab.xlabel('Day')
        pylab.ylabel('Price')

def unitTestStock():
    def runSim(stks, fig, mo):
        mean=0.0
        for s in stks:
            for d in range(numDays):
                s.makeMove(bias,mo)
            s.showHistory(fig)
            mean=mean+s.getPrice()
        mean=mean/float(numStks)
        pylab.axhline(mean)
    numStks=20
    numDays=100
    stks1=[]
    stks2=[]
    bias=0.0
    mo=False # momentum, if 
    for i in range(numStks):
        volatility=random.uniform(0,0.2)       
        d1=lambda: random.uniform(-volatility,volatility)
        d2=lambda: random.gauss(0.0,volatility/2.0)
        stks1.append(Stock(100.0,d1))
        stks2.append(Stock(100.0,d2))
    runSim(stks1,1,mo)
    runSim(stks2,2,mo)

unitTestStock()
pylab.show()

"""
def simMkt(mkt, numDays):
    endPrices = []
    for i in range(numDays):
        if i%(TRADING_DAYS_PER_YEAR/4) == 0:
            for s in mkt.getSectors():
                newBias = s.getOrigBias() + random.gauss(0, 2*s.getOrigBias())
                s.setBias(newBias)
            vals = mkt.moveAllStocks()
            vals = pylab.array(vals)
            mean = vals.sum()/float(len(vals))
            endPrices.append(mean)
    return endPrices


def plotValueOverTime(endPrices, title):
    pylab.plot(endPrices)
    pylab.title(title)
    pylab.xlabel('Days')
    pylab.ylabel('Price')

def plotDistributionAtEnd(mkt, title):
    prices = []
    for s in mkt.getStocks():
        prices.append(s.getPrice())
    pylab.hist(prices, bins = 20)
    pylab.title(title)
    pylab.xlabel('Last Sale')
    pylab.ylabel('Number of Securities')


    """
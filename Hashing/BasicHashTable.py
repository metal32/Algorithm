class Hashtable(object):
    def __init__(self):
        ## We create a list of list so that if for two different keys if there is same value we don't need to create list again and again 
        self.table=[[None]]*256
    def _gethash_value(self,key):
        total=0
        for i in range(len(key)):
            ## We dont just use sum of the characters only in the hash function as anagrams too has the same length
            total+=ord(key[i])*(7*i) 
        return (total*len(key)) % 256
    def insert(self,key):
        val=self._gethash_value(key)
        if self.table[val]==None:
            self.table[val]=key
        else:
            self.table[val].append(key)
            
    def delete(self, key):
        val = self._gethash_value(key)
        if self.table[val] != None:
            i = self.table[val].index(key)
            self.table[val][i] = None
        else:
            KeyError("key {key} can't be found.".format(key=key))

    def lookup(self,key):
        found=False
        val=self._gethash_value(key)
        found = key in self.table[val]
        return found

alist=['Ayush', 'Mittal', 'rishabh', 'Ashish']

hash=Hashtable()

for i in alist:
    hash.insert(i)

hash.delete(alist[1])

print hash.lookup(alist[1])
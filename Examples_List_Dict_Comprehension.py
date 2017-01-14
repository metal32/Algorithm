"""VERY IMPORTANT TRICK"""
#a=1
#b=a
#a=2
#print b ## AS stings and integers are immutable so b will remain 1 only.

#Now as lists are mutable 

#a=[1,2,3]
#b=a
#a[0]=4
#print b ##As lists are mutable so as we change the value of the object in which a is stored and b is also pointing to the same object the value of b[0] will also changes to 4.

a=[1,2,3]
b=a
##Now if you make a new list with empty set and assign it to "a" and then print b you will get the old list assigned to a
a=[]
print b

""" EXAMPLE OF LIST COMPREHENSION"""
###num=[1,2,3,4,5,6,7,8,9,10]
#my_list=[]
"""for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
        """
 
#my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
#print my_list

""" EXAMPLE OF DICTIONARY COMPREHENSION""" #DICTIONAIRIES ARE NOT ORDERED UNLIKE LISTS

#names= ["Ayush","Rishabh","Ashish","Viraj"]
#heroes=["Superman","Batman","Flash","Iron-Man"]
#print zip(names,heroes)

#my_dict={}
#for names,heroes in zip(names,heroes):
#    my_dict[names]= heroes
#print my_dict

# OR by dictionary comprehension
#my_dict_comprehension={name:hero for name,hero in zip(names,heroes)}
#print my_dict_comprehension

""" EXAMPLE OF SET COMPREHENSION
    A set is similar to list just that it has only unique values
"""
#number=[1,1,2,3,4,2,3,6,7,4,9,0,3,4,6,7]
#my_set=set()
#for n in number:
 #   my_set.add(n)
#print my_set

"""BY SET comprehension method"""
#my_set={n for n in number}
#print my_set

""" EXAMPLE OF GENERATORS"""
#num=[1,2,3,4,5,6,7,8,9,10]

#my_gen=(n*n for n in num)
#for i in my_gen:
#    print i

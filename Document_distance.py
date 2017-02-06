## Plagiarism
## Algorithm to math two files by taking the dot products of both the files and dividing by their magnitude

import string
import math
import sys
def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()

translation_table=string.maketrans(string.punctuation+string.uppercase," "*len(string.punctuation)+string.lowercase)

def get_words_from_text(L):
    text=text.translate(translation_table)
    word_list=text.split()
    return word_list


def countFreq(word_list):
    D={}
    for word in word_list:
        if D.has_key(word):
            D[word]=D[word]+1
        else:
            D[word]=1
    return D
def word_frequencies_for_file(file):
    text=read_file(file)
    word_list=get_words_from_text(text)
    freq_mapping=countFreq(word_list)
    return freq_mapping

def inner_product(D1,D2):
    sum=0.0
    for key in D1:
        if D2.has_key(key):
            sum=sum+D1[key]*D2[key]
    return sum

def vector_angle(D1,D2):
    numerator=inner_product(D1,D2)
    denominator=math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return math.acos(numerator/denominator)
def main():
    if len(sys.argv)!= 3:
        print "Usage: docdist1.py filename_1 filename_2"
    else:
        filename_1=sys.argv[1]
        filename_2=sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance=vector_angle(sorted_word_list_1,sorted_word_list_2)
        print "The distance between the documents is: %0.6f (radians)" %distance

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
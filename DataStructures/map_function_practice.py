#! /usr/bin/env python3

'''
Check if the given string of words can be formed from words present in the list of available words
Given a string array of M words and a list of N words. The task is to check if the 
given string of words can be formed from words present in the list.

'''

def match_words(dictionary, sentence):

    n = len(dictionary)
    sentence = sentence.split(' ')
    m = len(sentence)

    # make a map of the dictionary words with a count value
    mp = dict()
    print("word bank at start")
    print(mp)
    # making a map of quantities of each word available 
    for i in range(n): # for the number of items in the dictionary
        print("dictionary item " + str(i))
        mp[dictionary[i]] = mp.get(dictionary[i],0) + 1 
    print("word bank now looks like this")
    print(mp)


    for i in range(m):  # Now, for each item in the sentence
        print('sentence word ' + str(i) + ' is ' + sentence[i])
        if (mp.get([sentence[i]])):
            
            print("yea!!")
            mp[sentence[i]] -= 1
        else:
            return False

    return True



def main():
    dictionary = ["find", "a", "geeks", "all", "for", "on", "geeks", "answers", "inter", "geeks"]
    # dictionary = ["find", "a", "all", "for", "on", "geeks", "answers", "inter"]
    strIn = 'find all answers on geeks for geeks yellow'
    if match_words(dictionary,strIn):
        print('YES')
    else:
        print('No')




if __name__ == '__main__':
    main()

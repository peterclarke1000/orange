#! /usr/bin/env python3

class match_words:
    '''
    A class used to find match words in a sentence with words in a word bank or vocabulary. 
    An important distinction here is that if we're using word vocabularies then quantities of each words is infinite. 
    If we're using word banks then quantities of each word is finite.

    '''

    def __init__(self,wordBank=[],strIn="", vocab=False):
        self.wordBank = wordBank
        self.strIn = strIn
        self.lstIn = strIn.split(' ') if strIn != '' else []
        self.len_strIn = len(self.lstIn)
        self.vocab = vocab
        self.len_wordBank = len(wordBank)
        
        
    def print_variables(self):
        print("The strIn has " + str(self.len_strIn) + " words")
        print("The wordBank has " + str(self.len_wordBank) + " words")

    def match_words(self):
        # make a map of wordbank including count
        mp = dict()
        for i in range(self.len_wordBank):
            mp[self.wordBank[i]] = mp.get(self.wordBank[i],0) +1
        print(mp)    

        # next check to see if every word in sentence is available in the word bank
        for i in range(self.len_strIn):
            print('iteration ' + str(i) )
            print('word being processed: ' + str(self.lstIn[i]))
            print(" value: " + str(mp.get(self.lstIn[i])))
            if mp.get(self.lstIn[i]):
                if not self.vocab:
                    mp[self.lstIn[i]] -= 1
                    print(mp)
            else:
                print("in else part")
                print(mp)
                return False
        return True


dictionary = ["a", "geeks", "all", "for", "on", "geeks", "answers", "inter", "find"]
strIn = 'find geeks all answers on geeks for geeks'
# strIn = ''



MI = match_words(dictionary,strIn)
MI.print_variables()
if MI.match_words():
    print('YES,   you can make your sentence')
else:
    print('NOPE, your missing words')


        

        


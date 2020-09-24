class passwordcracker():
    def __init__(self):
        #print("I'm in class")
        self.substitutions={'s':'$', 'a': '4', 'l': '1', 'e': '3', 't': '7', 'i': '1', 'o': '0', 'b': '8', 'g': '9'}
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>', '<']
    def getPossibilities(self,word):
        possibilities = []
        possibilities.append(word)
        wordList = list(word)
        print(wordList)
        #


def main():
    #print("I'm in main")
    passwordcracker()
    baseWords=open("words.txt", "r").readlines()
    morethan10 = [word.rstrip('\n') for word in baseWords if len(word) >= 10]
    #print(len(morethan10))
    #print(morethan10[:10])
    hashFile=open("hash_2575198.txt","r").readlines()
    hashValues=[value.rstrip('\n') for value in hashFile ]
    #print(hashValues)
    passwordcracker().getPossibilities('TroubleShoot')


    

if __name__ == "__main__":
    main()
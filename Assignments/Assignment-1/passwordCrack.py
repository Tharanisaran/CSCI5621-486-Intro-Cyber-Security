from itertools import product
import hashlib
class passwordcracker():
    def __init__(self):
        #print("I'm in class")
        self.substitutions={'s':['$'], 'a': ['4'], 'l': ['1'], 'e': ['3'], 't': ['7'], 'i': ['1'], 'o': ['0'], 'b': ['8'], 'g': ['9']}
        for key in self.substitutions.keys():
            if key not in self.substitutions[key]:
                self.substitutions[key].append(key)
        #print(self.substitutions)

        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>', '<']
        self.symbolCharacters = []
        self.symbolCharacters = self.symbolCharacters + [str(a)+str(b) for a,b in product(range(0,10),self.symbols)]
        self.symbolCharacters = self.symbolCharacters + [str(a)+str(b) for a,b in product(self.symbols,range(0,10))]
        # print(self.symbolCharacters)

        self.shaSalt = hex(2575198)
    
    def getPossibilities(self,word):
        wordlist = []
        wordlist.append(word)
        wordlist.append(word.capitalize())
        allPossibilities = []
        wordPossibilities = []
        for nword in wordlist:
            for substitute in [zip(self.substitutions.keys(),character) for character in product(*self.substitutions.values())]:
                temp=nword
                for replacement in substitute:
                    temp=temp.replace(*replacement)
                wordPossibilities.append(temp)
        allPossibilities = allPossibilities + wordPossibilities
        symbolPossibilities = [str(a)+str(b) for a,b in product(wordPossibilities,self.symbolCharacters)]
        allPossibilities = allPossibilities + symbolPossibilities
        return allPossibilities

    def getPasswordHash(self,password):
        return hashlib.sha256(self.shaSalt.encode() + password.encode()).hexdigest()

def main():
    #print("I'm in main")
    #passwordcracker()
    baseWords=open("words.txt", "r").readlines()
    morethan10 = [word.rstrip('\n') for word in baseWords if len(word) >= 10]
    #print(len(morethan10))
    #print(morethan10[:10])
    hashFile=open("hash_2575198.txt","r").readlines()
    hashValues=[value.rstrip('\n') for value in hashFile ]
    #print(hashValues)
    run = passwordcracker()
    for word in morethan10:
        possibilities=run.getPossibilities(word)
        # print(len(possibilities))
        for password in possibilities:
            if run.getPasswordHash('4621_ctf{%s}'%(password)) in hashValues:
                print(password)
    

    

if __name__ == "__main__":
    main()
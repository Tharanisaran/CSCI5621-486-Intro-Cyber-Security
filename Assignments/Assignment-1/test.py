from itertools import product, combinations

substitutions={'s':'$', 'a': '4', 'l': '1', 'e': '3', 't': '7', 'i': '1', 'o': '0', 'b': '8', 'g': '9'}
# for key in substitutions.keys():
#     if key not in substitutions[key]:
#         substitutions[key].append(key)
# text = 'saletiobg'
# print(len(list(product(*substitutions.values()))))
# print(len(list(set(product(*substitutions.values())))))
# combiwords = []
# productSubstitutions = [list(zip(substitutions.keys(),character)) for character in product(*substitutions.values())]
# print(productSubstitutions)
# def find(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]

# word = 'saletioabg'
# allIndices = find(word,'a')
# replaceCombi = []
# for r in range(0,len(allIndices)+1):
#     replaceCombi.append(list(combinations(allIndices,r)))

# print(replaceCombi)
def getWordPossibilities(word,subs=[]):
    
    if not word:
        yield ''.join(subs)
    else:
        for i in [word[0], *substitutions.get(word[0], [])]:
            yield from getWordPossibilities(word[1:], subs+[i])
    print('Word: %s, Subs: %s'%(str(word),str(subs)))

print(list(getWordPossibilities('alpha')))
import string
#getting all possible ASCII characters
plain_text=string.printable.rstrip()
#getting the cipher text and substitutions
cipher_text=r'FI(:|tm}4?17a=+WcWoam1|5#~dS:2p9*i/x \uqx}oKB({J{8VU/<'
substitution='s:(/F!IM>gaot+1}{U0 "cp=W7r?%m_[TBKSG@8L.nXvy-,#C&\'hDVexbj2wlzf6~9PR;*uY]E`kNZ$q^5d)AOHi|J4\<3'
#print(plain_text)
# print(len(plain_text),len(substitution))
#creating a dictionary to store the mappings of plain text and substitutions
cipher_dict={}
if len(plain_text)==len(substitution):
    for i in range(len(plain_text)):
        cipher_dict[substitution[i]]=plain_text[i]
# print(cipher_dict)
flag = ''
#Mapping the cipher text to the values in dictionary
for letter in cipher_text:
    flag = flag + cipher_dict[letter]
#Printing the flag
print(flag)


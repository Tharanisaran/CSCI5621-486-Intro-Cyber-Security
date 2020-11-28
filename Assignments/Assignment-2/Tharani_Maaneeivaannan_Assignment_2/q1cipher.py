import string
#getting all possible ASCII characters
plain_text=string.printable.rstrip()
#getting the cipher text and substitutions
cipher_text=r'~[4M(&?}k<>,|E?_X`X^(2eEg)2ob}VoqLj#v(4[l\hX&Q]{2|TC'
substitution='mM4=~a[*.U{s&v`} ,_@;Xo>|D5hE?<q\']^T0Zx1)+L%due7Fn/:\WS2OBrfN6Q$j-gHtPyJRp8IAGclV#9zw3Yi(bk!C"'
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
print(plain_text)

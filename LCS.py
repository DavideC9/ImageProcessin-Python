# Python 3 program to find the stem
# of given list of words # function to find the stem (longest
# common substring) from the string array

from os import listdir
def findstem(arr):
# Determine size of the array
    n = len(arr)
# Take first word from array
# as reference


    s = arr[0]
    l = len(s)
    res = ""

for i in range(l):
    for j in range(i + 1, l + 1):
# generating all possible substrings
# of our reference string arr[0] i.e s
    stem = s[i:j]
    k = 1
    for k in range(1, n):
# Check if the generated stem is
# common to all words
    if stem not in arr[k]:
        break
# If current substring is present in
# all strings and its length is greater
# than current result
    if (k + 1 == n and len(res) < len(stem)):
        res = stem
    return res
stems=[]


#Driver Code 
if __name__ == "__main__":
    
    for s in range(50): 
        filepathTrovati= 'C:\\Users\\david\\Desktop\\Immagini\\legend\\Trovati\\' # percorso dove sono presenti gli Opcode trovati 
        fileTrovati = [f for f in listdir(filepathTrovati)] 
        righe=[] 
        
        with open(filepathTrovati + fileTrovati[s], encoding="utf-8") as f: 
            
            lines = f.readlines() 
            for l in lines: 
                riga=l.rstrip() 
                righe.append(str(riga)) 
                
        stems.append(findstem(righe)) 
        
        print(stems)
        print('\n') 

# porzione di codice per ritornare al valore originale dell’opcode 
# di={} 
# with open("simbolix.txt", encoding="utf-8") as f: 
#       for line in f: 
#           t = line.rstrip().split() 
#           di[t[1]]=t[0] 
# for s in stems: 
#   if s in di.values(): 
#       for k, v in di.items(): 
#               
#             if s == v: 
#                   print(str(k)) 
#                   print("k={} v={}".format(k, v))

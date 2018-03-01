import re
from urllib.request import urlretrieve

FILE_NAME = 'http_access_log.txt'
fh = open(FILE_NAME)

print("Calculating.....")
#counter vars
totalRequests = 0
janTotal = 0
febTotal = 0
marchTotal = 0
aprilTotal = 0
mayTotal = 0
juneTotal = 0
julyTotal = 0
augTotal = 0
sepTotal = 0
octTotal = 0
novTotal = 0
decTotal = 0
errorthreetotal = []
errorfourtotal = []
ERRORS = []
fileNames = {}

#expressions
janregex = r".* - - ([[]\d+.[J]+[a]+\S+)"
febregex = r".* - - ([[]\d+.[F]+[e]+\S+)"
marchregex = r".* - - ([[]\d+.[M]+[a]+[r]+\S+)"
aprilregex = r".* - - ([[]\d+.[A]+[p]+\S+)"
mayregex = r".* - - ([[]\d+.[M]+[a]+[y]+\S+)"
juneregex = r".* - - ([[]\d+.[J]+[u]+[n]+\S+)"
julyregex = r".* - - ([[]\d+.[J]+[u]+[l]+\S+)"
augregex = r".* - - ([[]\d+.[A]+[u]+\S+)"
sepregex = r".* - - ([[]\d+.[S]+[e]+\S+)"
octoregex = r".* - - ([[]\d+.[O]+\S+)"
novregex = r".* - - ([[]\d+.[N]+[o]+\S+)"
decregex = r".* - - ([[]\d+.[D]+[e]+\S+)"
nameregex = r".* - - .*[G]+[E]+[T] (\S+)"
errorthree = r".* - - .*[G]+[E]+[T] +\S+ +\S+ (3)"
errorfour = r".* - - .*[G]+[E]+[T] +\S+ +\S+ (4)"
fileregex = r".* - - .*[G]+[E]+[T] (\S+)"
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

#loops
for line in fh:
  parts = regex.split(line)
  if not parts or len(parts) < 7: 
    with open('error.txt', 'a') as the_file:
        the_file.write(line)    
 
  #pieces = re.search(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
  #filename = pieces.group(4)
  #if filename in fileNames:
  #  fileNames[filename] += 1
  #else:
  #  fileNames[filename] = 1
  totalRequests+=1

  
  #errors
  if re.search(errorthree, line):
    errorthreetotal.append(line) 
  if re.search(errorfour, line):
    errorfourtotal.append(line) 
    
  #months
  if re.search(janregex, line):
    janTotal+=1
    with open('january.txt', 'a') as the_file:
        the_file.write(line)    
  elif re.search(febregex, line):
    febTotal+=1
    with open('febuary.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(marchregex, line):
    marchTotal+=1
    with open('march.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(aprilregex, line):
    aprilTotal+=1
    with open('april.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(mayregex, line):
    mayTotal+=1
    with open('may.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(juneregex, line):
    juneTotal+=1
    with open('june.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(julyregex, line):
    julyTotal+=1
    with open('july.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(augregex, line):
    augTotal+=1
    with open('august.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(sepregex, line):
    sepTotal+=1
    with open('september.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(octoregex, line):
    octTotal+=1
    with open('october.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(novregex, line):
    novTotal+=1
    with open('november.txt', 'a') as the_file:
        the_file.write(line)        
  elif re.search(decregex, line):
    decTotal+=1
    with open('december.txt', 'a') as the_file:
        the_file.write(line)        

#print statements
print("Monthly Totals")
print("-------------------------")
print("")
print("January Total: ", janTotal)
print("Febuary Total: ", febTotal)
print("March Total: ", marchTotal)
print("April Total: ", aprilTotal)
print("May Total: ", mayTotal)
print("June Total: ", juneTotal)
print("July Total: ", julyTotal)
print("August Total: ", augTotal)
print("September Total: ", sepTotal)
print("October Total: ", octTotal)
print("November Total: ", novTotal)
print("December Total: ", decTotal)
print("")
print("Total Requests")
print("-------------------------")
print("")
print("Total Requests: ", totalRequests)
print("")
print("Error Messages")
print("-------------------------")
print("")
print("Percentage of the requests were not successful: ", (len(errorfourtotal)/totalRequests)*100 , "%")
print("Percentage of the requests were redirected elsewhere: ", (len(errorthreetotal)/totalRequests)*100 , "%")
print("")
print("File Frequency")
print("-------------------------")
print("")

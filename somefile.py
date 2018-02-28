FILE_NAME = 'http_access_log.txt'
fh = open(FILE_NAME)
import re

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
fileNames = []

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
    ERRORS.append(line)  
  else:
    file = re.search(regex, line)
    match = file.group(4)
    fileNames.append(match)
  totalRequests+=1

  
  #errors
  if re.search(errorthree, line):
    errorthreetotal.append(line) 
  if re.search(errorfour, line):
    errorfourtotal.append(line) 
    
  #months
  if re.search(janregex, line):
    janTotal+=1
  elif re.search(febregex, line):
    febTotal+=1
  elif re.search(marchregex, line):
    marchTotal+=1
  elif re.search(aprilregex, line):
    aprilTotal+=1
  elif re.search(mayregex, line):
    mayTotal+=1
  elif re.search(juneregex, line):
    juneTotal+=1
  elif re.search(julyregex, line):
    julyTotal+=1
  elif re.search(augregex, line):
    augTotal+=1
  elif re.search(sepregex, line):
    sepTotal+=1
  elif re.search(octoregex, line):
    octTotal+=1
  elif re.search(novregex, line):
    novTotal+=1
  elif re.search(decregex, line):
    decTotal+=1

#print statements
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
print("Total Requests: ", totalRequests)
print("Percentage of the requests were not successful: ", (len(errorfourtotal)/totalRequests)*100 , "%")
print("Percentage of the requests were redirected elsewhere: ", (len(errorthreetotal)/totalRequests)*100 , "%")

for p in fileNames: 
  print (p)
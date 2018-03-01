import re
import operator

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
searchList = []

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

for line in fh:
  #NUMBER 1
  totalRequests+=1
  
  #WRITES INCORRECT LINES TO ERROR.TXT 
  #NUMBER 5 AND 6
  parts = regex.split(line)
  if not parts or len(parts) < 7: 
    with open('error.txt', 'a') as the_file:
        the_file.write(line)        
  else:
    fileparts = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
    file = fileparts[4]
    if file not in searchList and file not in fileNames:
      searchList.append(file)
    elif file in searchList and file not in fileNames:
      fileNames[file] = 2
      searchList.remove(file)
    elif file not in searchList and file in fileNames:
      fileNames[file] += 1
      
  #NUMBER 2 MONTHLY CALCULATIONS
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
  
  #NUMBER 3 AND 4
  if re.search(errorthree, line):
    errorthreetotal.append(line) 
  if re.search(errorfour, line):
    errorfourtotal.append(line) 
    

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

maximum = max(fileNames.items(), key=operator.itemgetter(1))[0]
print ("Max file requested is", maximum, "which was requested", fileNames[maximum])
print ("Min files with one request", len(searchList), "and some examples include", searchList[1], searchList[5], searchList[10], searchList[20])

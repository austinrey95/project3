import re
import operator

from datetime import datetime
import os.path
from urllib.request import urlretrieve


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
if not os.path.isfile(LOCAL_FILE):
  local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
fh = open(LOCAL_FILE)


#counter vars

errorthreetotal = 0
errorfourtotal = 0
partList = []
errorCodes = []
errorLines = []
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
#janregex = r".* - - ([[]\d+.[J]+[a]+\S+)"
#febregex = r".* - - ([[]\d+.[F]+[e]+\S+)"
#marchregex = r".* - - ([[]\d+.[M]+[a]+[r]+\S+)"
#aprilregex = r".* - - ([[]\d+.[A]+[p]+\S+)"
#mayregex = r".* - - ([[]\d+.[M]+[a]+[y]+\S+)"
#juneregex = r".* - - ([[]\d+.[J]+[u]+[n]+\S+)"
#julyregex = r".* - - ([[]\d+.[J]+[u]+[l]+\S+)"
#augregex = r".* - - ([[]\d+.[A]+[u]+\S+)"
#sepregex = r".* - - ([[]\d+.[S]+[e]+\S+)"
#octoregex = r".* - - ([[]\d+.[O]+\S+)"
#novregex = r".* - - ([[]\d+.[N]+[o]+\S+)"
#decregex = r".* - - ([[]\d+.[D]+[e]+\S+)"
#nameregex = r".* - - .*[G]+[E]+[T] (\S+)"
#errorthree = r".* - - .*[G]+[E]+[T] +\S+ +\S+ (3)"
#errorfour = r".* - - .*[G]+[E]+[T] +\S+ +\S+ (4)"
#fileregex = r".* - - .*[G]+[E]+[T] (\S+)"
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

  #REQS = {1:0, 2:0............/}
  #entry_date = datetime.strptime(parts[1], "%d/%b/%Y")
  #REQS[r_date.month] += 1
 # print("total requests in jan {}".format(BY_MONTH[1]))

def main():
  global totalRequests
  global errorthreetotal
  global errorfourtotal
  for line in fh:
    totalRequests+=1
    parts = regex.split(line)
    partList.append(parts)
    if len(parts) < 6:
      errorLines.append(line)
    elif parts[6].startswith('3'):
      errorthreetotal += 1
    elif parts[6].startswith('4'):
      errorfourtotal += 1  
  print ("Total Requests: ", totalRequests)
  print (errorCodes)
  print ("Total 3xx errors is", errorthreetotal, "which is", (errorthreetotal/totalRequests)*100, "percentage of the total requests")
  print ("Total 4xx errors is", errorfourtotal, "which is", (errorfourtotal/totalRequests)*100, "percentage of the total requests")

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

import re
import operator
from datetime import datetime
import os.path
from urllib.request import urlretrieve
from collections import defaultdict

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
if not os.path.isfile(LOCAL_FILE):
  local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
fh = open(LOCAL_FILE)


#counter vars

errorthreetotal = 0
errorfourtotal = 0
partList = []
errorLines = []
totalRequests = 0
ERRORS = []
fileList = []
fileDict = {}
fileName = ''


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
  global fileName
  
  for line in fh:
    totalRequests+=1
    parts = regex.split(line)
    if not parts or len(parts) < 7: 
      errorLines.append(line)
    else:
      fileName = parts[4] 
      if parts[6].startswith('3'):
        errorthreetotal += 1
      elif parts[6].startswith('4'):
        errorfourtotal += 1  
      if fileName not in fileList and fileName not in fileDict:
        fileList.append(fileName)
      elif fileName in fileList and fileName not in fileDict:
        fileDict[fileName] = 1
        fileList.remove(fileName)
      elif fileName not in fileList and fileName in fileDict:
        fileDict[fileName] += 1
      
  print ("Total Requests: ", totalRequests)
  print ("Total errors in log:", len(errorLines), "which is", (len(errorLines)/totalRequests)*100, "percentage of all requests")
  print ("Total 3xx errors is", errorthreetotal, "which is", (errorthreetotal/totalRequests)*100, "percentage of the total requests")
  print ("Total 4xx errors is", errorfourtotal, "which is", (errorfourtotal/totalRequests)*100, "percentage of the total requests")
  maximum = max(fileDict.items(), key=operator.itemgetter(1))[0]
  print ("Max file requested is", maximum, "which was requested", fileDict[maximum])
  print ("Min files with one request", len(fileList), "and some examples include", fileList[1], fileList[5], fileList[10], fileList[20])
  
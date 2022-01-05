import hashlib
import requests
md5 = hashlib.md5()
inpat = input("enter file path: ")
file = open(inpat)
try:
  file = file.read()
except:
  print("Error: file cannot be read")
  try:
    quit()
  except:
    exec('^^^^')
md5.update(file)
hash = md5.digesthex()
if ".png" in inpat:
  finalhash = hash + ".png"
elif ".jpg" in inpat or "jpeg" in inpat:
  finalhash = hash + ".jpg"
elif ".gif" in inpat:
  finalhash = hash + ".gif"
else:
  print("could not find image file extension")
requests.post(f"https://assets.scratch.mit.edu/${finalhash}", file)

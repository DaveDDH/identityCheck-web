import json
from cryptography.fernet import Fernet

key = b'TJtbrjiYbnY0SMSehUWiWX5fPEymH7UlVo3GEHNhyXk='
f = Fernet(key)

def getKey(mId, db):
  if mId != None and mId != "":
    mKey = db.reference("keys/" + mId).get()
    print(mKey)
    if mKey != None and mKey != "":
      return "{\"key\":\"" + mKey + "\"}"
    else:
      return "{" + "}"
  else:
    return "{\"error\":\"" + "There were missing fields on the request." + "\"}"

def setKey(body, db):
  try:
    data = json.loads(body)
    email = data['email']
    mId = data['id']
    if email != None and email != "" and mId != None and mId != "":
      rData = json.loads(getKey(mId, db))
      if 'key' in rData.keys():
        return "{\"error\":\"" + "Key already existed." + "\"}"
      else:
        mKey = f.encrypt(str.encode(email))
        db.reference("keys/" + mId).set(mKey.decode())
        return mKey
    else:
      return "{\"error\":\"" + "There were missing fields." + "\"}"
  except:
    return "{\"error\":\"" + "There were missing fields." + "\"}"
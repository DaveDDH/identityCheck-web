import json

def getCount(mId, db):
  if mId != None and mId != "":
    mCount = db.reference("count/" + mId).get()
    print(mCount)
    if mCount != None and mCount != "":
      return "{\"count\":\"" + mCount + "\"}"
    else:
      return "{\"count\":\"" + str(0) + "\"}"
  else:
    return "{\"error\":\"" + "There were missing fields on the request." + "\"}"

def setCount(mId, db):
  if mId != None and mId != "":
    rData = json.loads(getCount(mId, db))
    if not 'count' in rData.keys():
      return "{\"error\":\"" + "There were missing fields on the request." + "\"}"
    else:
      mCount = str(int(rData['count']) + 1)
      db.reference("count/" + mId).set(mCount)
      return "{\"count\":\"" + mCount + "\"}"
  else:
    return "{\"error\":\"" + "There were missing fields." + "\"}"
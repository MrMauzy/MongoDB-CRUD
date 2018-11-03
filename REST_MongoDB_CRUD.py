import json
import pprint
from bson import json_util
from pymongo import MongoClient

connection = MongoClient()
db = connection['market']
collection = db['stocks']



def insert_document(document):
  try:
    collection.insert_one(document)
    print("Document was added successfully.")
  except:
    print("An issue has arised with your upload, please try again.")

def update_document(p1, p2, p3, p4):
  if (collection.find_one({p1 : p2})) != None:
    print("Original Document:\n")
    pprint.pprint(collection.find_one({p1 : p2}))
    collection.update_one(
      {p1 : p2},
      {
        "$set" : {
          p3 : p4
        }
      })
    print("Changed to:\n")
    pprint.pprint(collection.find_one({p1 : p2}))
  else:
      print("No Documents Found to Update")
 
def delete_document(p1, p2):
  if (collection.find_one({p1 : p2})) != None:
    print("Found this document and it is being deleted...\n")
    pprint.pprint(collection.find_one({p1 : p2}))
    collection.delete_one({p1 : p2})
    print("\n ..Delete Successfull..\n")
  else:
    print("No Documents found with this values.")

def main():
  stock1 = {"Ticker" : "ZZDZ",
            "Profit Margin" : .123,
            "Institutional Ownership" : 5568,
            "Current Ratio": 13,
            "Sector" : "Foods",
            "Payout Ratio" : "Monies",
            "Price" : 1,
            "50-Day High" : 55,
            "50-Day Low" : 2,
            "Volume" : 1}
  insert_document(stock1)
  pprint.pprint(collection.find_one({"Ticker": "ZZDZ"}))
  
  ticker = str(raw_input("What Stock Ticker Would you Like to Update?")).upper()
  vol = int(raw_input("What Volume Greater than 0 Would you like to Update?"))
  if(vol < 0):
    print("Please Enter a Valid Selection, Number Greater than 0.")
  else:
    update = dict(p1 = "Ticker", p2 = ticker, p3 = "Volume", p4 = vol)
    update_document(**update)
  
  print()
  
  tic = str(raw_input("Please Enter Stock Ticker to Delete from Documents.")).upper()
  deleteP = dict(p1 = "Ticker", p2 = tic)
  delete_document(**deleteP)
    
main()

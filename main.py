# c:/Users/bryan/Desktop/rasppi/venv/Scripts/Activate.ps1/Scripts/Activate.ps1
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import threading
import datetime

# Use the application default credentials
cred = credentials.Certificate('ServiceAccountKey.json')
firebase_admin.initialize_app(cred)

# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\bryan\Desktop\rasppi\ServiceAccountKey.json" (code for initial setting path)
# from google.cloud import firestore
db = firestore.client()


# doc_ref1 = db.collection('users4bryanlaptop').document('alovelace')
# doc_ref1.set({
#     'born': 1815,
# })
doc_ref1pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('1pm to 2pm')
doc_ref2pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('2pm to 3pm')
doc_ref3pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('3pm to 4pm')
doc_ref4pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('4pm to 5pm')
doc_ref5pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('5pm to 6pm')
doc_ref6pm = db.collection('SaracaHall').document(
    'Machine1').collection('Availability').document('6pm to 7pm')


# def on_snapshot(doc_snapshot, changes, read_time):
#     for doc in doc_snapshot:
#         test = doc.get('')
#         print(u'Received document snapshot: {}'.format(test))
#         return(test)


# def on_snapshot(document_snapshot, changes, read_time):
#     doc = document_snapshot
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))
# callback_done = threading.Event()

# # Create a callback on_snapshot function to capture changes

callback_done = threading.Event()

boolvalue = False


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        docDict = doc.to_dict()
        isbooked = docDict['isbooked']
        print(f'Received document snapshot: {doc.id},isbooked ={isbooked}')
        global boolvalue
        boolvalue = isbooked
    callback_done.set()


# doc_watch = doc_ref2pm.on_snapshot(on_snapshot)


# while True:
#     time.sleep(1)
#     print(boolvalue)

# doc_watch.unsubscribe()

# logic to check time before showing current ly available booking
while True:
    time.sleep(1)
    timenow = datetime.datetime.now()
    hournow = timenow.hour

    if (hournow in range(13, 14)):
        doc_watch = doc_ref1pm.on_snapshot(on_snapshot)
        print('1pmto2pm')
        print(boolvalue)
    elif (hournow in range(14, 15)):
        doc_watch = doc_ref2pm.on_snapshot(on_snapshot)
        print('2pmto3pm')
    elif(hournow in range(17, 18)):
        doc_watch = doc_ref5pm.on_snapshot(on_snapshot)
        print('5pm to6pm')
        print(boolvalue)
    elif(hournow in range(18, 19)):
        doc_watch = doc_ref6pm.on_snapshot(on_snapshot)
        print('6pm to 7pm')
        print(boolvalue)
    else:
        print("machine not available for booking")

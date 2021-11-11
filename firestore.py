import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# import json
import time
import threading
import datetime
import concurrent.futures
import logging
import RPi.GPIO as GPIO
import shutil
# import time
# 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)


# creds = open('ServiceAccountKey.json')
# # Use the application default credentials
cred =  credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\bryan\Desktop\rasppi\ServiceAccountKey.json" (code for initial setting path)
#from google.cloud import firestore
db = firestore.client()
doc_ref = db.collection(u'users2').document(u'alovelace')
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

  
    
    

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
       executor.map(on_snapshot, range(1))
    if (threading.active_count()>10):
           concurrent.futures.Future.cancel()


# doc_watch = doc_ref2pm.on_snapshot(on_snapshot)


# while True:
#     time.sleep(1)
#     print(boolvalue)

# doc_watch.unsubscribe()

def check1pm():
    time.sleep(1)
    doc_watch = doc_ref1pm.on_snapshot(on_snapshot)
    # global boolvalue1pm
    boolvalue1pm = boolvalue
    print(doc_watch)
    # # print('1pmto2pm')
    return(boolvalue1pm)


def check2pm():
    time.sleep(1)
    doc_watch = doc_ref2pm.on_snapshot(on_snapshot)
    # global boolvalue2pm
    boolvalue2pm = boolvalue

    # print('2pmto3pm')
    return(boolvalue2pm)


def check3pm():
    time.sleep(1)
    doc_watch = doc_ref3pm.on_snapshot(on_snapshot)
    # global boolvalue3pm
    boolvalue3pm = boolvalue

    # print('3pmto4pm')
    return(boolvalue3pm)


def check4pm():
    time.sleep(1)
    doc_watch = doc_ref4pm.on_snapshot(on_snapshot)
    # global boolvalue4pm
    boolvalue4pm = boolvalue

    # print('4pmto5pm')
    return(boolvalue4pm)
# logic to check time before showing current ly available booking

while True:
    time.sleep(2)
    timenow = datetime.datetime.now()
    interim = timenow.hour
    hournow = interim 
    print(threading.active_count())


    if (hournow == 13):
        doc_watch = doc_ref1pm.on_snapshot(on_snapshot)
        if boolvalue == True :
            GPIO.output(18, True)
            print('1pm to 2pm')
            print(boolvalue)
        if boolvalue == False :
            GPIO.output(18, False)
            print('1pm to 2pm')
            print(boolvalue)
    elif (hournow == 14):
        doc_watch = doc_ref2pm.on_snapshot(on_snapshot)
        if boolvalue == True :
            GPIO.output(18, True)
            print('2pm to 3pm')
            print(boolvalue)
        if boolvalue == False :
            GPIO.output(18, False)
           
            print('2pm to 3pm')
            print(boolvalue)
    elif (hournow == 15):
        doc_watch = doc_ref3pm.on_snapshot(on_snapshot)
        if boolvalue == True :
            GPIO.output(18, True)
           
            print('3pm to 4pm')
            print(boolvalue)
        if boolvalue == False :
            GPIO.output(18, False)
         
            print('3pm to 4pm')
            print(boolvalue)
    elif (hournow == 16):
        doc_watch = doc_ref4pm.on_snapshot(on_snapshot)
        if boolvalue == True :
            GPIO.output(18, True)
          
            print('4pm to 5pm')
            print(boolvalue)
        if boolvalue == False :
            GPIO.output(18, False)
         
            print('4pm to 5pm')
            print(boolvalue)
    elif (hournow == 18):
        doc_watch = doc_ref5pm.on_snapshot(on_snapshot)
        if boolvalue == True :
            GPIO.output(18, True)
          
            print('5pm to 6pm')
            print(boolvalue)
        if boolvalue == False :
            GPIO.output(18, False)
         
            print('5pm to 6pm')
            print(boolvalue)
        

    else:
        print("machine not available for booking")


# while True:
# 	if GPIO.input(25) :
# 		GPIO.output(18, False)
# 	else: 
# 		GPIO.output(18, True)



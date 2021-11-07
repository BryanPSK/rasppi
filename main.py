# c:/Users/bryan/Desktop/rasppi/venv/Scripts/Activate.ps1/Scripts/Activate.ps1
from main import *
import PySimpleGUI as sg
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import threading
import datetime

# Use the application default credentials
# cred = credentials.Certificate('ServiceAccountKey.json')
# firebase_admin.initialize_app(cred)
if not firebase_admin._apps:
    cred = credentials.Certificate('ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
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
# doc_ref5pm = db.collection('SaracaHall').document(
#     'Machine1').collection('Availability').document('5pm to 6pm')
# doc_ref6pm = db.collection('SaracaHall').document(
#     'Machine1').collection('Availability').document('6pm to 7pm')


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
# boolvalue1pm = False
# boolvalue2pm = False
# boolvalue3pm = False
# boolvalue4pm = False
# boolvalue5pm = False
# boolvalue6pm = False


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        docDict = doc.to_dict()
        isbooked = docDict['isbooked']
        # print(f'Received document snapshot: {doc.id},isbooked ={isbooked}')
        global boolvalue
        boolvalue = isbooked
    callback_done.set()


# doc_watch = doc_ref2pm.on_snapshot(on_snapshot)


# while True:
#     time.sleep(1)
#     print(boolvalue)

# doc_watch.unsubscribe()

# logic to check time before showing current ly available booking
# def timecheck():
#     time.sleep(1)
#     timenow = datetime.datetime.now()
#     hournow = timenow.hour

#     if (hournow == 13):
#         doc_watch = doc_ref1pm.on_snapshot(on_snapshot)
#         boolvalue1pm = boolvalue

#         print('1pmto2pm')
#         return(boolvalue1pm)
#     elif (hournow == 14):
#         doc_watch = doc_ref2pm.on_snapshot(on_snapshot)
#         boolvalue2pm = boolvalue

#         print('2pmto3pm')
#         print(boolvalue2pm)
#     elif (hournow == 15):
#         doc_watch = doc_ref3pm.on_snapshot(on_snapshot)
#         boolvalue3pm = boolvalue

#         print('3pmto4pm')
#         print(boolvalue3pm)
#     elif (hournow == 16):
#         doc_watch = doc_ref4pm.on_snapshot(on_snapshot)
#         boolvalue4pm = boolvalue

#         print('4pmto5pm')
#         print(boolvalue4pm)
#     elif(hournow == 17):
#         doc_watch = doc_ref5pm.on_snapshot(on_snapshot)
#         boolvalue5pm = boolvalue

#         print('5pm to 6pm')
#         print(boolvalue5pm)
#     elif(hournow == 18):
#         doc_watch = doc_ref6pm.on_snapshot(on_snapshot)
#         boolvalue6pm = boolvalue

#         print('6pm to 7pm')
#         print(boolvalue6pm)
#     else:
#         print("machine not available for booking")


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


# def check5pm():
#     time.sleep(1)
#     doc_watch = doc_ref5pm.on_snapshot(on_snapshot)
#     global boolvalue5pm
#     boolvalue5pm = boolvalue

#     # print('5pmto6pm')
#     return(boolvalue5pm)


# def check6pm():
#     time.sleep(1)
#     doc_watch = doc_ref6pm.on_snapshot(on_snapshot)
#     global boolvalue6pm
#     boolvalue6pm = boolvalue

#     # print('6pmto7pm')
#     return(boolvalue6pm)


# while True:
#     # check all time and pass boolvalue for each time to global
#     # take global bool and display on gui
#     if (check2pm() == True):
#         print('lmao')
#     else:
#         print('maolao')
# while True:
#     check1pm()
#     check2pm()
#     check3pm()
#     check4pm()

# layout = [[
#     sg.Frame('Saraca Hall machine A', [[
#           sg.Text('1pm to 2pm booked:'),
#           sg.Text(boolvalue),
#           sg.Column(sg.Text('hi'))
#           ]],

#     ),
# ]]
def mastercheck1pm():

    time.sleep(1)
    isbooked = db.collection('SaracaHall').document(
        'Machine1').collection('Availability').document('1pm to 2pm').get().get('isbooked')
    return(isbooked)


def mastercheck2pm():
    time.sleep(0.1)
    isbooked = db.collection('SaracaHall').document(
        'Machine1').collection('Availability').document('2pm to 3pm').get().get('isbooked')
    return(isbooked)


def mastercheck3pm():
    time.sleep(0.1)
    isbooked = db.collection('SaracaHall').document(
        'Machine1').collection('Availability').document('3pm to 4pm').get().get('isbooked')
    return(isbooked)


def mastercheck4pm():
    time.sleep(0.1)
    isbooked = db.collection('SaracaHall').document(
        'Machine1').collection('Availability').document('4pm to 5pm').get().get('isbooked')
    return(isbooked)


# layout = [[sg.Column([[sg.Text('Timeslot'), sg.Text('booked')],
#                       [sg.Text('1pmto2pm'), sg.Text(mastercheck1pm())],
#                       [sg.Text('2pmto3pm'), sg.Text(mastercheck2pm())],
#                       [sg.Text('3pmto4pm'), sg.Text(mastercheck3pm())],
#                       [sg.Text('4pmto5pm'), sg.Text(mastercheck4pm())],

#                       ])],
#           [sg.Button('test'), sg.Button('Exit')]]

# # Create the window
# window = sg.Window("Saraca Hall Machine A", layout)


# # Create an event loop
# while True:

#     event, values = window.read()

#     # End program if user closes window or
#     if event == 'test':
#         event, values = window.read()
#         window.Refresh()
#     # presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break

# window.close()
# # while True:

# print(mastercheck2pm())

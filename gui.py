import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Text, popup
from firestore1 import *
from PIL import Image

#img = Image.open('/home/pi/Desktop/michelle/pesula.png')

sg.theme('LightGreen3')

# layout = [[
#     sg.Frame('Saraca Hall machine A', [[
#           sg.Text('1pm to 2pm booked:'),
#           sg.Text(boolvalue),
#           sg.Column(sg.Text('hi'))
#           ]],

#     ),
# ]]
layout1 = [[sg.Column([[sg.Text('Timeslot', font=('bold', 50), size=(10, 1), justification='center'), sg.Text('Booked', font=('bold', 50), size=(10, 1), justification='center')],
                       [sg.Text('1pm to 2pm', font=(150), size=(40, 1), justification='center'), sg.Text(
                           check1pm(), background_color='white', font=(150), size=(40, 1), justification='center')],
                      [sg.Text('2pm to 3pm', font=(100), size=(40, 1), justification='center'), sg.Text(
                          check2pm(), background_color='white', font=(100), size=(40, 1), justification='center')],
                      [sg.Text('3pm to 4pm', font=(100), size=(40, 1), justification='center'), sg.Text(
                          check3pm(), background_color='white', font=(100), size=(40, 1), justification='center')],
                      [sg.Text('4pm to 5pm', font=(100), size=(40, 1), justification='center'), sg.Text(
                          check4pm(), background_color='white', font=(100), size=(40, 1), justification='center')],
                       [sg.Text(''), sg.Text('')]

                       ])],
           ]

layout2 = [[sg.Text('Enter your session OTP', font=('bold', 20), size=(100, 1), justification='center')],
           [sg.InputText(key='password', font=(100), size=(
               100, 1), justification='center')],
           [sg.Button('Login', font=('bold', 20), size=(100, 1))],
           [sg.Image('pesula.png')]
           ]

layout = [[sg.Column(layout1, key='bookings', visible=True),
           sg.Column(layout2, key='auth', visible=False)],
          [sg.Button('Check Bookings', font=('bold', 20), size=(21, 1)), sg.Button('Start session', font=('bold', 20), size=(25, 1))]]
# Create an event loop
window = sg.Window("Saraca Hall Machine A", layout,
                   location=(0, 0), size=(800, 600)).Finalize()
# window.Maximize()

while True:

    # Create the window

    event, values = window.read()

    if event == 'Start session':
        window[f'bookings'].update(visible=False)
        window[f'auth'].update(visible=True)
    if event == 'Check Bookings':
        window[f'bookings'].update(visible=True)
        window[f'auth'].update(visible=False)
    if event == 'Login' and values['password'] == '123':
        sg.PopupAutoClose(
            'Login successful, wash session will begin in 10 seconds', title='Success', font=(80))
        window[f'bookings'].update(visible=True)
        window[f'auth'].update(visible=False)
    if event == 'Login' and values['password'] != '123':
        sg.PopupAutoClose('Login unsuccessful. Please check your OTP and try again',
                          title='Unsuccessful', font=(80))
        window[f'bookings'].update(visible=False)
        window[f'auth'].update(visible=True)

    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

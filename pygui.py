import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Text, popup
from main import *

# layout = [[
#     sg.Frame('Saraca Hall machine A', [[
#           sg.Text('1pm to 2pm booked:'),
#           sg.Text(boolvalue),
#           sg.Column(sg.Text('hi'))
#           ]],

#     ),
# ]]
layout1 = [[sg.Column([[sg.Text('Timeslot'), sg.Text('booked')],
                      [sg.Text('1pmto2pm'), sg.Text(mastercheck1pm())],
                      [sg.Text('2pmto3pm'), sg.Text(mastercheck2pm())],
                      [sg.Text('3pmto4pm'), sg.Text(mastercheck3pm())],
                      [sg.Text('4pmto5pm'), sg.Text(mastercheck4pm())],


                       ])],
           ]

layout2 = [[sg.Text('Enter your session OTP')],
           [sg.InputText(key='password')],
           [sg.Button('Login')]
           ]

layout = [[sg.Column(layout1, key='bookings', visible=True),
           sg.Column(layout2, key='auth', visible=False)],
          [sg.Button('Check Bookings'), sg.Button('Start session')]]
# Create an event loop
window = sg.Window("Saraca Hall Machine A", layout, size=(300, 200))
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
            'login successful, wash session will begin in 10 seconds', title='Success')
        window[f'bookings'].update(visible=True)
        window[f'auth'].update(visible=False)
    if event == 'Login' and values['password'] != '123':
        sg.PopupAutoClose('login unsuccessful. Please try again',
                          title='Unsuccessful')
        window[f'bookings'].update(visible=False)
        window[f'auth'].update(visible=True)

    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

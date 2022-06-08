import PySimpleGUI as sg


class MoleasyGUI:
    def __init__(self):
        # Layout
        layout = [
            [sg.Button('Button')]
        ]
        
        # Window
        window = sg.Window('Moleasy').layout(layout)
        
        # Data extracted
        self.button, self.value = window.Read()

    def start(self):
        print('Test')


window = MoleasyGUI()
window.start()
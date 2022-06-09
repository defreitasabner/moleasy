import PySimpleGUI as sg


class MoleasyGUI:
    def __init__(self):
        sg.theme('DarkGrey13')
        # Layout
        layout = [
            [sg.Output(size=(50, 10), key='output_log')],
            [sg.Text('Input:'), sg.In(size=(33)), sg.FileBrowse()],
            [sg.Text('Output:'), sg.In(size=(32)), sg.FileBrowse()],
            [sg.Radio('Fasta (.fas)', 'file_converter'),
             sg.Radio('Phyllip (.phy)', 'file_converter'),
              sg.Radio('Nexus (.nex)', 'file_converter'),
               sg.Button('Convert', key='convert_file')]
        ]
        
        # Window
        self.window = sg.Window('Moleasy').layout(layout)
        
        # Data extracted
        self.event, self.values = self.window.Read()

    def start(self):
        while True:
            if self.event == sg.WIN_CLOSED or self.event == 'Exit':
                break
            if self.event == 'convert_file':
                print('Converting...')
            elif self.event == 'concat_file':
                print('Concat...')
        self.window.close()

window = MoleasyGUI()
window.start()
# pdf_viewer.py

import PySimpleGUI as sg
import os.path

def f(pdf_files, outfolder):
    from pathlib import Path
    from PyPDF2 import PdfFileMerger
    pdf_merger = PdfFileMerger()
    for path in pdf_files: pdf_merger.append(path)
    with Path(outfolder + "merged-file.pdf").open(mode="wb") as output_file: pdf_merger.write(output_file)

#sg.theme('DarkAmber')

# First the window layout

file_list_column = [
    [
        sg.Text("PDF Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Text("Output Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-OUTFOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Merge"),
    ],
]



pdf_list_column = [
    [sg.Text(size=(40, 1), key="-TOUT-")],
]


# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("PDF Files Selector", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".pdf"))
        ]
        window["-FILE LIST-"].update(fnames)
    if event == "-OUTFOLDER-":
        outfolder = values["-OUTFOLDER-"]

    if event == 'Merge':
        #pdf_files = os.path.abspath(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]))
        pdf_files = [folder + s for s in pdf_files]
        try:
          f(pdf_files,outfolder)
        except:
          pass

window.close()
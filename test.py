import pandas as pd, numpy as np
import os, time
import cv2
from pytesseract import pytesseract
import docx, re, PyPDF2 as pdf
import string
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import multiprocessing as mp
import sys

'''
AutomText. Una herramienta orientada al procesamiento de macrodatos.
Juan Esteban Urrea C.
Sebastian Espinosa Soto.
Antony Flores.
'''


class Data:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)
        self.files = os.listdir(os.getcwd())
        self.dfCreate = []  # Atributo que contiene la cantidad total de coincidencias
        self.dfCreate1 = []  # Atributo que contiene la cantidad de coincidencias por línea
        self.tesserPath = r'C:\Users\jumao\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        _, self.image = self.camera.read()

    def find(self, mode):

        fileExt = input("Ingrese la extensión del archivo: ")
        start = time.perf_counter()

        archivos = []
        if fileExt == "txt":
            if mode == "m":

                for file in self.files:  # Abrir archivos de la dirección actual
                    if file.endswith(".txt"):
                        archivos.append(open(file=file, mode='r'))

                t = []
                for texts in range(0, len(archivos)):  # Lectura de archivos

                    t.append(archivos[texts].read())

                res = []  # lista sin puntuación

                for i in range(len(archivos)):  # Separar palabras de textos en listas excluyendo la puntuación.
                    res.append(re.sub('[' + string.punctuation + ']', '', t[i]).split(" "))

                entry = input("Por favor, ingrese una palabra clave: ")

                name = []
                for i in range(len(t)):
                    name.append(archivos[i].name)  # get all file names
                print(name)

                for i in range(len(archivos)):
                    print(20 * "-" + f"{name[i]}" + 20 * "-")
                    for lines in t[i].split("\n"):
                        if entry in lines:
                            print(lines)

                finish = time.perf_counter()
                print(f"Se terminó el proceso en {round(finish - start, 2)}")

        elif mode == "o":
            start = time.perf_counter()
            name = input("Por favor, ingrese el nombre del archivo: ")
            file = open(name + '.txt', mode='r', encoding='utf-8')
            t = file.read()
            res = re.sub('[' + string.punctuation + ']', '', t).split()
            entry = input("Por favor, ingrese una palabra clave: ")
            lines_list = t.split("\n")
            for lines in lines_list:
                if entry in lines:
                    print(lines)
        finish = time.perf_counter()
        print(f"Se terminó el proceso en {round(finish - start, 2)}")

        if fileExt == "doc":
            start = time.perf_counter()
            documentsFiles = []
            documentsOpen = []
            documentsName = []
            n = []
            documentText = []
            for docs in self.files:
                if docs.endswith(".docx"):
                    documentsFiles.append(docs)
            for openDoc in documentsFiles:  # Consiguiendo el nombre del documento
                documentsOpen.append(docx.Document(openDoc))
            for name in documentsFiles:
                if name.endswith(".docx"):
                    documentsName.append(name)
            for i in range(len(documentsName)):
                n.append(list(os.path.splitext(documentsName[i])))
            for i in range(len(documentsName)):
                n[i].pop(1)

            keyword = input("Ingrese una palabra clave: ")
            text = []
            for i in range(len(n)):
                for paragraph in documentsOpen[i].paragraphs:
                    documentText.append(paragraph.text)

            for i in range(len(n)):
                print(20 * "-" + f"{n[i]}" + 20 * "-")
                for line in documentText[i].split("\n"):
                    if keyword in line:
                        print(line)
            finish = time.perf_counter()
            print(f"Se terminó el proceso en {round(finish - start, 2)}")
        '''
        if fileExt == "pdf":
            f = []
            lec = []
            pag = []
            text = []
            pdfFile = open('aeu.pdf', 'rb')

            # create PDFFileReader object to read the file
            pdfReader = pdf.PdfReader(pdfFile)
            p = pdfReader.pages[50]


            print("- - - - - - - - - - - - - - - - - - - -")
            print("Info: " + p.extract_text())


            # close the PDF file object
            pdfFile.close()
            
            for files in self.files:
                if files.endswith(".pdf"):
                 f.append(open(files, mode='rb'))
            for i in range(len(f)):
                 lec.append(pdf.PdfReader(f[i]))
            for i in range(len(f)): #Páginas del PDF
                pag.append(lec[i].pages[5])
            for i in range(len(f)):
                text.append(pag[i].extract_text())
            print(text)

            entry = input("Ingrese la palabra que desea buscar: ")
            for i in range(len(f)):
              print(20 * "-" + f"{f[i].name}" + 20 * "-")
              for lines in text[i].split("\n"):
                  if entry in lines:
                      print(lines)

               '''

    def compare(self):
        with open("prueba.txt", mode='r') as f1:
            t1 = f1.read()
        with open("prueba2.txt", mode='r') as gb:
            t2 = gb.read()
        lines1 = t1.split("\n")
        words1 = " ".join(lines1).split(" ")
        lines2 = t2.split("\n")
        words2 = " ".join(lines2).split(" ")

        print(lines2[0])
        print(f"Los textos tienen {len(set(words1) & set(words2))} palabras en común")
        time.sleep(1)
        if len(lines1) <= len(lines2):
            for i in range(len(lines2)):
                print(
                    f"En la línea #{i + 1} se encontraron {len(set(lines1[i].split(' ')) & set(lines2[i].split(' ')))} coincidencias")
        elif len(lines1) >= len(lines2):
            for i in range(len(lines1)):
                print(
                    f"En la línea #{i + 1} se encontraron {len(set(lines1[i].split(' ')) & set(lines2[i].split(' ')))} coincidencias")

    def filedates(self):

        archivos = []
        f = []
        date = []
        #  entry = input("Ingrese una fecha: ")

        for i in range(0, len(self.files)):  # Guardar todos los archivos
            archivos.append(open(file=self.files[i], mode='r'))

        for i in range(0, len(self.files)):
            f.append(archivos[i])

        for i in range(0, len(self.files)):  # Fechas
            date.append(time.ctime(os.path.getctime(f[i].name)))

        for i in range(0, len(self.files)):
            #     if entry in date[i]:
            pass
        print(date[4])

    def createfile(self):
        entry = input("<<")
        d = input("¿Desea imprimir el archivo?")
        with open("probando.txt", mode='w') as f:
            f.write(entry)
        with open("probando.txt", mode='r') as f:
            t = f.read()

        if d == 'Y':
            print(t)
        elif d == 'N':
            pass
        else:
            pass

    def enumerate_files(self):
        entry = input("¿Desea cambiar ennumerar el nombre de sus archivos?")
        files, names = [], []
        if entry == 'Y':
            for i in self.files:
                if i.endswith(".log"):
                    files.append(open(i))
            for i in range(len(self.files)):
                names.append(files[i].name)
            print("Renombrando archivos...")

            for i in range(len(self.files)):
                files[i].close()
                os.rename(names[i], f"File #{str(i + 1)}.log")
            print("Se ha terminado de renombrar todos los archivos.")
        elif entry == "N":
            pass
        else:
            pass

    def cam_capture(self):

        while True:
            cv2.imshow('AutomText Scan', self.image)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite('test.jpg', self.image)
                break
        self.camera.release()
        cv2.destroyAllWindows()
        self.image_scan()

    def image_scan(self):
        pytesseract.tesseract_cmd = self.tesserPath
        path = 'test.jpg'
        text = pytesseract.image_to_string(Image.open(path))
        print(text[:-1])

    def dataframe(self, f1, gb):
        # Dataframe #1: Contiene la cantidad de palabras coincidentes por línea
        f = []
        text = []
        names = []
        words1, words2 = [], []
        j = 0
        entry = [f1, gb]

        for files in entry:
            if files.endswith(".txt"):
                f.append(open(files))
        for i in range(len(f)):
            names.append(f[i].name)

        for i in range(len(f)):
            text.append(f[i].read())

        lines1 = text[0].split("\n")
        lines2 = text[1].split("\n")
        words1 = " ".join(lines1).split(" ")
        words2 = " ".join(lines2).split(" ")
        rows = []
        if lines1 <= lines2:
            for i in range(len(lines2)):
                rows.append("Línea #" + str(i + 1))
        elif lines1 >= lines2:
            for i in range(len(lines1)):
                rows.append("Línea #" + str(i + 1))

        self.dfCreate = [len(set(words1) & set(words2))]  # Cantidad total de palabras coincidentes
        for i in range(len(lines2)):
            self.dfCreate1.append(len(set(lines1[i].split(' ')) & set(lines2[i].split(' '))))
        df = pd.DataFrame(self.dfCreate1, columns=[f"Coincidencias entre {names[0]} y {names[1]}"])

        df.index = rows

        print(df)
        del df


class Window(QWidget, Data):
    def __init__(self):
        super(Window, self).__init__()
        win = QMainWindow
        self.setGeometry(250, 250, 800, 800)
        self.setWindowTitle("AutomText")
        self.setWindowIcon(QIcon("asd.png"))
        self.name = ""

    def not_files_loaded(self):
        QMessageBox.about(self, "Error", "No has subido ningún archivo en las ranuras.")

    def init_ui(self):
        boxv = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()
        grid2 = QFormLayout()
        hbox2 = QGridLayout()
        self.setLayout(boxv)
        functions = ["Búsqueda de texto", "Ennumerar archivos", "Búsqueda de texto"]
        logo = QPixmap('asd.png')
        image = QLabel()
        image.setPixmap(logo)
        f1 = QFrame()
        gb = QGroupBox("¡Configura tu búsqueda!")
        gb.setFont(QFont("Arial", 15))
        f1.setLayout(grid)
        gb.setLayout(grid2)

        Font = QFont("Times", 20)
        font_title = QFont("Arial", 25)

        title = QLabel("AutomText")
        lb1 = QLabel("Elija su función:")
        lb_word = QLabel("Ingrese una palabra clave")
        cb1 = QComboBox()
        cb2 = QComboBox()

        cb1.addItems(functions)
        #  for num in range(5):
        #     cb2.addItem(str(num + 1))

        cb1.adjustSize()
        #   cb2.adjustSize()
     #   if cb1.currentText() == "Búsqueda de texto":

        title.setFont(font_title)
        lb1.setFont(Font)
        # lb2.setFont(Font)
        lb1.setStyleSheet("foreground-color: red")

        grid.addWidget(title, 0, 0)
        grid.addWidget(image, 0, 1)
        grid2.addRow(lb1, cb1)
        #  grid2.addRow(lb2, cb2)

        file_slots = QGroupBox("Ranuras de archivo")
        file_slots.setFont(QFont("Arial", 15))

        previous_value = 0

        # current_value = int(cb2.currentText())

        button3 = QPushButton("Comenzar")
        button3.clicked.connect(w.not_files_loaded)

        # print(w.open_file)

        tab = QTabWidget()
        tab.setFont(QFont("Arial", 15))
        default = fileSlot()

        for i in range(4):
            tab.addTab(fileSlot(), f"Ranura {i + 1}")

        boxv.addWidget(f1)
        boxv.addWidget(gb)
        boxv.addWidget(tab)
        boxv.addWidget(button3)


class fileSlot(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # WIDGETS DE LAS RANURAS
        self.name = 'Elija un archivo:'
        self.boxv2 = QVBoxLayout()
        self.setLayout(self.boxv2)
        self.image = QPixmap('carpeta.png')
        self.text = QLabel(self.name)
        self.text2 = QLabel("O... ¡Escanee un documento!")
        self.button = QPushButton("Abrir")
        self.button2 = QPushButton("Escanear")
        self.smaller = self.image.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.file_font = QFont("Arial", 18)
        self.text.setFont(self.file_font)

        def open_file():
            self.name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "",
                                                       "Archivos de texto (*.txt);; Archivos .log (*.log)")
            lastModified = QFileInfo(self.name)

            filename = QFileInfo(self.name).fileName()
            if self.name:
                self.text.setText(f"--{filename}--")
                self.boxv2.removeWidget(self.button)

        self.button.clicked.connect(open_file)

        self.icon = QLabel()
        self.icon.setPixmap(self.smaller)
        self.boxv2.addWidget(self.icon)
        self.boxv2.addWidget(self.text)
        self.boxv2.addWidget(self.button)
        self.boxv2.addWidget(self.text2)
        self.boxv2.addWidget(self.button2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.init_ui()
    w.show()
    sys.exit(app.exec())

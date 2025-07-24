
import PyPDF2
import os

merger = PyPDF2.pdfMerger()

lista_arquivos = os.listdir('arquivos')
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'arquivos/{arquivo}')

merger.write('PDF Final.pdf')        
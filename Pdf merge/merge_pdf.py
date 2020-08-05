import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() 
    for pdf in pdf_list:
        merger.append(pdf) 
    merger.write('Output.pdf') # Specify the name of the output pdf file

if __name__ == "__main__":
    pdf_combiner(inputs)


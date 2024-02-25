import os
import sys
import argparse
import glob
try:
    from pypdf import PdfWriter
except Exception as error:
    print("error happened: %s" % error)
    os.system("pip3 install pypdf")
    

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="please provide the directory or the names of PDF file")
    parser.add_argument('--directory', '-d', type=str, help='directory')
    args = parser.parse_args()

    merger = PdfWriter()
    directory = args.directory or ''
    
    if directory != '':
        file_list = glob.glob(directory + '/*.pdf' )
        print("pdf files to be merged: %s" % file_list)

        for file in file_list:
            merger.append(file)
        merger.write('merged_pdf.pdf')
        merger.close()
        print("pdf merged successfully")
    else:
        print("please input the directory")
        sys.exit(1)
        
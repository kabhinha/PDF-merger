try:
    import sys
    import os
    import PyPDF2
except ModuleNotFoundError:
    import subprocess
    subprocess.run("pip install PyPDF2")


def collector(dirr):
    splitext = os.path.splitext
    listdir = os.listdir
    files = []
    for x in listdir(dirr):
        if splitext(x)[1]=="":
            for i in listdir(f"{dirr}\{x}"):
                if splitext(i)[1]=="":
                    for j in listdir(f"{dirr}\{x}\{i}"):
                        if splitext(j)[1]==".pdf":
                            files.append(f"{dirr}\{x}\{i}\{j}")
                elif splitext(i)[1]==".pdf":
                    files.append(f"{dirr}\{x}\{i}")
        elif splitext(x)[1]==".pdf":
            files.append(f"{dirr}\{x}")
    return files

def merger(plist, new_file):
    merger = PyPDF2.PdfFileMerger()
    for pdf in plist:
        merger.append(pdf)
    merger.write(f"{new_file}.pdf")


ins =  sys.argv[1:]
root_directory = ins[0]
super_file = ins[1]
files = collector(root_directory)
print("Merged successfully...!")

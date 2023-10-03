# userfile.py
# Program do generowania nazw uzytkowników w serii.

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("Program do generowania nazw użytkowników")
    print("z pliku tekstowego.")

    # zdobądz nazwy plików
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    # otwieranie plików
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # przetwarzanie każdego wersu pliku wejściowego
    for line in infile:
        # wez imie i nazwisko z wersu
        first, last = line.split()
        # stworz nazwe uzytkownika
        uname = (first[0]+last[:7]).lower()
        # zapisz w pliku wyjsciowym
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Nazwy użytkownika zostały zapisane do pliku", outfileName)

main()


        

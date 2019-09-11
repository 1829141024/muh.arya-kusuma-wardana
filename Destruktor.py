class MyFile(object):
    def __init__(self, namafile):
        print("  /=======================================\ ")
        print(" | SELAMAT DATANG DI PROGRAM BUKA PARAGRAF | ")
        print("  \=======================================/")                              
        print("\nMembuka file %s... \n" % namafile)
        self.file = open(namafile)
    def __del__(self):
        print("\Menutup file...")
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    f = MyFile ("G:/BAHAN KULIAH/SEMESTER 3/Pemrograman Lanjut/pertemuan 3/readme.txt")
    f.bacadata()
if __name__=="__main__":
    main()

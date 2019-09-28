class FakultasTeknik:
    def __init__(self,Universitas, Fakultas, TahunAjar):
        self.un = Universitas
        self.fa = Fakultas
        self.ta = TahunAjar

    def CetakData(self):
        print('Universitas   : ',self.un)
        print('Fakultas      : ',self.fa)
        print('Tahun Ajaran  : ',self.ta)

class TeknikKomputer(FakultasTeknik):
    def __init__(self,Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self,Universitas, Fakultas, TahunAjar)
    def CetakData(self):
        print('Teknik Komputer')
        print('Universitas   : ', self.un)
        print('Fakultas      : ', self.fa)
        print('Tahun Ajaran  : ', self.ta)
        print('Jumlah Angkatan di prodi Teknik Kompter adalah', self.JA)
     

class Mekatronika(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Pendidikan Vokasi Mekatronika')
        print('Universitas   : ', self.un)
        print('Fakultas      : ', self.fa)
        print('Tahun Ajaran  : ', self.ta)
        print('Jumlah Angkatan di prodi Teknik Kompter adalah', self.JA)

class PTIK(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan, Jurusan):
        self.JA = JumlahAngkatan
        self.J = Jurusan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Pendidikan Teknik Informatika & Komputer')
        print('Universitas   : ', self.un)
        print('Fakultas      : ', self.fa)
        print('Jurusan       : ', self.J)
        print('Tahun Ajaran  : ', self.ta)
        print('Jumlah Angkatan di prodi Teknik Kompter adalah', self.JA)
       
def main():
    a = FakultasTeknik('UNM', 'Teknik', 2017, )
    a.CetakData()

    del a

    a = TeknikKomputer('UNM', 'Teknik', 2017, 250 )
    a.CetakData()

    b = Mekatronika('UNM', 'Teknik', 2017, 350)
    b.CetakData()

    del b

    b = PTIK('UNM', 'Teknik', 2017, 350, 'Pendidikan Teknik Elektro')
    b.CetakData()




if __name__ == "__main__":
    main()

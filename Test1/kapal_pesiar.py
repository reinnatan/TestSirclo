from Test1.kapal import Kapal

class KapalPesiar(Kapal):
    def __init__(self, panjang, tinggi, lebar, kecepatan, jumlah_penumpang):
        super().__init__(panjang, tinggi, lebar, kecepatan, jumlah_penumpang)

    def set_jumlah_awak(self, jumlah_awak):
        self.__jumlah_awak = jumlah_awak

    def get_jumlah_awak(self):
        return self.__jumlah_awak

    def set_fasilitas(self, fasilitas):
        self.__fasilitas = fasilitas

    def get_fasilitas(self):
        return self.__fasilitas

    def berlayar(self):
        return "Naikan jangkar, dorong kapal ketengah dengan perahu kecil, hidupkan mesin kapal"

    def berlabuh(self):
        return "Matikan mesin kapal, dorong kapal dengan kapal kecil ke buritan, turunkan jangkar"
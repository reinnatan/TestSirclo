from Test1.kapal import Kapal

class PerahuLayar(Kapal):
    def __init__(self, panjang, tinggi, lebar, kecepatan, jumlah_penumpang):
        super().__init__(panjang, tinggi, lebar, kecepatan, jumlah_penumpang)

    def set_jumlah_layar(self, jumlah_layar):
        self.__jumlah_layar = jumlah_layar

    def get_jumlah_layar(self):
        return self.__jumlah_layar

    def berlayar(self):
        return "Lepaskan tali pengait, rentangkan layar"

    def berlayar(self):
        return "Kuncupkan layar, dan dorong dengan sampan apabila sudah dekat dengan buritan, kaitkan tali kapal ke pancang"

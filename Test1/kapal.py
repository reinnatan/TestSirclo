class Kapal:
    def __init__(self, panjang, tinggi, lebar, kecepatan, jumlah_penumpang):
        self.__panjang = panjang
        self.__tinggi = tinggi
        self.__lebar = lebar
        self.__kecepatan = kecepatan
        self.__jumlah_penumpang = jumlah_penumpang

    def set_panjang(self, panjang):
        self.__panjang = panjang

    def get_panjang(self):
        return self.__panjang

    def set_tinggi(self, tinggi):
        self.__tinggi = tinggi

    def get_tinggi(self):
        return self.__tinggi

    def set_lebar(self, lebar):
        self.__lebar = lebar

    def get_lebar(self):
        return self.__lebar

    def set_kecepatan(self, kecepatan):
        self.__kecepatan = kecepatan

    def get_keceptan(self):
        return self.__kecepatan

    def set_jumlah_penumpang(self, jumlah_penumpang):
        self.__jumlah_penumpang = jumlah_penumpang

    def get_jumlah_penumpang(self):
        return self.__jumlah_penumpang

    def berlayar(self):
        raise NotImplementedError("Subclass harus mengimplemetasikan method berlayar")

    def berlabuh(self):
        raise NotImplementedError("Subclass harus mengimplemetasikan method berlabuh")



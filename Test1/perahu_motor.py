from Test1.kapal import Kapal


class PerahuMotor(Kapal):
    def __init__(self, panjang, tinggi, lebar, kecepatan, jumlah_penumpang):
        super().__init__(panjang, tinggi, lebar, kecepatan, jumlah_penumpang)

    def set_jumlah_motor(self, jumlah_motor):
        self.__jumlah_motor = jumlah_motor

    def get_jumlah_motor(self):
        return self.__jumlah_motor

    def berlayar(self):
        return "Naikan tali pengait, hidupkan semua mesin kapal"

    def berlabuh(self):
        return "Turunkan kecepatan mesin, dan matikan mesin apabila sudah dekat dengan buritan, kaitkan tali kapal ke pancang"
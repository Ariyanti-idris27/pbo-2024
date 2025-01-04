# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/
# .
# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;
        
# ini Kontribusi dari Ikhwan 
def batas():
    print("-"*35)

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

class TempatWisata:
    def __init__(self, nama, lokasi, deskripsi, harga_tiket):
        self.nama = "pantai sulamadaha"
        self.lokasi = "ternate utara"
        self.deskripsi = "pantai dengan air jerni dengn pemandangan bawa laut"
        self.harga_tiket = 10000

    def tampilkan_info(self):
        return f"Nama: {self.nama}\nLokasi: {self.lokasi}\nDeskripsi: {self.deskripsi}\nHarga Tiket: Rp{self.harga_tiket:,}\n"


class DaftarWisata:
    def __init__(self):
        self.wisata_list = []

    def tambah_wisata(self, wisata):
        self.wisata_list.append(wisata)

    def tampilkan_semua(self):
        if not self.wisata_list:
            return "Belum ada tempat wisata yang terdaftar."
        return "\n".join([wisata.tampilkan_info() for wisata in self.wisata_list])

    def cari_wisata(self, nama):
        for wisata in self.wisata_list:
            if wisata.nama.lower() == nama.lower():
                return wisata.tampilkan_info()
        return "Tempat wisata tidak ditemukan."

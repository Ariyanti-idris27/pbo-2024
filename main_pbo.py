# For Test using or import modul
# Main code untuk test modul projek bersama


from modul_satu_pbo import TempatWisata, DaftarWisata

# Inisialisasi daftar wisata
daftar_wisata = DaftarWisata()

# Menambahkan beberapa tempat wisata di Ternate
daftar_wisata.tambah_wisata(TempatWisata("Pantai Sulamadaha", "Ternate Utara", "Pantai indah dengan air jernih dan pemandangan bawah laut.", 10000))
daftar_wisata.tambah_wisata(TempatWisata("Benteng Tolukko", "Kota Ternate", "Benteng peninggalan Portugis dengan nilai sejarah tinggi.", 15000))
daftar_wisata.tambah_wisata(TempatWisata("Danau Tolire", "Ternate Barat", "Danau yang terkenal dengan legenda dan keindahan alamnya.", 5000))

# Menampilkan semua tempat wisata
print("Daftar Tempat Wisata:")
print(daftar_wisata.tampilkan_semua())

# Mencari tempat wisata
nama_dicari = input("\nMasukkan nama tempat wisata yang ingin dicari: ")
print(daftar_wisata.cari_wisata(nama_dicari))

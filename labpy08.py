class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, nama, tugas, uts, uas):
        """Menambah data mahasiswa."""
        self.data_mahasiswa[nama] = (tugas, uts, uas)
        print(f"Data untuk {nama} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan semua data mahasiswa."""
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.data_mahasiswa.items():
                tugas, uts, uas = nilai
                print(f"Nama: {nama}, Tugas: {tugas}, UTS: {uts}, UAS: {uas}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"Data untuk {nama} berhasil dihapus.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")
    
    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama."""
        if nama in self.data_mahasiswa:
            self.data_mahasiswa[nama] = nilai_baru
            print(f"Data untuk {nama} berhasil diubah.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

if __name__ == "__main__":
    daftar = DaftarNilaiMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Hapus data")
        print("4. Ubah data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama: ")
            tugas = int(input("Nilai Tugas: "))
            uts = int(input("Nilai UTS: "))
            uas = int(input("Nilai UAS: "))
            daftar.tambah(nama, tugas, uts, uas)
        elif pilihan == "2":
            daftar.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ")
            daftar.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang akan diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            daftar.ubah(nama, nilai_baru)
        elif pilihan == "5":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
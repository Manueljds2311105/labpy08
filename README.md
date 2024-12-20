# labpy08 class
Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom., 

Mata Kuliah: Bahasa Pemograman

## Penjelasan
### Class DaftarNilaiMahasiswa
a. Inisialisasi (__init__)
```python
    def __init__(self):
    self.data_mahasiswa = {}
```
- Membuat sebuah dictionary kosong self.data_mahasiswa untuk menyimpan data mahasiswa dengan format:
  ```python
  {
    "Nama Mahasiswa": (Nilai Tugas, Nilai UTS, Nilai UAS)
  }
  ```
b. Tambah
```python
def tambah(self, nama, tugas, uts, uas):
    self.data_mahasiswa[nama] = (tugas, uts, uas)
    print(f"Data untuk {nama} berhasil ditambahkan.")
```
- Menambahkan data mahasiswa ke dalam dictionary data_mahasiswa dengan kunci berupa nama dan nilai berupa tuple (tugas, uts, uas).

c. Tampilkan
```python
def tampilkan(self):
    if not self.data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for nama, nilai in self.data_mahasiswa.items():
            tugas, uts, uas = nilai
            print(f"Nama: {nama}, Tugas: {tugas}, UTS: {uts}, UAS: {uas}")
```
- Menampilkan seluruh data mahasiswa jika ada, atau pesan bahwa data belum tersedia jika dictionary kosong.
  
d. Hapus
```python
def hapus(self, nama):
    if nama in self.data_mahasiswa:
        del self.data_mahasiswa[nama]
        print(f"Data untuk {nama} berhasil dihapus.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")
```
- Menghapus data mahasiswa berdasarkan nama. Jika nama tidak ditemukan, program akan menampilkan pesan tidak ada data.
  
e. Ubah
```python
def ubah(self, nama, nilai_baru):
    if nama in self.data_mahasiswa:
        self.data_mahasiswa[nama] = nilai_baru
        print(f"Data untuk {nama} berhasil diubah.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")
```
- Mengubah data mahasiswa berdasarkan nama. nilai_baru adalah nilai yang akan menggantikan data sebelumnya.
  
f. Loop Program
```python
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
```
- Program terus berjalan dalam loop hingga pengguna memilih opsi "Keluar".
- Input dari pengguna menentukan tindakan yang akan dilakukan, seperti menambah, menampilkan, menghapus, atau mengubah data.
## Hasil Program
![foto](https://github.com/Manueljds2311105/foto/blob/4c9f2fc78e79eaa8293705d36c10006691e3ecbe/labpy08.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2012_7_2024%209_04_54%20AM.png)
![foto](https://github.com/Manueljds2311105/foto/blob/4c9f2fc78e79eaa8293705d36c10006691e3ecbe/labpy08.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2012_7_2024%209_05_10%20AM.png)
## Diagram
![foto](https://github.com/Manueljds2311105/foto/blob/88e09d3843bd69e519573af4172ff3c263253713/Diagramlab8.drawio.png)
## Flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/88e09d3843bd69e519573af4172ff3c263253713/lab8.drawio.png)

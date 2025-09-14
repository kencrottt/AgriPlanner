# import csv
# import os

# USER = 'users.csv'
# TANAMAN = 'tanaman.csv'

# # baca csv
# def load_users():
#     if not os.path.exists(USER):
#         return []
#     with open(USER, newline='', encoding='utf-8') as f:
#         return list(csv.DictReader(f))

# def save_users(users):
#     with open(USER, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=["username", "nama", "password"])
#         writer.writeheader()
#         writer.writerows(users)

# # register login
# def registrasi():
#     print("\n== REGISTRASI ==")
#     users = load_users()
#     username = input("Username: ")
#     if any(u['username'] == username for u in users):
#         print("Username sudah digunakan.")
#         return
#     nama = input("Nama lengkap: ")
#     password = input("Password: ")
    
#     users.append({
#         "username": username,
#         "nama": nama,
#         "password": password
#     })

#     save_users(users)
#     print("Registrasi berhasil!")

# def login():
#     print("\n== LOGIN ==")
#     username = input("Username: ")
#     password = input("Password: ")

#     users = load_users()
#     for user in users:
#         if user["username"] == username and user["password"] == password:
#             print(f"Selamat datang, {user['nama']}!")
#             return user 
#     print("Username atau password salah.")
#     return None

# penyimpanan
import csv
import os
from tabulate import tabulate

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def lihat_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                print(tabulate(data[1:], headers=data[0], tablefmt="grid"))
            else:
                print("Belum ada data tanaman.")
    except FileNotFoundError:
        print("File belum dibuat.")

def tambah_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        data = [[
            "id_tanaman", "nama_tanaman", "stok", "jenis_tanah", "musim",
            "value_per_kg", "kg_per_m2", "persemaian", "pertumbuhan_vegetatif",
            "pembungaan_generatif", "pembuahan", "pematangan", "panen"
        ]]

    id_tanaman = input("ID Tanaman: ")
    if any(row[0] == id_tanaman for row in data[1:]):
        print("ID tanaman sudah ada.")
        return

    nama = input("Nama Tanaman: ")
    stok = input("Stok: ")
    jenis_tanah = input("Jenis Tanah: ")
    musim = input("Musim: ")
    value = input("Value per kg: ")
    kg_per_m2 = input("Kg per m2: ")
    fase = [input(f"{f}: ") for f in [
        "Persemaian", "Pertumbuhan Vegetatif", "Pembungaan Generatif", "Pembuahan", "Pematangan", "Panen"
    ]]

    baru = [id_tanaman, nama, stok, jenis_tanah, musim, value, kg_per_m2] + fase

    data.append(baru)
    with open("tanaman.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Tanaman berhasil ditambahkan.")

def edit_stok_busuk():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("File belum ada.")
        return

    lihat_tanaman()
    id_edit = input("Masukkan ID tanaman: ")
    for row in data[1:]:
        if row[0] == id_edit:
            print(f"Stok saat ini: {row[2]}")
            try:
                jumlah_busuk = int(input("Jumlah tanaman busuk: "))
                row[2] = str(max(0, int(row[2]) - jumlah_busuk))
                with open("tanaman.csv", 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print("Stok berhasil diperbarui.")
            except ValueError:
                print("Input harus angka.")
            return
    print("ID tidak ditemukan.")

def hapus_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("File belum ada.")
        return

    lihat_tanaman()
    id_hapus = input("Masukkan ID tanaman yang ingin dihapus: ")
    data_baru = [data[0]] + [row for row in data[1:] if row[0] != id_hapus]

    if len(data_baru) < len(data):
        with open("tanaman.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data_baru)
        print("Tanaman berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")

def sort_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("File belum ada.")
        return

    if len(data) <= 1:
        print("Tidak ada data untuk diurutkan.")
        return

    print("""
=== SORTING ===
1. Nama Tanaman (A-Z)
2. Stok (terbesar-terkecil)
3. Value per Kg (tertinggi)
""")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        hasil = sorted(data[1:], key=lambda x: x[1].lower())
    elif pilihan == "2":
        hasil = sorted(data[1:], key=lambda x: int(x[2]), reverse=True)
    elif pilihan == "3":
        hasil = sorted(data[1:], key=lambda x: int(x[5]), reverse=True)
    else:
        print("Pilihan tidak valid.")
        return

    print(tabulate(hasil, headers=data[0], tablefmt="grid"))

def search_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("File belum ada.")
        return

    print("""
=== SEARCH TANAMAN ===
1. Berdasarkan ID
2. Berdasarkan Nama (mengandung)
""")
    opsi = input("Pilih: ")
    hasil = []
    if opsi == "1":
        id_cari = input("Masukkan ID: ")
        hasil = [row for row in data[1:] if row[0].lower() == id_cari.lower()]
    elif opsi == "2":
        nama = input("Masukkan kata kunci nama: ")
        hasil = [row for row in data[1:] if nama.lower() in row[1].lower()]
    else:
        print("Pilihan tidak valid.")
        return

    if hasil:
        print(tabulate(hasil, headers=data[0], tablefmt="grid"))
    else:
        print("Data tidak ditemukan.")

def perencanaan_maksimal():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("File tanaman.csv tidak ditemukan.")
        return

    if len(data) <= 1:
        print("Tidak ada data tanaman.")
        return

    jenis_tanah_input = input("Masukkan jenis tanah lahan: ").lower()
    musim_input = input("Masukkan musim: ").lower()
    try:
        luas = float(input("Masukkan luas lahan (m2): "))
        planning_period = int(input("Masukkan periode perencanaan (hari): "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    rekomendasi = []
    for row in data[1:]:
        if row[3].lower() == jenis_tanah_input and row[4].lower() == musim_input:
            try:
                kg_per_m2 = float(row[6])
                value_per_kg = float(row[5])
                cycle_days = sum([int(row[i]) for i in range(7, 13)])
            except ValueError:
                continue

            cycles = planning_period // cycle_days
            yield_per_cycle = kg_per_m2 * luas
            total_yield = yield_per_cycle * cycles
            estimated_income = total_yield * value_per_kg

            rekomendasi.append([
                row[0], row[1], cycle_days, cycles,
                round(yield_per_cycle, 2), round(total_yield, 2), f'Rp {round(estimated_income):,}'
            ])

    clear_screen()
    if not rekomendasi:
        print("Tidak ada tanaman yang cocok.")
    else:
        rekomendasi.sort(key=lambda x: x[6], reverse=True)
        print(tabulate(rekomendasi, headers=["ID", "Nama Tanaman", "Siklus (hari)", "Jumlah Siklus", "Hasil per Siklus (kg)", "Total Hasil (kg)", "Estimasi Income"], tablefmt="grid"))
# Siklus: jumlah total hari fase pertumbuhan dari persemaian sampai panen (jumlah kolom 7 sampai 12)
# Jumlah Siklus: berapa kali tanaman bisa dipanen dalam periode yang diinput (planning_period // cycle_days)
# Hasil per Siklus: kg per m2 * luas
# Estimasi Income: total hasil panen dikali value per kg

def main_menu():
    while True:
        clear_screen()
        print("""
=== MENU UTAMA APLIKASI AGRIPLANNER ===
1. Kelola Tanaman
2. Perencanaan Maksimal
3. Keluar
""")
        pilih = input("Pilih menu (1-3): ")
        if pilih == '1':
            menu_tanaman()
        elif pilih == '2':
            clear_screen()
            perencanaan_maksimal()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk coba lagi...")

def menu_tanaman():
    while True:
        clear_screen()
        print("""
=== MENU KELOLA TANAMAN ===
1. Lihat Daftar Tanaman
2. Tambah Tanaman
3. Edit Stok (Karena Busuk)
4. Hapus Tanaman
5. Urutkan Tanaman
6. Cari Tanaman
7. Kembali ke Menu Utama
""")
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == '1': clear_screen(); lihat_tanaman(); input("\nTekan Enter...")
        elif pilihan == '2': clear_screen(); tambah_tanaman(); input("\nTekan Enter...")
        elif pilihan == '3': clear_screen(); edit_stok_busuk(); input("\nTekan Enter...")
        elif pilihan == '4': clear_screen(); hapus_tanaman(); input("\nTekan Enter...")
        elif pilihan == '5': clear_screen(); sort_tanaman(); input("\nTekan Enter...")
        elif pilihan == '6': clear_screen(); search_tanaman(); input("\nTekan Enter...")
        elif pilihan == '7': break
        else: print("Pilihan tidak valid."); input("Tekan Enter...")

main_menu()

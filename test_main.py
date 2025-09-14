import os
import pandas as pd
import pyfiglet
from tabulate import tabulate
from datetime import datetime, date, timedelta
import math
import csv

def font_keren():
    font = 'small_slant'
    text = 'AgriPlanner'
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)


def omni_man_gyatt():
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠟⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣳⠖⠳⣄⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡤⠒⠀⠂⡾⠉⠀⠀⠀⠀⠉⢳⡄⣄⡀⠀⠀
    ⠀⠀⠀⢸⡥⠀⣀⡼⢁⠀⢰⡄⠀⡄⠀⠀⣧⠀⠙⡆⠀
    ⠀⢀⣠⠼⠗⠚⠉⠠⠋⠀⠀⢷⣠⣧⠀⠀⠈⠳⢤⣇⠀
    ⠀⣾⣟⠒⠦⣄⠀⠀⠀⣠⡴⠋⠁⢈⠛⢦⣄⣠⣴⣾⣷
    ⢀⡟⠙⢶⣤⠬⠷⣼⡏⠉⠉⢩⡍⠹⠦⢤⣿⣤⣨⣿⠈
    ⡾⣡⠆⠁⠀⠀⠀⢠⡀⠀⠀⠀⢱⡀⠀⠂⠙⠎⠻⡅⠀
    ⢿⠁⠒⣤⠤⣤⣀⠀⢧⠀⠀⠀⣸⠃⠀⠀⠀⡶⣤⣽⠀
    ⠈⠳⣴⡇⠀⠀⠈⠛⢦⣄⣠⠾⢿⣄⣀⣠⠾⣡⠞⠁⠀
    ⠀⠀⠈⠉⠉⠉⠁⢧⢠⠟⣽⠀⢿⠀⢧⢰⡈⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠐⢫⠏⢸⠁⠀⠈⢳⠘⢧⣙⢦⠀''')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def register():
    # Pastikan user.csv ada dengan header
    if not os.path.exists("user.csv"):
        pd.DataFrame(columns=["email", "username", "password", "nama"]).to_csv("user.csv", index=False)
    
    read_user = pd.read_csv("user.csv")
    
    while True:
        inputan_email = input("Masukkan Email : ")
        if inputan_email == "":
            print("Email tidak boleh kosong!")
            continue
        elif inputan_email in read_user["email"].values:
            print("Email sudah terdaftar!")
            continue
        else: 
            break
    
    while True:
        inputan_username = input("Masukkan Username : ")
        if inputan_username == "":
            print("Username tidak boleh kosong!")
            continue
        elif inputan_username in read_user["username"].values:
            print("Username sudah terdaftar!")
            continue
        else: 
            break
    
    while True:
        inputan_password = input("Masukkan Password : ")
        if inputan_password == "":
            print("Password tidak boleh kosong!")
            continue
        else: 
            break

    while True:
        inputan_nama = input("Masukkan Nama : ")
        if inputan_nama == "":
            print("Nama tidak boleh kosong!")
            continue
        else: 
            break

    # while True:
    #     inputan_jenis_tanah_dominan = input("Masukkan Jenis Tanah Dominan : ")
    #     if inputan_jenis_tanah_dominan == "":
    #         print("Jenis tanah dominan tidak boleh kosong!")
    #         continue
    #     else: 
    #         break

    new_user = pd.DataFrame({
        "email": [inputan_email],
        "username": [inputan_username],
        "password": [inputan_password],
        "nama": [inputan_nama]
        })
    read_user = pd.concat([read_user, new_user], ignore_index=True)
    read_user.to_csv("user.csv", index=False)
    print("Pendaftaran berhasil!")

def login():
    try:
        users = pd.read_csv('user.csv')
    except FileNotFoundError:
        print("File 'user.csv' tidak ditemukan. Silakan daftar terlebih dahulu.")
        return None

    while True:
        input_username = str(input("Masukkan Username : "))
        if input_username in users['username'].values:
            break
        else:
            print("Username belum terdaftar atau salah.")
            continue
    
    while True:
        input_paswort = str(input("Masukkan Password : "))
        user_match = users[users["username"] == input_username]
        
        if not user_match.empty:
            stored_password = user_match.iloc[0]["password"]
            if stored_password == input_paswort:
                global username 
                username = user_match.iloc[0]["username"]
                nama_manggil = user_match.iloc[0]["nama"]
                print(f"Selamat datang, {nama_manggil}!")
                return username
            else:
                print("Password salah.")
        else:
            print("Pengguna tidak ditemukan (kesalahan internal).") 
        
        continue

def kelola_user(current_username):
    while True:
        clear_screen()
        print('Dashboard User')
        print('==============')
        print(f"Silakan pilih menu.")
        print(f'''
1. Cek Biodata
2. Ubah Biodata
3. Keluar''')

        inputan1 = input("Pilih menu [1-3]: ").strip()

        if inputan1 == "1":
            try:
                akses = pd.read_csv('user.csv')
            except FileNotFoundError:
                print("File 'user.csv' tidak ditemukan.")
                input("Tekan Enter untuk kembali...")
                continue
            
            buka_pd = akses[akses['username'] == current_username]
            
            if buka_pd.empty:
                print("User tidak ditemukan.")
                input("Tekan Enter untuk kembali...")
                break # Keluar jika pengguna tidak ditemukan, ada yang salah
            
            print('\n============')
            print('Biodata User')
            print('============')
            email = buka_pd["email"].iloc[0]
            username_tampil = buka_pd["username"].iloc[0]
            nama = buka_pd["nama"].iloc[0]
            # jenis_tanah_dominan = buka_pd["jenis_tanah_dominan"].iloc[0]

            print(f"Email       : {email}")
            print(f"Username    : {username_tampil}")
            print(f"Nama        : {nama}")
            # print(f"Jenis Tanah : {jenis_tanah_dominan}")
            input("\nTekan Enter untuk kembali...")
        
        elif inputan1 == "2":
            try:
                akses = pd.read_csv('user.csv')
            except FileNotFoundError:
                print("File 'user.csv' tidak ditemukan.")
                input("Tekan Enter untuk kembali...")
                continue
            
            buka_pd = akses[akses['username'] == current_username]
            if buka_pd.empty:
                print("User tidak ditemukan.")
                input("Tekan Enter untuk kembali...")
                break # Keluar jika pengguna tidak ditemukan
            
            print('\n============')
            print('Biodata User')
            print('============')
            email = buka_pd["email"].iloc[0]
            username_tampil = buka_pd["username"].iloc[0]
            nama = buka_pd["nama"].iloc[0]
            # jenis_tanah_dominan = buka_pd["jenis_tanah_dominan"].iloc[0]

            print(f"Email       : {email}")
            print(f"Username    : {username_tampil}")
            print(f"Nama        : {nama}")
            # print(f"Jenis Tanah : {jenis_tanah_dominan}")
            
            input_lanjutan = input("Apakah anda ingin mengedit biodata anda? [y/t] ").lower()
            
            if input_lanjutan != 'y':
                print("Biodata tidak diubah.")
                input("Tekan Enter untuk kembali...")
                continue
            
            while True:
                print('''
                1. Email
                2. Username
                3. Nama
                ''')
                input_pilihan_edit = input("Data mana yang ingin anda ubah? ").strip()
                
                if input_pilihan_edit not in ['1', '2', '3']:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    continue
                else:
                    break 

            kolom_map = {
                '1': 'email',
                '2': 'username',
                '3': 'nama'
            }
            
            kolom_ubah = kolom_map[input_pilihan_edit]
            print(f"\nPerubahan {kolom_ubah.capitalize()}")
            print("===================")
            
            nilai_lama = buka_pd[kolom_ubah].iloc[0]
            print(f"Nilai lama: {nilai_lama}")
            
            nilai_baru = input(f"Masukkan nilai baru untuk {kolom_ubah}: ").strip()
            
            df = pd.read_csv('user.csv')
            df.loc[df['username'] == current_username, kolom_ubah] = nilai_baru
            
            if kolom_ubah == 'username':
                current_username = nilai_baru # Perbarui current_username di sesi ini
                print("Username telah diubah, harap gunakan username baru untuk akses selanjutnya.")
            
            df.to_csv('user.csv', index=False)
            print(f"{kolom_ubah.capitalize()} berhasil diubah menjadi: {nilai_baru}")
            input("\nTekan Enter untuk kembali...")

        elif inputan1 == "3":
            print("Keluar dari menu kelola user.")
            break

        else:
            print("Input tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk kembali...")
            continue



def pagination_tanaman(file_path, jumlah_per_halaman=5):
    try:
        df = pd.read_csv(file_path)
        # Bersihkan nama kolom
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return
    except KeyError as e:
        print(f"Error: Kolom yang diharapkan tidak ada di '{file_path}': {e}")
        return

    total_data = len(df)
    total_halaman = (total_data + jumlah_per_halaman - 1) // jumlah_per_halaman
    halaman = 1

    while True:
        clear_screen()
        awal = (halaman - 1) * jumlah_per_halaman
        akhir = min(awal + jumlah_per_halaman, total_data) # Pastikan 'akhir' tidak melebihi total_data
        
        # Pilih dan tampilkan kolom yang relevan
        display_df = df.iloc[awal:akhir]
        # id tanaman,nama tanaman,stok,jenis tanah,luas lahan,musim,value per kg,jumlah per m^2 (kg),berat per satuan,fase persemaian,fase pertumbuhan vegetatif,fase pembungaan generatif,fase pembuahan,fase pematangan,fase panen
        # Definisikan header secara eksplisit untuk tabulate
        kolom = ["id tanaman", "nama tanaman", "stok", "value per kg", "jumlah per m^2 (kg)", "berat per satuan"]
        headers = ["Id Tanaman", "Nama Tanaman", "Stok", "Value/kg", "KG per m^2", "Berat per satuan"]
        # Pastikan semua headers_to_display ada di dataframe
        if not all(col in display_df.columns for col in kolom):
            print(f"Error: Beberapa kolom yang diharapkan untuk tampilan tidak ditemukan di file '{file_path}'.")
            print(f"Kolom yang tersedia: {display_df.columns.tolist()}")
            input("Tekan Enter untuk kembali...")
            return

        print(tabulate(display_df[kolom], headers=headers, tablefmt='grid', showindex=False))
        print(f"Halaman {halaman} dari {total_halaman}")

        pilihan = input("\n[P]rev, [N]ext, [Q]uit: ").strip().lower()

        if pilihan == 'n' and halaman < total_halaman:
            halaman += 1
        elif pilihan == 'p' and halaman > 1:
            halaman -= 1
        elif pilihan == 'q':
            print("Keluar dari tampilan.")
            break
        else:
            print("Input tidak valid atau sudah di akhir/awal halaman.")
            input("Tekan Enter untuk melanjutkan...")

# pagination_tanaman("tanaman.csv")

def input_pengeluaran():
    clear_screen()
    print("Input Pengeluaran")
    print("=================")

    try:
        daftar_pengeluaran = pd.read_csv("pengeluaran.csv")
    except FileNotFoundError:
        daftar_pengeluaran = pd.DataFrame(columns=['kategori', 'nama pengeluaran', 'harga', 'jumlah', 'keterangan', 'tanggal beli'])

    try:
        daftar_tanaman = pd.read_csv("tanaman.csv")
        daftar_tanaman.columns = daftar_tanaman.columns.str.strip()
    except FileNotFoundError:
        print("Error: File 'tanaman.csv' tidak ditemukan. Tidak dapat melakukan pengeluaran tanaman.")
        input("Tekan Enter untuk kembali...")
        return
    
    try:
        di_gudang = pd.read_csv("gudang.csv")
        di_gudang.columns = di_gudang.columns.str.strip()
    except FileNotFoundError:
        print("Error: File 'gudang.csv' tidak ditemukan. Tidak dapat melakukan pengeluaran tanaman ke gudang.")
        input("Tekan Enter untuk kembali...")
        return

    while True:
        print('''
1. Tanaman
2. Biaya Produksi
        ''')
        input_kategori = input("\nPilih kategori pengeluaran : ").strip()

        if input_kategori == '2':
            input_nama_pengeluaran = input("\nNama Pengeluaran : ").strip()
            if not input_nama_pengeluaran:
                print("Nama pengeluaran tidak boleh kosong.")
                continue

            while True:
                try:
                    input_harga = int(input("\nHarga : "))
                    if input_harga > 0:
                        break
                    else:
                        print("Harga harus lebih dari 0.")
                except ValueError:
                    print("Input harus berupa angka!")
            
            while True:
                try:
                    input_jumlah = int(input("\nJumlah : "))
                    if input_jumlah > 0:
                        break
                    else:
                        print("Jumlah harus lebih dari 0.")
                except ValueError:
                    print("Input harus berupa angka!")
            
            tanggal_beli = date.today().strftime('%Y-%m-%d') # Format tanggal
                
            input_keterangan = input("Masukkan keterangan (opsional, tekan Enter jika kosong) : ").strip()
            
            pengeluaran_baru = pd.DataFrame ([{
                'kategori' : "biaya produksi",
                'nama pengeluaran' : input_nama_pengeluaran,
                'harga' : input_harga,
                'jumlah' : input_jumlah,
                'keterangan' : input_keterangan if input_keterangan else '-', # Simpan '-' jika kosong
                'tanggal beli' : tanggal_beli
            }])
        
            daftar_pengeluaran = pd.concat([daftar_pengeluaran, pengeluaran_baru], ignore_index=True)
            daftar_pengeluaran.to_csv('pengeluaran.csv', index=False)
            print("\nPengeluaran sudah tercatat!")
            break

        elif input_kategori == "1":
            pagination_tanaman("tanaman.csv")

            while True:
                input_id_tanaman_pengeluaran = input("\nMasukkan ID tanaman yang dibeli : ").upper().strip()
                hasil_cari = daftar_tanaman[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran]

                if hasil_cari.empty:
                    print("ID tidak valid atau tidak ada dalam daftar tanaman anda.\n")
                    continue
                else:
                    hasil_cari = hasil_cari.iloc[0]
                    break

            nama_pengeluaran = hasil_cari['nama tanaman']
                
            while True:
                try:
                    input_jumlah_tanaman = int(input("Masukkan jumlah yang dibeli (unit) : ")) 
                    if input_jumlah_tanaman > 0:
                        break
                    else:
                        print("Jumlah harus lebih dari 0.")
                except ValueError:
                    print("Inputan harus berisi angka.")
            
            while True:
                try:
                    inputan_harga = int(input("Masukkan jumlah uang yang terpakai : "))
                    if inputan_harga > 0:
                        break
                    else:
                        print("Harga harus lebih dari 0.")
                except ValueError:
                    print("Inputan harus berisi angka.")
            
            tanggal_beli = date.today().strftime('%Y-%m-%d') # Format tanggal

            inputan_keterangan = input("\nMasukkan keterangan (opsional, tekan Enter jika kosong) : ").strip()
            
            pengeluaran_baru = pd.DataFrame ([{
                'kategori' : "tanaman",
                'nama pengeluaran' : nama_pengeluaran,
                'harga' : inputan_harga,
                'jumlah' : input_jumlah_tanaman, # Ini adalah 'jumlah' dalam unit, bukan KG
                'keterangan' : inputan_keterangan if inputan_keterangan else '-',
                'tanggal beli' : tanggal_beli
            }])
            daftar_pengeluaran = pd.concat([daftar_pengeluaran, pengeluaran_baru], ignore_index=True)
            daftar_pengeluaran.to_csv('pengeluaran.csv', index=False)     

            # Perbarui stok di tanaman.csv (stok master)
            # Pastikan kolom 'stok' di tanaman.csv adalah numerik
            daftar_tanaman['stok'] = pd.to_numeric(daftar_tanaman['stok'], errors='coerce')
            stok_lama_tanaman = daftar_tanaman.loc[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'].iloc[0]
            stok_baru_tanaman = stok_lama_tanaman + input_jumlah_tanaman
            daftar_tanaman.loc[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'] = stok_baru_tanaman
            daftar_tanaman.to_csv('tanaman.csv', index=False)
            
            # Perbarui stok di gudang.csv (stok di gudang)
            # Jika tanaman baru di gudang.csv, tambahkan. Jika tidak, perbarui.
            # Pastikan kolom 'stok' di gudang.csv adalah numerik
            di_gudang['stok'] = pd.to_numeric(di_gudang['stok'], errors='coerce')
            
            if input_id_tanaman_pengeluaran in di_gudang['id tanaman'].values:
                stok_lama_gudang = di_gudang.loc[di_gudang['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'].iloc[0]
                stok_baru_gudang = stok_lama_gudang + input_jumlah_tanaman
                di_gudang.loc[di_gudang['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'] = stok_baru_gudang
            else:
                # Tambahkan baris baru ke gudang.csv jika ID tidak ditemukan di sana
                # Pastikan new_gudang_row memiliki semua kolom yang diperlukan untuk gudang.csv
                # Dapatkan kolom yang relevan dari daftar_tanaman untuk baris baru
                new_gudang_row_data = daftar_tanaman[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran].iloc[0].to_dict()
                new_gudang_row_data['stok'] = input_jumlah_tanaman # Tetapkan stok awal
                
                # Pastikan DataFrame baru memiliki kolom yang sama dengan gudang_df yang ada
                # untuk menghindari masalah dengan pd.concat
                new_gudang_df_row = pd.DataFrame([new_gudang_row_data], columns=di_gudang.columns)
                di_gudang = pd.concat([di_gudang, new_gudang_df_row], ignore_index=True)

            di_gudang.to_csv('gudang.csv', index=False)
            print("Pengeluaran dan stok berhasil dicatat!")
            break
                        
        else:
            print("Inputan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")
            continue
    input("\nTekan Enter untuk kembali ke menu utama...")


def hitung_estimasi_aset(file_path):
    """
    Menghitung total estimasi laba dari file CSV yang diberikan (gudang atau ladang).
    """
    try:
        df = pd.read_csv(file_path)
        
        # Kolom 'berat per satuan' di CSV mungkin memiliki spasi di akhir, jadi kita bersihkan
        df.columns = df.columns.str.strip() 

        # Pastikan kolom yang diperlukan ada
        required_columns = ['stok', 'berat per satuan', 'value per kg']
        if not all(col in df.columns for col in required_columns):
            missing_cols = [col for col in required_columns if col not in df.columns]
            raise KeyError(f"Kolom yang diperlukan tidak ditemukan: {', '.join(missing_cols)}")

        # Konversi kolom yang diperlukan ke numerik
        df['stok'] = pd.to_numeric(df['stok'], errors='coerce').fillna(0)
        df['berat per satuan'] = pd.to_numeric(df['berat per satuan'], errors='coerce').fillna(0)
        df['value per kg'] = pd.to_numeric(df['value per kg'], errors='coerce').fillna(0)


        df['estimated_profit'] = df['stok'] * df['berat per satuan'] * df['value per kg']
        total_estimated_profit = df['estimated_profit'].sum()
        return total_estimated_profit

    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return None
    except KeyError as e:
        print(f"Error: {e}. Pastikan nama kolom di CSV sesuai (stok, berat per satuan, value per kg).")
        return None
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca {file_path}: {e}")
        return None

def estimasi_laba_dan_aset():
    """
    Menggabungkan perhitungan estimasi aset gudang, ladang, dan laba bersih.
    Menyediakan looping untuk perhitungan berulang.
    """
    while True:
        clear_screen()
        print("\n=== Menu Estimasi Laba dan Aset ===")
        print("1. Estimasi Aset Gudang")
        print("2. Estimasi Aset Ladang")
        print("3. Estimasi Laba Bersih (30 hari terakhir)")
        print("4. Input Pengeluaran")
        print("5. Keluar")

        pilihan = input("Pilih menu [1-4]: ").strip()

        if pilihan == '1':
            print("\nMenghitung Estimasi Aset Gudang...")
            total_aset_gudang = hitung_estimasi_aset('gudang.csv')
            if total_aset_gudang is not None:
                print(f"Total Estimasi Aset Gudang: Rp {total_aset_gudang:,.2f}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '2':
            print("\nMenghitung Estimasi Aset Ladang...")
            total_aset_ladang = hitung_estimasi_aset('ladang.csv')
            if total_aset_ladang is not None:
                print(f"Total Estimasi Aset Ladang: Rp {total_aset_ladang:,.2f}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '3':
            print("\nMenghitung Estimasi Laba Bersih (30 hari terakhir)...")
            try:
                batasakhir_str = input("Masukkan tanggal akhir rekap (format:YYYY-MM-DD, kosongkan untuk hari ini): ").strip()
                if batasakhir_str:
                    batasakhir = datetime.strptime(batasakhir_str, "%Y-%m-%d")
                else:
                    batasakhir = datetime.now() 

                batasawal = batasakhir - timedelta(days=30)

                # --- Pemasukan ---
                total_pemasukan = 0
                try:
                    read_pemasukan = pd.read_csv('pemasukan.csv')
                    # Pastikan 'tanggal pemasukan' adalah string sebelum mengonversi ke datetime
                    read_pemasukan['tanggal pemasukan'] = read_pemasukan['tanggal pemasukan'].astype(str)
                    read_pemasukan['tanggal pemasukan'] = pd.to_datetime(read_pemasukan['tanggal pemasukan'], format='%Y-%m-%d', errors='coerce')
                    
                    # Hapus baris di mana konversi tanggal gagal
                    read_pemasukan.dropna(subset=['tanggal pemasukan'], inplace=True)

                    filtereddate_pemasukan = read_pemasukan[(read_pemasukan['tanggal pemasukan'] >= batasawal) & (read_pemasukan['tanggal pemasukan'] <= batasakhir)]
                    total_pemasukan = filtereddate_pemasukan['uang masuk'].sum()
                except FileNotFoundError:
                    print("File 'pemasukan.csv' tidak ditemukan. Pemasukan diasumsikan Rp 0.")
                except KeyError as e:
                    print(f"Error: Kolom 'uang masuk' atau 'tanggal pemasukan' tidak ditemukan di 'pemasukan.csv': {e}. Pemasukan diasumsikan Rp 0.")
                except Exception as e:
                    print(f"Terjadi kesalahan saat membaca 'pemasukan.csv': {e}. Pemasukan diasumsikan Rp 0.")

                # --- Pengeluaran ---
                total_pengeluaran = 0
                try:
                    read_pengeluaran = pd.read_csv('pengeluaran.csv')
                    # Pastikan 'tanggal beli' adalah string sebelum mengonversi ke datetime
                    read_pengeluaran['tanggal beli'] = read_pengeluaran['tanggal beli'].astype(str)
                    read_pengeluaran['tanggal beli'] = pd.to_datetime(read_pengeluaran['tanggal beli'], format='%Y-%m-%d', errors='coerce')
                    
                    # Hapus baris di mana konversi tanggal gagal
                    read_pengeluaran.dropna(subset=['tanggal beli'], inplace=True)

                    filtereddate_pengeluaran = read_pengeluaran[(read_pengeluaran['tanggal beli'] >= batasawal) & (read_pengeluaran['tanggal beli'] <= batasakhir)]
                    total_pengeluaran = filtereddate_pengeluaran['harga'].sum()
                except FileNotFoundError:
                    print("File 'pengeluaran.csv' tidak ditemukan. Pengeluaran diasumsikan Rp 0.")
                except KeyError as e:
                    print(f"Error: Kolom 'harga' atau 'tanggal beli' tidak ditemukan di 'pengeluaran.csv': {e}. Pengeluaran diasumsikan Rp 0.")
                except Exception as e:
                    print(f"Terjadi kesalahan saat membaca 'pengeluaran.csv': {e}. Pengeluaran diasumsikan Rp 0.")
                
                print(f"\nRekap Laba Periode: {batasawal.strftime('%Y-%m-%d')} sampai {batasakhir.strftime('%Y-%m-%d')}")
                print(f"Total Pemasukan : Rp {total_pemasukan:,.2f}")
                print(f"Total Pengeluaran : Rp {total_pengeluaran:,.2f}")
                laba = total_pemasukan - total_pengeluaran
                print(f"Laba Bersih : Rp {laba:,.2f}")

            except ValueError as ve:
                print(f"Input tanggal tidak valid: {ve}. Pastikan format YYYY-MM-DD.")
            except Exception as e:
                print(f"Terjadi kesalahan saat menghitung laba: {e}.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '4':
            input_pengeluaran()

        elif pilihan == '5':
            print("Keluar dari menu estimasi laba dan aset.")
            break

        else:
            print("Input tidak valid, silakan pilih antara 1 sampai 4.")
            input("Tekan Enter untuk melanjutkan...")
            continue
        
def rekomendasi_tanaman():
    # Pastikan CSV ada atau buat dengan header yang sesuai
    # Menggunakan header yang konsisten dengan tambah_tanaman
    tanaman_headers = [
        "id tanaman", "nama tanaman", "stok", "jenis tanah", "musim",
        "value per kg", "jumlah per m^2 (kg)", "berat per satuan", 
        "fase persemaian", "fase pertumbuhan vegetatif", "fase pembungaan generatif", 
        "fase pembuahan", "fase pematangan", "fase panen"
    ]

    if not os.path.exists('tanaman.csv'):
        pd.DataFrame(columns=tanaman_headers).to_csv('tanaman.csv', index=False)
    
    if not os.path.exists('ladang.csv'):
        pd.DataFrame(columns=tanaman_headers).to_csv('ladang.csv', index=False)

    if not os.path.exists('gudang.csv'):
        pd.DataFrame(columns=tanaman_headers).to_csv('gudang.csv', index=False)

    try:
        daftar_tanaman = pd.read_csv('tanaman.csv')
        daftar_tanaman.columns = daftar_tanaman.columns.str.strip() # Bersihkan nama kolom
    except FileNotFoundError:
        print("Error: File 'tanaman.csv' tidak ditemukan. Harap tambahkan data tanaman terlebih dahulu.")
        input("Tekan Enter untuk kembali...")
        return
    except KeyError as e:
        print(f"Error membaca 'tanaman.csv': Kolom yang diharapkan tidak ada {e}. Harap periksa integritas file.")
        input("Tekan Enter untuk kembali...")
        return

    try:
        ladang = pd.read_csv('ladang.csv')
        ladang.columns = ladang.columns.str.strip()
    except FileNotFoundError:
        ladang = pd.DataFrame(columns=tanaman_headers)
        ladang.to_csv('ladang.csv', index=False)
    except KeyError as e:
        print(f"Error membaca 'ladang.csv': Kolom yang diharapkan tidak ada {e}.")
        input("Tekan Enter untuk kembali...")
        return

    try:
        gudang = pd.read_csv('gudang.csv')
        gudang.columns = gudang.columns.str.strip()
    except FileNotFoundError:
        gudang = pd.DataFrame(columns=tanaman_headers)
        gudang.to_csv('gudang.csv', index=False)
    except KeyError as e:
        print(f"Error membaca 'gudang.csv': Kolom yang diharapkan tidak ada {e}.")
        input("Tekan Enter untuk kembali...")
        return

    while True:
        clear_screen()
        print("\n=== Rekomendasi Tanaman ===")
        jenis_tanah_input = input("Masukkan jenis tanah: ").title().strip()
        musim_input = input("Masukkan musim: ").lower().strip()

        matching_plants = daftar_tanaman[
            (daftar_tanaman['jenis tanah'].astype(str).str.lower() == jenis_tanah_input.lower()) &
            (daftar_tanaman['musim'].astype(str).str.lower() == musim_input.lower())
        ]

        if not matching_plants.empty:
            print(f"\nTanaman yang cocok untuk jenis tanah '{jenis_tanah_input}' dan musim '{musim_input}':")
            display_cols = ["id tanaman", "nama tanaman", "jenis tanah", "musim", 
                            "stok", "value per kg", "jumlah per m^2 (kg)", "berat per satuan"]
            
            if all(col in matching_plants.columns for col in display_cols):
                print(tabulate(matching_plants[display_cols],
                            headers=["ID", "Nama", "Jenis Tanah", "Musim", "Stok (Unit)", "Value per KG", "Jumlah per m^2 (Kg)", "Berat per Satuan (Kg)"], 
                            tablefmt='grid', showindex=False))
            else:
                print("Beberapa kolom yang diharapkan untuk tampilan tidak ditemukan.")
                print(f"Kolom tersedia: {matching_plants.columns.tolist()}")
            break
        else:
            print(f"\nTidak ada tanaman yang cocok dengan jenis tanah '{jenis_tanah_input}' dan musim '{musim_input}'.")
            input("Tekan Enter untuk mencoba lagi...")
            continue 

    if matching_plants.empty:
        input("Tekan Enter untuk kembali ke menu utama...")
        return

    # --- Bagian untuk pilihan menanam ---
    while True:
        inputan_ditanam = input("Apakah anda ingin menanam tanaman tersebut? (y/n): ").lower().strip()
        if inputan_ditanam == 'y':
            while True: 
                input_id_tanaman = input("Masukkan ID tanaman yang ingin ditanam: ").upper().strip()
                selected_plant_info = daftar_tanaman[daftar_tanaman['id tanaman'] == input_id_tanaman]
                
                if selected_plant_info.empty:
                    print("ID tidak valid atau tidak ada dalam daftar tanaman Anda.\n")
                    continue
                else:
                    selected_plant_info = selected_plant_info.iloc[0]
                    break
            
            while True:
                try:
                    input_jumlah_tanaman_units = int(input(f"Masukkan jumlah yang ingin ditanam ({selected_plant_info.get('berat per satuan', 'N/A')} KG per unit) (Unit) : "))
                    
                    gudang['stok'] = pd.to_numeric(gudang['stok'], errors='coerce').fillna(0)
                    
                    current_gudang_stok = gudang.loc[gudang['id tanaman'] == input_id_tanaman, 'stok'].iloc[0] if input_id_tanaman in gudang['id tanaman'].values else 0
                    
                    if input_jumlah_tanaman_units <= 0:
                        print("Jumlah tanaman harus lebih dari 0.")
                        continue
                    elif input_jumlah_tanaman_units > current_gudang_stok:
                        print(f"Stok di gudang tidak cukup. Stok tersedia: {current_gudang_stok} unit.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Inputan harus berisi angka.")
                except IndexError:
                    print("Stok tanaman ini belum tercatat di gudang. Tidak dapat menanam.")
                    input_jumlah_tanaman_units = 0
                    break

                print("Jumlah tanaman berhasil dicatat untuk ditanam!")

                # --- Kurangi dari gudang.csv ---
                gudang.loc[gudang['id tanaman'] == input_id_tanaman, 'stok'] -= input_jumlah_tanaman_units
                gudang.to_csv('gudang.csv', index=False)
                print(f"Mengurangi {input_jumlah_tanaman_units} unit '{selected_plant_info['nama tanaman']}' dari gudang.")


                # --- Tambah ke ladang.csv ---
                ladang['stok'] = pd.to_numeric(ladang['stok'], errors='coerce').fillna(0)
                if input_id_tanaman in ladang['id tanaman'].values:
                    ladang.loc[ladang['id tanaman'] == input_id_tanaman, 'stok'] += input_jumlah_tanaman_units
                else:
                    new_ladang_row = selected_plant_info.copy() 
                    new_ladang_row['stok'] = input_jumlah_tanaman_units
                    new_ladang_row_df = pd.DataFrame([new_ladang_row.to_dict()], columns=ladang.columns)
                    ladang = pd.concat([ladang, new_ladang_row_df], ignore_index=True)

                ladang.to_csv('ladang.csv', index=False)
                print(f"Menambahkan {input_jumlah_tanaman_units} unit '{selected_plant_info['nama tanaman']}' ke ladang.")
            
            break 
        elif inputan_ditanam == 'n':
            print("Anda memilih untuk tidak menanam tanaman ini.")
            break
        else:
            print("Inputan tidak valid. Harap masukkan 'y' atau 'n'.")
    input("\nTekan Enter untuk kembali ke menu utama...")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def lihat_tanaman():
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip() # Bersihkan nama kolom
        if not df.empty:
            pagination_tanaman("tanaman.csv")
        else:
            print("Belum ada data tanaman.")
    except FileNotFoundError:
        print("File 'tanaman.csv' belum dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca atau menampilkan tanaman: {e}")
    input("\nTekan Enter untuk kembali...")

def tambah_tanaman():
    import pandas as pd

    tanaman_headers = [
        "id tanaman", "nama tanaman", "stok", "jenis tanah", "musim",
        "value per kg", "jumlah per m^2 (kg)", "berat per satuan", 
        "fase persemaian", "fase pertumbuhan vegetatif", "fase pembungaan generatif", 
        "fase pembuahan", "fase pematangan", "fase panen"
    ]

    # Coba baca tanaman.csv
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        df = pd.DataFrame(columns=tanaman_headers)
        df.to_csv("tanaman.csv", index=False)

    while True:
        id_tanaman = input("ID Tanaman: ").upper().strip()
        if not id_tanaman:
            print("ID tanaman tidak boleh kosong.")
            continue
        if id_tanaman in df["id tanaman"].values:
            print("ID tanaman sudah ada. Silakan masukkan ID lain.")
            continue
        break

    nama = input("Nama Tanaman: ").strip()
    while not nama:
        print("Nama tanaman tidak boleh kosong.")
        nama = input("Nama Tanaman: ").strip()

    stok = 0  # Stok awal default

    jenis_tanah = input("Jenis Tanah: ").strip().title()
    while not jenis_tanah:
        print("Jenis tanah tidak boleh kosong.")
        jenis_tanah = input("Jenis Tanah: ").strip().title()

    musim = input("Musim: ").strip().lower()
    while not musim:
        print("Musim tidak boleh kosong.")
        musim = input("Musim: ").strip().lower()

    def input_float(prompt):
        while True:
            try:
                val = float(input(prompt))
                if val < 0: raise ValueError
                return val
            except ValueError:
                print("Input harus angka positif.")

    def input_int(prompt):
        while True:
            try:
                val = int(input(prompt))
                if val < 0: raise ValueError
                return val
            except ValueError:
                print("Input harus angka bulat positif.")

    value = input_float("Value per kg (Rp): ")
    kg_per_m2 = input_float("Kg per m2 (hasil panen per meter persegi): ")
    berat_per_satuan = input_float("Berat per Satuan (Kg per unit/buah): ")

    fase_names = [
        "fase persemaian", "fase pertumbuhan vegetatif", "fase pembungaan generatif",
        "fase pembuahan", "fase pematangan", "fase panen"
    ]
    fase_values = [input_int(f"Jumlah hari untuk {f}: ") for f in fase_names]

    # Buat dict tanaman baru
    new_data = {
        "id tanaman": id_tanaman,
        "nama tanaman": nama,
        "stok": stok,
        "jenis tanah": jenis_tanah,
        "musim": musim,
        "value per kg": value,
        "jumlah per m^2 (kg)": kg_per_m2,
        "berat per satuan": berat_per_satuan,
        "fase persemaian": fase_values[0],
        "fase pertumbuhan vegetatif": fase_values[1],
        "fase pembungaan generatif": fase_values[2],
        "fase pembuahan": fase_values[3],
        "fase pematangan": fase_values[4],
        "fase panen": fase_values[5],
    }

    # Tambahkan ke tanaman.csv
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("tanaman.csv", index=False)
    print("Tanaman berhasil ditambahkan.")

    # Tambah ke gudang.csv
    try:
        gudang_df = pd.read_csv("gudang.csv")
        gudang_df.columns = gudang_df.columns.str.strip()
    except FileNotFoundError:
        gudang_df = pd.DataFrame(columns=tanaman_headers)

    if id_tanaman not in gudang_df["id tanaman"].values:
        new_gudang_entry = new_data.copy()
        new_gudang_entry["stok"] = 0
        gudang_df = pd.concat([gudang_df, pd.DataFrame([new_gudang_entry])], ignore_index=True)
        gudang_df.to_csv("gudang.csv", index=False)
        print(f"'{nama}' juga ditambahkan ke gudang.csv dengan stok awal 0.")

    # Tambah ke ladang.csv
    try:
        ladang_df = pd.read_csv("ladang.csv")
        ladang_df.columns = ladang_df.columns.str.strip()
    except FileNotFoundError:
        ladang_df = pd.DataFrame(columns=tanaman_headers)

    if id_tanaman not in ladang_df["id tanaman"].values:
        new_ladang_entry = new_data.copy()
        new_ladang_entry["stok"] = 0
        ladang_df = pd.concat([ladang_df, pd.DataFrame([new_ladang_entry])], ignore_index=True)
        ladang_df.to_csv("ladang.csv", index=False)
        print(f"'{nama}' juga ditambahkan ke ladang.csv dengan stok awal 0.")

    input("\nTekan Enter untuk kembali...")

def edit_stok_busuk():
    clear_screen()
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        print("File 'tanaman.csv' belum ada.")
        input("Tekan Enter untuk kembali...")
        return

    lihat_tanaman()
    id_edit = input("\nMasukkan ID tanaman yang stoknya busuk: ").upper().strip()
    
    if id_edit not in df["id tanaman"].values:
        print("ID tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return
    
    df['stok'] = pd.to_numeric(df['stok'], errors='coerce').fillna(0)

    current_stok = df.loc[df['id tanaman'] == id_edit, 'stok'].iloc[0]
    print(f"Stok saat ini: {current_stok} unit")
    
    while True:
        try:
            jumlah_busuk = int(input("Jumlah tanaman busuk (unit): "))
            if jumlah_busuk < 0:
                print("Jumlah busuk tidak boleh negatif.")
                continue
            if jumlah_busuk > current_stok:
                print(f"Jumlah busuk ({jumlah_busuk}) melebihi stok yang ada ({current_stok}).")
                continue
            break
        except ValueError:
            print("Input harus angka.")
    
    df.loc[df['id tanaman'] == id_edit, 'stok'] = current_stok - jumlah_busuk
    df.to_csv("tanaman.csv", index=False)

    gudang = pd.read_csv("gudang.csv")
    gudang.columns = gudang.columns.str.strip()
    gudang.loc[gudang['id tanaman'] == id_edit,'stok'] = current_stok - jumlah_busuk
    gudang.to_csv("gudang.csv", index=False)

    print("Stok di gudang dan di penyimpanan berhasil diperbarui.")
    input("\nTekan Enter untuk kembali...")


def hapus_tanaman():
    clear_screen()
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        print("File 'tanaman.csv' belum ada.")
        input("Tekan Enter untuk kembali...")
        return

    lihat_tanaman()
    id_hapus = input("\nMasukkan ID tanaman yang ingin dihapus: ").upper().strip()
    
    if id_hapus not in df["id tanaman"].values:
        print("ID tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    initial_rows = len(df)
    df = df[df['id tanaman'] != id_hapus]

    if len(df) < initial_rows:
        df.to_csv("tanaman.csv", index=False)
        print("Tanaman berhasil dihapus.")
        try:
            gudang_df = pd.read_csv("gudang.csv")
            gudang_df.columns = gudang_df.columns.str.strip()
            gudang_df = gudang_df[gudang_df['id tanaman'] != id_hapus]
            gudang_df.to_csv("gudang.csv", index=False)
            print(f"'{id_hapus}' juga dihapus dari gudang.csv.")
        except FileNotFoundError:
            pass 
        
        try:
            ladang_df = pd.read_csv("ladang.csv")
            ladang_df.columns = ladang_df.columns.str.strip()
            ladang_df = ladang_df[ladang_df['id tanaman'] != id_hapus]
            ladang_df.to_csv("ladang.csv", index=False)
            print(f"'{id_hapus}' juga dihapus dari ladang.csv.")
        except FileNotFoundError:
            pass
            
    else:
        print("ID tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")

def sort_tanaman():
    clear_screen()
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        print("File 'tanaman.csv' belum ada.")
        input("Tekan Enter untuk kembali...")
        return

    if df.empty:
        print("Tidak ada data untuk diurutkan.")
        input("Tekan Enter untuk kembali...")
        return

    print("""
=== SORTING ===
1. Nama Tanaman (A-Z)
2. Stok (terbesar-terkecil)
3. Value per Kg (tertinggi)
""")
    pilihan = input("Pilih: ").strip()
    
    if pilihan == "1":
        # Pastikan kolom 'nama tanaman' ada sebelum mengurutkan
        if 'nama tanaman' in df.columns:
            df_sorted = df.sort_values(by='nama tanaman', ascending=True)
        else:
            print("Kolom 'nama tanaman' tidak ditemukan.")
            input("Tekan Enter untuk kembali...")
            return
    elif pilihan == "2":
        # Pastikan kolom 'stok' ada dan numerik
        if 'stok' in df.columns:
            df['stok'] = pd.to_numeric(df['stok'], errors='coerce').fillna(0)
            df_sorted = df.sort_values(by='stok', ascending=False)
        else:
            print("Kolom 'stok' tidak ditemukan.")
            input("Tekan Enter untuk kembali...")
            return
    elif pilihan == "3":
        # Pastikan kolom 'value per kg' ada dan numerik
        if 'value per kg' in df.columns:
            df['value per kg'] = pd.to_numeric(df['value per kg'], errors='coerce').fillna(0)
            df_sorted = df.sort_values(by='value per kg', ascending=False)
        else:
            print("Kolom 'value per kg' tidak ditemukan.")
            input("Tekan Enter untuk kembali...")
            return
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")
        return

    print(tabulate(df_sorted, headers='keys', tablefmt="grid"))
    input("\nTekan Enter untuk kembali...")

def search_tanaman():
    clear_screen()
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        print("File 'tanaman.csv' belum ada.")
        input("Tekan Enter untuk kembali...")
        return

    if df.empty:
        print("Tidak ada data tanaman untuk dicari.")
        input("Tekan Enter untuk kembali...")
        return

    print("""
=== CARI TANAMAN ===
1. Berdasarkan ID
2. Berdasarkan Nama (mengandung)
""")
    opsi = input("Pilih: ").strip()
    hasil_df = pd.DataFrame() # Inisialisasi DataFrame kosong

    if opsi == "1":
        id_cari = input("Masukkan ID: ").upper().strip()
        hasil_df = df[df['id tanaman'].str.upper() == id_cari]
    elif opsi == "2":
        nama = input("Masukkan kata kunci nama: ").lower().strip()
        hasil_df = df[df['nama tanaman'].str.lower().str.contains(nama, na=False)]
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")
        return

    if not hasil_df.empty:
        print(tabulate(hasil_df, headers='keys', tablefmt="grid"))
    else:
        print("Data tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")

def perencanaan_maksimal():
    clear_screen()
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip() # Bersihkan nama kolom
    except FileNotFoundError:
        print("File tanaman.csv tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    if df.empty:
        print("Tidak ada data tanaman untuk perencanaan.")
        input("Tekan Enter untuk kembali...")
        return

    jenis_tanah_input = input("Masukkan jenis tanah lahan: ").strip().title()
    musim_input = input("Masukkan musim: ").strip().lower()
    
    while True:
        try:
            luas = float(input("Masukkan luas lahan (m2): "))
            if luas <= 0: raise ValueError
            break
        except ValueError:
            print("Luas lahan harus angka positif.")
    
    while True:
        try:
            planning_period = int(input("Masukkan periode perencanaan (hari): "))
            if planning_period <= 0: raise ValueError
            break
        except ValueError:
            print("Periode perencanaan harus angka positif.")

    rekomendasi = []
    for index, row in df.iterrows():
        # Pastikan tipe data benar sebelum perbandingan/perhitungan
        try:
            row_jenis_tanah = str(row['jenis tanah']).strip().title()
            row_musim = str(row['musim']).strip().lower()
        except AttributeError: # Tangani potensi NaN atau nilai non-string
            continue # Lewati baris jika konversi gagal

        if row_jenis_tanah == jenis_tanah_input and row_musim == musim_input:
            try:
                # Konversi kolom yang relevan ke numerik, tangani kesalahan
                kg_per_m2 = pd.to_numeric(row['jumlah per m^2 (kg)'], errors='coerce')
                value_per_kg = pd.to_numeric(row['value per kg'], errors='coerce')
                
                # Menjumlahkan hari fase, pastikan numerik
                cycle_days = sum([
                    pd.to_numeric(row['fase persemaian'], errors='coerce') or 0,
                    pd.to_numeric(row['fase pertumbuhan vegetatif'], errors='coerce') or 0,
                    pd.to_numeric(row['fase pembungaan generatif'], errors='coerce') or 0,
                    pd.to_numeric(row['fase pembuahan'], errors='coerce') or 0,
                    pd.to_numeric(row['fase pematangan'], errors='coerce') or 0,
                    pd.to_numeric(row['fase panen'], errors='coerce') or 0
                ])
                # cycle_days = sum([
                #     pd.to_numeric(row['fase persemaian'], errors='coerce').fillna(0),
                #     pd.to_numeric(row['fase pertumbuhan vegetatif'], errors='coerce').fillna(0),
                #     pd.to_numeric(row['fase pembungaan generatif'], errors='coerce').fillna(0),
                #     pd.to_numeric(row['fase pembuahan'], errors='coerce').fillna(0),
                #     pd.to_numeric(row['fase pematangan'], errors='coerce').fillna(0),
                #     pd.to_numeric(row['fase panen'], errors='coerce').fillna(0)
                # ])

                # Lewati jika ada nilai kritis yang NaN/0 setelah konversi
                if pd.isna(kg_per_m2) or pd.isna(value_per_kg) or kg_per_m2 == 0 or cycle_days == 0:
                    continue
                
                cycles = planning_period // cycle_days
                
                yield_per_cycle = kg_per_m2 * luas
                total_yield = yield_per_cycle * cycles
                estimated_income = total_yield * value_per_kg

                rekomendasi.append([
                    row['id tanaman'], row['nama tanaman'], int(cycle_days), cycles,
                    round(yield_per_cycle, 2), round(total_yield, 2), f'Rp {int(round(estimated_income)):,}' # Format pendapatan dengan rapi
                ])
            except (ValueError, TypeError):
                continue

    clear_screen()
    if not rekomendasi:
        print("Tidak ada tanaman yang cocok untuk kondisi lahan dan musim yang diberikan.")
    else:
        rekomendasi.sort(key=lambda x: int(x[6].replace('Rp ', '').replace(',', '')), reverse=True)
        print(tabulate(rekomendasi, headers=["ID", "Nama Tanaman", "Siklus (hari)", "Jumlah Siklus", "Hasil per Siklus (kg)", "Total Hasil (kg)", "Estimasi Income"], tablefmt="grid"))
    input("\nTekan Enter untuk kembali...")

def menu_tanaman():
    while True:
        clear_screen()
        print("""
=== MENU KELOLA TANAMAN ===
1. Lihat Daftar Tanaman
2. Tambah Tanaman Baru
3. Edit Stok (Karena Busuk)
4. Hapus Tanaman
5. Kembali ke Menu Utama
""")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == '1': clear_screen(); lihat_tanaman(); 
        elif pilihan == '2': clear_screen(); tambah_tanaman(); 
        elif pilihan == '3': clear_screen(); edit_stok_busuk(); 
        elif pilihan == '4': clear_screen(); hapus_tanaman(); 
        elif pilihan == '5': break
        else: print("Pilihan tidak valid."); input("Tekan Enter...")

def main():
    """
    Fungsi utama untuk menjalankan program AgriPlanner.
    """
    font_keren()
    print("\nSelamat Datang di AgriPlanner!")
    
    if not os.path.exists("user.csv"):
        print("\nBelum ada pengguna terdaftar. Silakan daftar terlebih dahulu.")
        register()
    
    current_logged_in_username = None
    while current_logged_in_username is None:
        print("\n=== Login / Register ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        choice = input("Pilih [1-3]: ").strip()

        if choice == '1':
            current_logged_in_username = login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Terima kasih, sampai jumpa!")
            return
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    while True:
        clear_screen()
        print(f"\nSelamat datang kembali, {current_logged_in_username}!")
        print("\n=== Menu Utama AgriPlanner ===")
        print("1. Kelola User")
        print("2. Kelola penyimpanan")
        print("3. Estimasi Laba dan Aset")
        print("4. Rekomendasi Tanaman")
        print("5. Perencanaan Hasil Maksimal")
        print("6. Logout")
        print("7. Exit")

        main_choice = input("Pilih menu [1-7]: ").strip()

        if main_choice == '1':
            kelola_user(current_logged_in_username)
            input("Tekan Enter untuk kembali ke layar login...")
        elif main_choice == '2':
            menu_tanaman()
        elif main_choice == '3': 
            estimasi_laba_dan_aset()
        elif main_choice == '4': 
            rekomendasi_tanaman()
        elif main_choice == '5':
            perencanaan_maksimal()
        elif main_choice == '6':
            current_logged_in_username = None
            print("Anda telah logout.")
            input("Tekan Enter untuk kembali ke layar login...")
            break
        elif main_choice == '8':
            print("Terima kasih telah menggunakan AgriPlanner!")
            return
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

main()
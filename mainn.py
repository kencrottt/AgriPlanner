import os
import pandas as pd
import pyfiglet
from tabulate import tabulate
from datetime import datetime
from datetime import date,timedelta
import math
import csv

# font = 'ansi_regular'
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
    os.system('cls')


def register():
    read_user = pd.read_csv("user.csv")
    while True:
        inputan_email = input("Masukkan Email : ")
        if inputan_email in read_user["email"].values:
            print("Email sudah terdaftar!")
            continue
        elif inputan_email == "":
            print("Email tidak boleh kosong!")
            continue
        else: 
            break
    
    while True:
        inputan_username = input("Masukkan Username : ")
        if inputan_username in read_user["username"].values:
            print("Username sudah terdaftar!")
            continue
        elif inputan_username == "":
            print("Username tidak boleh kosong!")
            continue
        else: 
            break
    
    while True:
        inputan_password = input("Masukkan Password : ")
        if inputan_password in read_user["password"].values:
            print("Password sudah terdaftar!")
            continue
        elif inputan_password == "":
            print("Password tidak boleh kosong!")
            continue
        else: 
            break

    while True:
        inputan_nama = input("Masukkan Nama : ")
        if inputan_nama in read_user["nama"].values:
            print("Nama sudah terdaftar!")
            continue
        elif inputan_nama == "":
            print("Nama tidak boleh kosong!")
            continue
        else: 
            break

    while True:
        inputan_jenis_tanah_dominan = input("Masukkan Jenis Tanah Dominan : ")
        if inputan_jenis_tanah_dominan == "":
            print("Nama tidak boleh kosong!")
            continue
        else: 
            break

    new_user = pd.DataFrame({
        "email": [inputan_email],
        "username": [inputan_username],
        "password": [inputan_password],
        "nama": [inputan_nama],
        "jenis_tanah_dominan": [inputan_jenis_tanah_dominan.title()]
        })
    read_user = pd.concat([read_user, new_user], ignore_index=True)
    read_user.to_csv("user.csv", index=False)
    print("Pendaftaran berhasil!")

def login():
    users = pd.read_csv('user.csv')
    while True:
        input_username = str(input("Masukkan Username : "))
        if input_username in users['username'].values:
            break
        else :
            print("Username belum terdaftar atau salah.")
            continue
        break
    #buat fitur lupa password
    while True:
        # print("Masukkan Password Akun : ")
        input_paswort = str(input("Masukkan Password : "))
        user_match = users[(users["username"] == input_username)]
        stored_password = user_match.iloc[0]["password"]
        if stored_password == input_paswort:
            global username
            username = user_match.iloc[0]["username"]
            nama_manggil = user_match.iloc[0]["nama"]
            print(f"Selamat datang, {nama_manggil}!")
            return
            break
        else:
            print("Password salah le.")
            continue


def kelola_user(username):

    print('Dashboard User')
    print('==============')
    print(f"Silahkan pilih menu.")
    print(f'''
1. Cek Biodata
2. Ubah Biodata
3. Keluar''')

    inputan1 = str(input())
    while True:
        if inputan1 == "1":
            akses = pd.read_csv('user.csv')
            buka_pd = akses[akses['username'] == username]
            
            print('============')
            print('Biodata User')
            print('============')
            email = buka_pd["email"].iloc[0]
            username_tampil = buka_pd["username"].iloc[0]
            nama = buka_pd["nama"].iloc[0]
            jenis_tanah_dominan = buka_pd["jenis_tanah_dominan"].iloc[0]

            print(f"Email       : {email}")
            print(f"Username    : {username_tampil}")
            print(f"Nama        : {nama}")
            print(f"Jenis Tanah : {jenis_tanah_dominan}")
            
        
        elif inputan1 == "2":
            try:
                akses = pd.read_csv('user.csv')
            except FileNotFoundError:
                print("File 'user.csv' tidak ditemukan.")
                return
            
            buka_pd = akses[akses['username'] == username]
            if buka_pd.empty:
                print("User tidak ditemukan.")
                return
            
            print('============')
            print('Biodata User')
            print('============')
            email = buka_pd["email"].iloc[0]
            username_tampil = buka_pd["username"].iloc[0]
            nama = buka_pd["nama"].iloc[0]
            jenis_tanah_dominan = buka_pd["jenis_tanah_dominan"].iloc[0]

            print(f"Email       : {email}")
            print(f"Username    : {username_tampil}")
            print(f"Nama        : {nama}")
            print(f"Jenis Tanah : {jenis_tanah_dominan}")
            
            input_lanjutan = input("Apakah anda ingin mengedit biodata anda? [y/t] ").lower()
            
            if input_lanjutan != 'y':
                print("Biodata tidak diubah.")
                return
            
            while True:
                print('''
                1. Email
                2. Username
                3. Nama
                4. Jenis Tanah
                ''')
                input_pilihan_edit = input("Data mana yang ingin anda ubah? ").strip()
                
                if input_pilihan_edit not in ['1', '2', '3', '4']:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    continue
                else:
                    break  # valid input, keluar dari loop

            kolom_map = {
                '1': 'email',
                '2': 'username',
                '3': 'nama',
                '4': 'jenis_tanah_dominan'
            }
            
            kolom_ubah = kolom_map[input_pilihan_edit]
            print(f"Perubahan {kolom_ubah.capitalize()}")
            print("===================")
            
            nilai_lama = buka_pd[kolom_ubah].iloc[0]
            print(f"Nilai lama: {nilai_lama}")
            
            nilai_baru = input(f"Masukkan nilai baru untuk {kolom_ubah}: ").strip()
            
            df = pd.read_csv('user.csv')
            df.loc[df['username'] == username, kolom_ubah] = nilai_baru
            
            if kolom_ubah == 'username':
                print("Username telah diubah, harap gunakan username baru untuk akses selanjutnya.")
            
            df.to_csv('user.csv', index=False)
            print(f"{kolom_ubah.capitalize()} berhasil diubah menjadi: {nilai_baru}")
                

        elif inputan1 == "3":
            print("Keluar dari program.")
            break

        else:
            print("Input tidak valid. Silahkan coba lagi.")
            continue

        lanjut = input("\nApakah Anda masih ingin mengakses menu kelola user? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Keluar dari program.")
            break
        

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

def input_pengeluaran():
    print("Input Pengeluaran")
    print("=================")
    while True:
        print('''
1. Tanaman
2. Biaya Produksi
        ''')
        input_kategori = str(input("\nPilih kategori pengeluaran : "))
        if input_kategori == '2':
            # print("geda")
            input_nama_pengeluaran = str(input("\nNama Pengeluaran : "))
            print("Nama pengeluaran tercatat!\n")
            while True:
                try:
                    input_harga = int(input("\nHarga : "))
                    if input_harga > 0:
                        print("Harga pengeluaran tercatat!\n")
                        break
                except ValueError:
                    print("Input harus berupa angka!\n")
                    continue
            while True:
                try:
                    input_jumlah = int(input("\nJumlah : "))
                    if input_jumlah > 0:
                        print("Jumlah pengeluaran tercatat!\n")
                        break
                except ValueError:
                    print("Input harus berupa angka!\n")
                    continue
            tanggal_beli = date.today()
                
            input_keterangan = str(input("Masukkan keterangan : "))
            daftar_pengeluaran = pd.read_csv("pengeluaran.csv")
            pengeluaran_baru = pd.DataFrame ([{
                'kategori' : "biaya produksi",
                'nama pengeluaran' : input_nama_pengeluaran,
                'harga' : int(input_harga),
                'jumlah' : int(input_jumlah),
                'keterangan' : input_keterangan,
                'tanggal beli' : tanggal_beli
            }])
        
            pengeluaran_baru = pd.concat([daftar_pengeluaran, pengeluaran_baru], ignore_index=True)
            pengeluaran_baru.to_csv('pengeluaran.csv', index=False)
            print("\nPengeluaran sudah tercatat!")
            break
        elif input_kategori == "1":
            daftar_pengeluaran = pd.read_csv("pengeluaran.csv")
            daftar_tanaman = pd.read_csv("tanaman.csv")
            di_gudang = pd.read_csv("gudang.csv")

            pagination_tanaman("tanaman.csv")

            while True:
                input_id_tanaman_pengeluaran = str(input("\nMasukkan ID tanaman yang dibeli : ")).upper()
                # hasil_cari = daftar_tanaman[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran].iloc[0]
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
                    input_jumlah_tanaman = int(input("Masukkan jumlah yang dibeli (KG) : ")) 
                    if input_jumlah_tanaman > 0:
                        print("Jumlah tanaman berhasil dicatat di stok!\n")
                        break
                except ValueError:
                    print("Inputan harus berisi angka.\n")
                    continue
            
            while True:
                try:
                    inputan_harga = int(input("Masukkan jumlah uang yang terpakai : "))
                    if inputan_harga > 0:
                        print("Harga berhasil dicatat di pengeluaran!\n")
                        break
                except ValueError:
                    print("Inputan harus berisi angka.\n")
                    continue
            tanggal_beli = date.today()

            inputan_keterangan = str(input("\nMasukkan keterangan (tulis - jika kosong) : "))
            print("Pengeluaran berhasil dicatat!")
            pengeluaran_baru = pd.DataFrame ([{
            'kategori' : "tanaman",
            'nama pengeluaran' : nama_pengeluaran,
            'harga' : inputan_harga,
            'jumlah' : input_jumlah_tanaman,
            'keterangan' : inputan_keterangan,
            'tanggal beli' : tanggal_beli
            }])
            pengeluaran_baru = pd.concat([daftar_pengeluaran, pengeluaran_baru], ignore_index=True)
            pengeluaran_baru.to_csv('pengeluaran.csv', index=False)     


            # ke csv tanaman
            #buat konfirmasi data weyy
            stok_lama = hasil_cari['stok']
            stok_baru = stok_lama + input_jumlah_tanaman
            daftar_tanaman.loc[daftar_tanaman['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'] = stok_baru
            daftar_tanaman.to_csv('tanaman.csv', index=False)
            
            # masuk ke gudang.csv
            stok_lama = hasil_cari['stok']
            stok_baru = stok_lama + input_jumlah_tanaman
            di_gudang.loc[di_gudang['id tanaman'] == input_id_tanaman_pengeluaran, 'stok'] = stok_baru
            di_gudang.to_csv('gudang.csv', index=False)
            break
                        
        else:
            print("Inputan tidak valid.")
            continue

# def estimasi_laba_dan_aset():
def estimasi_laba_dan_aset():
    while True:
        print("\n=== Menu Estimasi Laba dan Aset ===")
        print("1. Estimasi Aset Gudang")
        print("2. Estimasi Aset Ladang")
        print("3. Estimasi Laba")
        print("4. Keluar")

        pilihan = input("Pilih menu [1-4]: ").strip()

        if pilihan == '1':
            try:
                df = pd.read_csv('gudang.csv')

                df['estimated_profit'] = df['stok'] * df['berat per satuan'] * df['value per kg']

                total_estimated_profit = df['estimated_profit'].sum()

                print(f"Total Estimasi Laba Keseluruhan dari Semua Tanaman: Rp {total_estimated_profit:,.2f}")

            except FileNotFoundError:
                print(f"Error: File tidak ditemukan.")
            except KeyError as e:
                print(f"Error: Kolom yang diperlukan tidak ditemukan: {e}. Pastikan nama kolom di CSV sesuai (stok, berat per satuan, value per kg).")
            except Exception as e:
                print(f"Terjadi kesalahan lain: {e}")

        elif pilihan == '2':
            try:
                df = pd.read_csv('ladang.csv')

                df['estimated_profit'] = df['stok'] * df['berat per satuan'] * df['value per kg']

                total_estimated_profit = df['estimated_profit'].sum()

                print(f"Total Estimasi Laba Keseluruhan dari Semua Tanaman: Rp {total_estimated_profit:,.2f}")

            except FileNotFoundError:
                print(f"Error: File tidak ditemukan.")
            except KeyError as e:
                print(f"Error: Kolom yang diperlukan tidak ditemukan: {e}. Pastikan nama kolom di CSV sesuai (stok, berat per satuan, value per kg).")
            except Exception as e:
                print(f"Terjadi kesalahan lain: {e}")

        elif pilihan == '3':
            try:
                batasakhir = (input("Masukkan tanggal akhir rekap (format: YYYY-MM-DD): "))
                batasakhir = datetime.strptime(batasakhir, "%Y-%m-%d")

                batasawal = batasakhir - timedelta(days=30)

                try:
                    read_pemasukan = pd.read_csv('pemasukan.csv')
                    read_pemasukan['tanggal pemasukan'] = pd.to_datetime(read_pemasukan['tanggal pemasukan'], format='%Y-%m-%d', errors='coerce')
                except FileNotFoundError:
                    print("File 'pemasukan.csv' tidak ditemukan.")
                    continue
                except Exception as e:
                    print(f"Terjadi kesalahan saat membaca 'pemasukan.csv': {e}")
                    continue

                filtereddate = read_pemasukan[(read_pemasukan['tanggal pemasukan'] >= batasawal) & (read_pemasukan['tanggal pemasukan'] <= batasakhir)]
                total_pemasukan = filtereddate['uang masuk'].sum()

                try:
                    read_pengeluaran = pd.read_csv('pengeluaran.csv')
                    read_pengeluaran['tanggal beli'] = pd.to_datetime(read_pengeluaran['tanggal beli'], format='%Y-%m-%d', errors='coerce')
                except FileNotFoundError:
                    print("File 'pengeluaran.csv' tidak ditemukan.")
                    continue
                except Exception as e:
                    print(f"Terjadi kesalahan saat membaca 'pengeluaran.csv': {e}")
                    continue
                
                filtereddate = read_pengeluaran[(read_pengeluaran['tanggal beli'] >= batasawal) & (read_pengeluaran['tanggal beli'] <= batasakhir)]
                total_pengeluaran = filtereddate['harga'].sum()

                print(f"Tanggal {batasawal.date()} - {batasakhir.date()}")
                print(f"Total Pemasukan : Rp {total_pemasukan:,.2f}")
                print(f"Total Pengeluaran : Rp {total_pengeluaran:,.2f}")
                laba = total_pemasukan - total_pengeluaran
                print(f"Laba : Rp {laba:,.2f}")

            except ValueError as ve:
                print(f"Input tidak valid: {ve}. Silakan coba lagi.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")

        elif pilihan == '4':
            print("Keluar dari program.")
            break

        else:
            print("Input tidak valid, silakan pilih antara 1 sampai 4.")
            continue

        # konfirmasi
        lanjut = input("\nApakah Anda masih ingin mengakses menu estimasi laba? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Keluar dari program.")
            break


def rekomendasi_tanaman():
    def jump_search(arr, x):
        n = len(arr)
        step = int(math.sqrt(n))  # Optimal block size
        prev = 0

        # nyari blok yang ada targetnya, sesuai jumlah step
        while prev < n and arr[min(step, n) - 1] < x:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        # linear search ketika sudah ketemu targetnya di blok tsb
        for i in range(prev, min(step, n)):
            if arr[i] == x:
                return i

        return -1

    # Read the CSV file
    daftar_tanaman = pd.read_csv('tanaman.csv')
    ladang = pd.read_csv('ladang.csv')
    gudang = pd.read_csv('gudang.csv')
    while True:
        jenis_tanah_input = input("Masukkan jenis tanah: ").title()
        musim_input = input("Masukkan musim: ").lower()

        # ubah ke list dan tipe data string untuk dicari
        jenis_tanah_list = daftar_tanaman['jenis tanah'].astype(str).tolist()
        musim_list = daftar_tanaman['musim'].astype(str).tolist()

        # urutkan listnya agar bisa dijump search
        sorted_indices = sorted(range(len(jenis_tanah_list)), key=lambda k: (jenis_tanah_list[k], musim_list[k]))
        jenis_tanah_list = [jenis_tanah_list[i] for i in sorted_indices]
        musim_list = [musim_list[i] for i in sorted_indices]

        # lakukan jump search berdasarkan list jenis tanah dan inputannya
        index = jump_search(jenis_tanah_list, jenis_tanah_input)

        # kumpulkan yang benar pasangannya, masukkan dilist agar bisa dikomparasi.
        matching_indices = []
        while index != -1 and index < len(jenis_tanah_list) and jenis_tanah_list[index] == jenis_tanah_input:
        # pastikan jenis tanah yg sesuai dengan inputan punya musim yang sesuai juga. ketika cocok semua, masuk ke list matching_indices
            if musim_list[index] == musim_input:
                matching_indices.append(sorted_indices[index])
            index += 1
        #index += 1 agar loopingnya berjalan dan terus mencari

        # Display the results
        if matching_indices:
            print(f"\nTanaman yang cocok untuk jenis tanah '{jenis_tanah_input}' dan musim '{musim_input}':")
            hasil_df = daftar_tanaman.iloc[matching_indices]
            print(tabulate(hasil_df[["id tanaman", "nama tanaman","jenis tanah","musim", "stok", "value per kg", "jumlah per m^2 (kg)"]],
                        headers=["ID", "Nama","jenis tanah","musim", "Stok (KG)", "Value per KG", "Jumlah per m (Kg)", "Harga"], tablefmt='simple', showindex=False))
            break
        else:
            print(f"\nTidak ada tanaman yang cocok dengan jenis tanah '{jenis_tanah_input}' dan musim '{musim_input}'.")
            continue
    while True:
        inputan_ditanam = str(input("Apakah anda ingin menanam tanaman tersebut? (y/n) : ")).lower()
        if inputan_ditanam == 'y':
            input_id_tanaman = str(input("Masukkan ID tanaman yang ingin ditanam : ")).upper()
            hasil_cari = daftar_tanaman[daftar_tanaman['id tanaman'] == input_id_tanaman]
            if hasil_cari.empty:
                print("ID tidak valid atau tidak ada dalam daftar tanaman anda.\n")
                continue
            else:
                hasil_cari = hasil_cari.iloc[0]
                break
        elif inputan_ditanam == 'n':
            break
        else:
            print("Inputan tidak valid.")
            continue
    while True:
        try:
            input_jumlah_tanaman = int(input("Masukkan jumlah yang ditanam (KG) : "))
            if input_jumlah_tanaman > 0:
                print("Jumlah tanaman berhasil dicatat di stok!\n")
                break
        except ValueError as ve:
            print(f"Inputan tidak valid: {ve}. Silakan coba lagi.")
            continue
    stok_lama = hasil_cari['stok']
    stok_baru = stok_lama + input_jumlah_tanaman
    daftar_tanaman.loc[daftar_tanaman['id tanaman'] == input_id_tanaman, 'stok'] = stok_baru
    #update di csv tanaman
    daftar_tanaman.to_csv('tanaman.csv', index=False)

    hasil_cari2 = ladang[ladang['id tanaman'] == input_id_tanaman].iloc[0]
    #tambah ke ladang
    stok_lama_ladang = hasil_cari2['stok']
    ladang.loc[ladang['id tanaman'] == input_id_tanaman, 'stok'] = stok_baru_ladang
    ladang.to_csv('tanaman.csv', index=False)

    stok_baru_ladang = stok_lama_ladang + input_jumlah_tanaman
    #kurangi dari gudang
    hasil_cari3 = gudang[gudang['id tanaman'] == input_id_tanaman].iloc[0]
    stok_lama_gudang = hasil_cari3['stok']
    stok_baru_gudang = stok_lama_gudang - input_jumlah_tanaman
    gudang.loc[gudang['id tanaman'] == input_id_tanaman, 'stok'] = stok_baru_gudang
    gudang.to_csv('tanaman.csv', index=False)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def lihat_tanaman():
    try:
        with open("tanaman.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                pagination_tanaman('tanaman.csv')
            else:
                print("Belum ada data tanaman.")
    except FileNotFoundError:
        print("File belum dibuat.")

def tambah_tanaman():
    # Definisikan header yang konsisten untuk tanaman.csv
    tanaman_headers = [
        "id tanaman", "nama tanaman", "stok", "jenis tanah", "musim",
        "value per kg", "jumlah per m^2 (kg)", "berat per satuan", 
        "fase persemaian", "fase pertumbuhan vegetatif", "fase pembungaan generatif", 
        "fase pembuahan", "fase pematangan", "fase panen"
    ]
    
    try:
        df = pd.read_csv("tanaman.csv")
        df.columns = df.columns.str.strip()
    except FileNotFoundError:
        df = pd.DataFrame(columns=tanaman_headers)
        df.to_csv("tanaman.csv", index=False) # Buat file dengan header

    # Baca lagi dengan kolom bersih
    df = pd.read_csv("tanaman.csv")
    df.columns = df.columns.str.strip()

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

    # Stok awal biasanya 0 saat menambahkan jenis tanaman baru, Anda membelinya nanti
    stok = 0 
    
    jenis_tanah = input("Jenis Tanah: ").strip().title()
    while not jenis_tanah:
        print("Jenis tanah tidak boleh kosong.")
        jenis_tanah = input("Jenis Tanah: ").strip().title()

    musim = input("Musim: ").strip().lower()
    while not musim:
        print("Musim tidak boleh kosong.")
        musim = input("Musim: ").strip().lower()

    while True:
        try:
            value = float(input("Value per kg (Rp): "))
            if value < 0: raise ValueError
            break
        except ValueError:
            print("Value per kg harus angka positif.")
    
    while True:
        try:
            kg_per_m2 = float(input("Kg per m2 (hasil panen per meter persegi): "))
            if kg_per_m2 < 0: raise ValueError
            break
        except ValueError:
            print("Kg per m2 harus angka positif.")

    while True:
        try:
            berat_per_satuan = float(input("Berat per Satuan (Kg per unit/buah): "))
            if berat_per_satuan < 0: raise ValueError
            break
        except ValueError:
            print("Berat per satuan harus angka positif.")

    fase_names = [
        "fase persemaian", "fase pertumbuhan vegetatif", "fase pembungaan generatif",
        "fase pembuahan", "fase pematangan", "fase panen"
    ]
    fase_values = []
    for f in fase_names:
        while True:
            try:
                val = int(input(f"Jumlah hari untuk {f}: "))
                if val < 0: raise ValueError
                fase_values.append(val)
                break
            except ValueError:
                print("Input harus angka positif untuk fase.")


    new_row = pd.DataFrame([{
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
        "fase panen": fase_values[5]
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("tanaman.csv", index=False)
    print("Tanaman berhasil ditambahkan.")

    # Secara opsional, tambahkan juga ke gudang.csv dengan stok 0 pada awalnya jika itu jenis baru
    try:
        gudang_df = pd.read_csv("gudang.csv")
        gudang_df.columns = gudang_df.columns.str.strip()
    except FileNotFoundError:
        gudang_df = pd.DataFrame(columns=tanaman_headers)
    
    if id_tanaman not in gudang_df["id tanaman"].values:
        new_gudang_entry = new_row.copy()
        new_gudang_entry['stok'] = 0 # Mulai dengan stok 0 di gudang
        # Pastikan kolom yang ditambahkan konsisten
        new_gudang_entry_df = pd.DataFrame([new_gudang_entry.to_dict()], columns=gudang_df.columns)
        gudang_df = pd.concat([gudang_df, new_gudang_entry_df], ignore_index=True)
        gudang_df.to_csv("gudang.csv", index=False)
        print(f"'{nama}' juga ditambahkan ke gudang.csv dengan stok awal 0.")
    
    # Lakukan hal yang sama untuk ladang.csv
    try:
        ladang_df = pd.read_csv("ladang.csv")
        ladang_df.columns = ladang_df.columns.str.strip()
    except FileNotFoundError:
        ladang_df = pd.DataFrame(columns=tanaman_headers)

    if id_tanaman not in ladang_df["id tanaman"].values:
        new_ladang_entry = new_row.copy()
        new_ladang_entry['stok'] = 0 # Mulai dengan stok 0 di ladang
        # Pastikan kolom yang ditambahkan konsisten
        new_ladang_entry_df = pd.DataFrame([new_ladang_entry.to_dict()], columns=ladang_df.columns)
        ladang_df = pd.concat([ladang_df, new_ladang_entry_df], ignore_index=True)
        ladang_df.to_csv("ladang.csv", index=False)
        print(f"'{nama}' juga ditambahkan ke ladang.csv dengan stok awal 0.")
    
    input("\nTekan Enter untuk kembali...")

# tambah_tanaman()

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

# rekomendasi_tanaman()
pagination_tanaman("tanaman.csv")
import time
import os
import random

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('clear')  # Untuk Linux/MacOS
    # os.system('cls')  # Uncomment untuk Windows

# Warna untuk styling teks
MERAH = '\033[31m'
HIJAU = '\033[32m'
KUNING = '\033[33m'
BIRU = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
PUTIH = '\033[37m'
RESET = '\033[0m'

# Fungsi untuk menampilkan logo
def print_logo():
    logo = f"""
    {MAGENTA}
    ⠉⠉⠉⠉⠁⠀⠀⠀⠀⠒⠂⠰⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠀⠐⠒⠒⠀⠀⠈⠉⠉⠉⠉⢉⣉⣉⣉⣙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠒⠒⠉⠁⠀⠀⠀⠀⠳⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠉⠛⠛⠶⢦⣤⡐⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⢳⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠳⠶⢶⣦⠤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠉⠑⢄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀
    ===================================================================
    ================ WELCOME TO THE WA HACK TOOL =======================
    ===================================================================
    {RESET}
    """
    print(logo)

# Fungsi untuk menampilkan menu
def display_menu():
    print(HIJAU + """
    ┌────────────────────────────────────────────────────────┐
    │                   MAIN MENU                            │
    ├────────────────────────────────────────────────────────┤
    │ 1: LOGIN RPL                                           │
    │ 2: HACK SATELIT                                        │
    │ 3: HACK HP ORANG PAKE NOMER WA                         │
    │ 4: Gabut Mode (Dapet Inspirasi)                        │
    │ 5: HACK WA                                             │
    │ 6: HACK IPHONE                                         │
    │ 7: CPU OVERLOAD                                        │
    │ 8: SIMULATE WIFI HACKING                               │
    │ 9: EXIT                                                │
    └────────────────────────────────────────────────────────┘
    """ + RESET)

# Fungsi untuk melakukan "hack target"
def hack_target():
    target_number = input(f"{CYAN}[Hack WA] {RESET} Masukkan nomor WA target (misalnya: +628xxxxxxxxxx): ")
    print(f"{HIJAU}Mencoba mengakses data untuk nomor: {target_number}...{RESET}")
    loading_effect("Mengeksekusi proses...", 3)
    print(f"{MAGENTA}[INFO] {RESET} Akses ke nomor {target_number} berhasil.\n")
    print(f"{CYAN}[WARNING] {RESET} Harap diingat bahwa ini hanya hiburan! Jangan gunakan untuk tujuan ilegal.")

# Fungsi untuk melakukan hacking iphone (simulasi)
def hack_iphone():
    print(f"{CYAN}[HACK IPHONE] {RESET}")
    target_iphone = input("Masukkan nomor iPhone target (misalnya: +628xxxxxxxxxx): ")
    print(f"{HIJAU}Mencoba mengakses iPhone: {target_iphone}...{RESET}")
    loading_effect("Mengeksekusi proses...", 3)
    print(f"{MAGENTA}[INFO] {RESET} Akses ke iPhone {target_iphone} berhasil.\n")
    print(f"{CYAN}[WARNING] {RESET} Harap diingat bahwa ini hanya hiburan! Jangan gunakan untuk tujuan ilegal.")

# Fungsi untuk menampilkan efek loading
def loading_effect(message, duration):
    print(f"{CYAN}[INFO] {RESET} {message}")
    for i in range(3):
        time.sleep(duration / 3)
        print(f"{CYAN}[INFO] {RESET} {'.' * (i + 1)}", end="\r")
    print(f"{CYAN}[INFO] {RESET} Selesai!")

# Fungsi untuk keluar dari program
def exit_program():
    print(f"{CYAN}[EXIT] {RESET} Terima kasih telah menggunakan WA Hack Tool. Sampai jumpa!")
    time.sleep(2)
    exit()

# Fungsi utama untuk menjalankan program
def main():
    clear_screen()
    print_logo()
    while True:
        display_menu()
        choice = input(f"{HIJAU}[Pilih menu (1-9)] {RESET}")
        if choice == "1":
            print(f"{CYAN}[LOGIN] {RESET}")
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            if username == "admin" and password == "admin123":
                print(f"{HIJAU}Login berhasil!{RESET}")
            else:
                print(f"{MERAH}Login gagal. Coba lagi.{RESET}")
        elif choice == "2":
            print(f"{CYAN}[Hack Satelit] {RESET}")
            loading_effect("Mencoba terhubung dengan satelit...", 3)
        elif choice == "3":
            hack_target()  # Menjalankan fungsi untuk hack WA
        elif choice == "4":
            print(f"{CYAN}[Gabut Mode] {RESET}")
            print("Dapatkan inspirasi!")
            time.sleep(1)
            print(f"{CYAN}Motivasi: {RESET} Setiap kegagalan adalah pelajaran.")
        elif choice == "5":
            print(f"{CYAN}[System Status] {RESET} Semua sistem berjalan dengan baik.")
        elif choice == "6":
            hack_iphone()  # Menjalankan fungsi untuk hack iPhone
        elif choice == "7":
            print(f"{CYAN}[CPU Overload] {RESET} CPU mengalami overload sementara. Mengatur ulang.")
            time.sleep(1)
        elif choice == "8":
            print(f"{CYAN}[WiFi Hack] {RESET} Melakukan percakapan WiFi.")
        elif choice == "9":
            exit_program()  # Menjalankan fungsi untuk keluar dari program
        else:
            print(f"{MERAH}Pilihan tidak valid, coba lagi.{RESET}")
        time.sleep(1)  # Pause sebelum menampilkan menu lagi

if __name__ == "__main__":
    main()

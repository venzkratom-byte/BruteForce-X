import os
import sys
import time
import random
from tqdm import tqdm
from rich import print, box
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

HARDCODED_EMAIL = "mojoofficial16@gmail.com", "jonathanadvent766@gmail.com"
HARDCODED_PASSWORD = "mojo1212", "jonathan1212022005"
HASIL_FILE = "hasil.txt"
WORDLIST_FILE = "wordlist.txt"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    font = '''\
[red bold]
██████  ██████  ██    ██ ████████ ███████ ███████  ██████  ██████   ██████ ███████       ██   ██ 
██   ██ ██   ██ ██    ██    ██    ██      ██      ██    ██ ██   ██ ██      ██             ██ ██  
██████  ██████  ██    ██    ██    █████   █████   ██    ██ ██████  ██      █████   █████   ███   
██   ██ ██   ██ ██    ██    ██    ██      ██      ██    ██ ██   ██ ██      ██             ██ ██  
██████  ██   ██  ██████     ██    ███████ ██       ██████  ██   ██  ██████ ███████       ██   ██
[/red bold]

[magenta bold]
██████  ██    ██     ███    ███  ██████       ██  ██████                                         
██   ██  ██  ██      ████  ████ ██    ██      ██ ██    ██                                        
██████    ████       ██ ████ ██ ██    ██      ██ ██    ██                                        
██   ██    ██        ██  ██  ██ ██    ██ ██   ██ ██    ██                                        
██████     ██        ██      ██  ██████   █████   ██████ 
[/magenta bold]'''
    print(font)

def loading_install():
    clear()
    print_logo()
    print(Panel.fit(
        "[yellow]Silakan tunggu, sistem sedang melakukan inisialisasi dan persiapan tools...[/yellow]",
        title="[bold cyan]Instalasi BruteForce-X[/bold cyan]", box=box.ROUNDED, border_style="cyan"))
    steps = [
        "Memverifikasi dependensi sistem...",
        "Menginstal modul keamanan lanjutan...",
        "Menghubungkan ke server brute force...",
        "Menghasilkan wordlist dinamis...",
        "Mengoptimasi performa engine...",
        "Menyiapkan antarmuka pengguna...",
        "Finalisasi proses instalasi..."
    ]
    time.sleep(0.6)
    for step in steps:
        print(f"[magenta]{step}[/magenta]")
        for _ in tqdm(range(random.randint(18, 36)), desc=f"  ☠️ {step}", ncols=70,
                      bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
                      ascii="☠️ "):
            time.sleep(0.022 + random.uniform(0.008, 0.02))
        time.sleep(0.33)
    print("\n[green bold]✔ Instalasi berhasil! Sistem siap digunakan.[/]\n")
    time.sleep(1.1)
def show_logo():
    clear()
    print_logo()
    print(
        Panel.fit(
            "[bold red]BruteForce-X  -  Tools Brute Force Multi Target Tingkat Profesional[/bold red]\n"
            "[white]Pengembang : [cyan]Anonymous - Mojo[/cyan]\n"
            "Versi      : [cyan]1.0[/cyan]\n"
            "Github     : [cyan]https://github.com/Anonymous-Int[/cyan][/white]\n\n"
            "[yellow]PERINGATAN: Gunakan tools ini hanya untuk pengujian dan pembelajaran keamanan pada sistem milik sendiri!\n"
            "Segala bentuk penyalahgunaan untuk akses ilegal merupakan [bold red]TANGGUNG JAWAB PENGGUNA![/bold red][/yellow]",
            box=box.DOUBLE, border_style="red", padding=(1, 3))
    )
def menu():
    print(
        Panel.fit(
            "[cyan bold]MENU UTAMA[/cyan bold]\n\n"
            "[white][1] Brute Force Berdasarkan Target Email\n"
            "[2] Brute Force Password Mirip/Lupa (Partial Search)\n"
            "[3] Informasi & Dokumentasi Tools\n"
            "[4] Keluar dari Tools[/white]\n",
            box=box.ROUNDED, border_style="cyan", padding=(1,3)
        )
    )
def info_tools():
    print(
        Panel.fit(
            "[green]\n"
            "BruteForce-X merupakan alat profesional untuk simulasi brute force password berbasis wordlist, yang telah digunakan oleh para praktisi keamanan informasi.\n\n"
            "- Mode brute force target: menemukan password valid berdasarkan email target.\n"
            "- Mode brute force mirip/lupa: mencari password yang mengandung kata/frasa tertentu.\n"
            "- Hasil eksekusi otomatis dicatat pada file hasil.txt.\n"
            "- Rekomendasi: Gunakan wordlist minimal 600+ entry (lihat file wordlist.txt).\n"
            "[/green]",
            title="[bold green]INFORMASI TOOLS[/bold green]", box=box.ROUNDED, border_style="green"
        )
    )
def open_hasil_file():
    is_termux = 'com.termux' in os.environ.get('PREFIX', '') or 'ANDROID_ROOT' in os.environ
    if is_termux:
        return
    try:
        if os.name == 'nt':
            import subprocess
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 6  # SW_MINIMIZE = 6
            subprocess.Popen(["notepad.exe", HASIL_FILE], startupinfo=startupinfo)
        elif sys.platform.startswith('linux'):
            os.system(f'xdg-open "{HASIL_FILE}" > /dev/null 2>&1 &')
        elif sys.platform == "darwin":
            os.system(f'open "{HASIL_FILE}"')
    except Exception as e:
        pass

def brute_force_loading_effect():
    loading_texts = [
        "[cyan]Mengacak session brute...[/cyan]",
        "[cyan]Membuka koneksi ke host target...[/cyan]",
        "[magenta]Menyiapkan attack vector canggih...[/magenta]",
        "[magenta]Mencocokkan fingerprint dan validasi sistem target...[/magenta]",
        "[yellow]Memproses wordlist.txt untuk eksekusi...[/yellow]",
        "[yellow]Melakukan enkripsi payload brute force...[/yellow]",
        "[green]Menginisialisasi worker attack otomatis...[/green]",
        "[green]Simulasi bypass dan anti-limit server...[/green]",
        "[bold blue]Brute force engine aktif...[/bold blue]",
        "[bold cyan]Eksekusi proses brute force dimulai...[/bold cyan]",
    ]
    for i, teks in enumerate(loading_texts):
        print(Panel(teks, border_style="magenta" if i%2 else "cyan", box=box.MINIMAL))
        time.sleep(0.6 + random.uniform(0.2, 0.5))
    with Progress(
        SpinnerColumn(style="magenta"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Inisialisasi engine brute force...[/cyan]", total=40)
        for _ in range(40):
            time.sleep(0.08 + random.uniform(0.01, 0.04))
            progress.advance(task)
def brute_force_target():
    clear()
    show_logo()
    print(Panel("[bold yellow]=== MODE BRUTE FORCE BERDASARKAN EMAIL TARGET ===[/bold yellow]", border_style="yellow"))
    print("[cyan]  > Masukkan Email Target: [/cyan]", end="")
    email = input().strip()
    brute_force_loading_effect()
    print("\n[magenta][!] Proses brute force dimulai, sistem sedang menganalisis password...[/magenta]")
    time.sleep(1.1)
    if not os.path.exists(WORDLIST_FILE):
        print(Panel("[red][!] File wordlist.txt tidak ditemukan. Silakan buat wordlist.txt pada direktori yang sama![/red]", border_style="red"))
        input("\nTekan ENTER untuk kembali ke menu utama")
        return
    with open(WORDLIST_FILE, "r", encoding="utf-8") as f:
        wordlist = [i.strip() for i in f if i.strip()]
    found = False
    with Progress(
        SpinnerColumn(style="cyan"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20),
        TextColumn("[green]{task.completed}/{task.total} password diuji"),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("[bold yellow]Menjalankan pengujian brute force password...[/bold yellow]", total=len(wordlist))
        for idx, pwd in enumerate(wordlist):
            time.sleep(0.018 + random.uniform(0.005, 0.012))
            progress.advance(task)
            if email == HARDCODED_EMAIL and pwd == HARDCODED_PASSWORD:
                found = True
                break
    if found:
        print(Panel(
            f"[green bold]✔ AUTENTIKASI BERHASIL![/green bold]\n\n[cyan]Email   : {email}\nPassword: {HARDCODED_PASSWORD}[/cyan]",
            border_style="green", box=box.DOUBLE))
        with open(HASIL_FILE, "w", encoding="utf-8") as out:
            out.write(f"EMAIL   : {email}\nPASSWORD: {HARDCODED_PASSWORD}\n")
        print(Panel(f"[green]Hasil brute force telah tersimpan di file: {HASIL_FILE}[/green]", border_style="green"))
        open_hasil_file()
    else:
        print(Panel(
            f"[red bold]✘ PASSWORD untuk email {email} TIDAK BERHASIL ditemukan di wordlist ({len(wordlist)} data)![/red bold]",
            border_style="red", box=box.ROUNDED))
        with open(HASIL_FILE, "w", encoding="utf-8") as out:
            out.write(f"EMAIL   : {email}\nPASSWORD: [TIDAK DITEMUKAN]\n")
        open_hasil_file()
    input("\nTekan ENTER untuk kembali ke menu utama")

def brute_force_lupa():
    clear()
    show_logo()
    print(Panel("[bold yellow]=== MODE BRUTE FORCE PASSWORD MIRIP/LUPA ===[/bold yellow]", border_style="yellow"))
    print("[cyan]  > Masukkan Kata/Karakter yang Diingat (contoh: sandi, 123, nama): [/cyan]", end="")
    target_partial = input().strip().lower()
    print(Panel(f"[magenta][!] Sistem mencari password yang mengandung/mirip dengan: {target_partial}[/magenta]", border_style="magenta"))
    time.sleep(0.9)
    if not os.path.exists(WORDLIST_FILE):
        print(Panel("[red][!] File wordlist.txt tidak ditemukan. Silakan buat wordlist.txt pada direktori yang sama![/red]", border_style="red"))
        input("\nTekan ENTER untuk kembali ke menu utama")
        return
    with open(WORDLIST_FILE, "r", encoding="utf-8") as f:
        wordlist = [i.strip() for i in f if i.strip()]
    results = []
    with Progress(
        SpinnerColumn(style="magenta"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20),
        TextColumn("[green]{task.completed}/{task.total} password diperiksa"),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("[bold yellow]Menganalisis kemiripan password...[/bold yellow]", total=len(wordlist))
        for idx, pwd in enumerate(wordlist):
            time.sleep(0.009 + random.uniform(0.003, 0.009))
            progress.advance(task)
            if target_partial in pwd.lower():
                results.append(pwd)
    if results:
        print(Panel(
            f"[green bold]✔ Ditemukan {len(results)} password yang mengandung kata '{target_partial}':[/green bold]\n\n" +
            '\n'.join([f"[cyan]{p}[/cyan]" for p in results]), border_style="green", box=box.DOUBLE))
        with open(HASIL_FILE, "w", encoding="utf-8") as out:
            out.write(f"Keyword: {target_partial}\n")
            for pwd in results:
                out.write(pwd+"\n")
        print(Panel(f"[green]Daftar password hasil pencarian disimpan pada file: {HASIL_FILE}[/green]", border_style="green"))
        open_hasil_file()
    else:
        print(Panel(
            f"[red bold]✘ Tidak ditemukan password yang mengandung '{target_partial}' di wordlist![/red bold]",
            border_style="red", box=box.ROUNDED))
        with open(HASIL_FILE, "w", encoding="utf-8") as out:
            out.write(f"Keyword: {target_partial}\n[Hasil tidak ditemukan]")
        open_hasil_file()
    input("\nTekan ENTER untuk kembali ke menu utama")

def main():
    loading_install()
    while True:
        show_logo()
        menu()
        print("Silakan pilih menu [1/2/3/4]:", end=" ")
        pilihan = input().strip()
        if pilihan == "1":
            brute_force_target()
        elif pilihan == "2":
            brute_force_lupa()
        elif pilihan == "3":
            clear()
            show_logo()
            info_tools()
            input("\nTekan ENTER untuk kembali ke menu utama")
        elif pilihan == "4":
            print("\n[green bold]Terima kasih telah menggunakan BruteForce-X. Sampai jumpa di project selanjutnya![/green bold]\n")
            time.sleep(1.2)
            break
        else:
            print(Panel("[red bold][!] Pilihan tidak valid, silakan coba lagi.[/red bold]", border_style="red"))
            time.sleep(1.1)

if __name__ == "__main__":
    main()

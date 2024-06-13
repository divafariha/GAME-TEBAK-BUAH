import pygame
import sys
import random

# Inisialisasi pygame
pygame.init()

# Pengaturan jendela
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Menebak Buah")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 205, 0)
BLUE = (0, 0, 255)

# Daftar kata
kata_kunci = ["APEL", "ANGGUR", "PISANG", "SEMANGKA", "JERUK", "MANGGA", "NANAS", "ALPUKAT", "MANGGIS", "DURIAN"]

# Pustaka untuk memuat gambar
def load_image(file_name):
    image = pygame.image.load(file_name)
    return image.convert_alpha()

# Memuat gambar untuk setiap kata kunci
gambar_buah_dict = {}
for kata in kata_kunci:
    gambar_buah = load_image(kata + ".png")
    gambar_buah_dict[kata] = pygame.transform.scale(gambar_buah, (380, 380))

# Pilih kata secara acak
kata_tebak = random.choice(kata_kunci)

# Fungsi untuk menampilkan teks di tengah layar
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Fungsi untuk menampilkan waktu dan skor
def tampilkan_waktu_skor(waktu, skor):
    display_text("Waktu: " + str(round(waktu)), font , BLACK, 700, 50)
    display_text("Skor: " + str(skor), font, BLACK, 700, 100)

# Font
font = pygame.font.Font(None, 42)

# Inisialisasi variabel
tebakan = ""
tebakan_benar = False
waktu = 120  # Atur waktu awal dalam detik
skor = 0

# Pustaka untuk memuat gambar latar belakang
def load_background(file_name):
    return pygame.image.load(file_name)

# Memuat gambar latar belakang
background = load_background("BACKGROUND2.png")  # Ganti dengan nama file latar belakang Anda
background = pygame.transform.scale(background, window_size)  # Menyesuaikan latar belakang dengan ukuran jendela

clock = pygame.time.Clock()  # Inisialisasi clock

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if tebakan.upper() == kata_tebak:
                    tebakan_benar = True
                    display_text("BENARR", font, GREEN, 400, 180)
                    pygame.display.flip()
                    pygame.time.wait(500)
                else:
                    tebakan = ""
                    display_text("JAWABAN SALAH!!", font, RED, 400, 180)
                    pygame.display.flip()
                    pygame.time.wait(1500)

            elif event.key == pygame.K_BACKSPACE:
                tebakan = tebakan[:-1]
            else:
                tebakan += event.unicode


    # Menampilkan latar belakang
    screen.blit(background, (0, 0))

    display_text("Tebak Buah: " + tebakan, font, BLACK, 400, 130)

    if tebakan_benar:
        skor += 10  # Tambahkan skor jika tebakan benar
        # Menghapus kata yang sudah dijawab dari daftar kata_kunci
        kata_kunci.remove(kata_tebak)
        if not kata_kunci:
            display_text("Skor Akhir: " + str(skor), font, BLACK, 400, 300)
            display_text("Selamat, Anda Menyelesaikan Game Tebak Buah :)", font, BLACK, 400, 200)
            pygame.display.flip()
            pygame.time.wait(10000)  # Tunggu 10 detik sebelum keluar
            pygame.quit()
            sys.exit()
        # Memilih kata baru
        kata_tebak = random.choice(kata_kunci)
        tebakan_benar = False
        # Mereset tebakan
        tebakan = ""
    else:
        display_text("BUAH  " + "_ " * len(kata_tebak), font, BLACK, 400, 90)

    tampilkan_waktu_skor(waktu, skor)  # Tampilkan waktu dan skor

    # Menampilkan gambar buah
    buah_gambar = gambar_buah_dict[kata_tebak]
    buah_gambar_rect = buah_gambar.get_rect(center=(400, 370))
    screen.blit(buah_gambar, buah_gambar_rect)

    # Kurangi waktu
    waktu -= 1.5/60  # Kurangi waktu sebanyak 1.5 detik setiap 60 frame

    # Jika waktu habis atau sudah menjawab semua buah, tampilkan skor akhir
    if waktu <= 0 or not kata_kunci:
        screen.blit(background, (0, 0))  # Tampilkan latar belakang
        display_text("Skor Akhir: " + str(skor), font, BLACK, 400, 300)
        display_text("Selamat, Anda Menyelesaikan Game Tebak Buah :)", font, BLACK, 400, 200)
        pygame.display.flip()
        pygame.time.wait(10000)  # Tunggu 10 detik sebelum keluar
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(60)  # Atur frame rate (60 FPS)

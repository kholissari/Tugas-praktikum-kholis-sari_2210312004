import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada pagi hari, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada sore hari, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada malam hari, ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Rina sedang masak ")
if karakter == 2 :
    kalimat_2 = ("Rina sedang makan ")
if karakter == 3 :
    kalimat_2 = ("Rina sedang membaca ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("dan pada hari sabtu hari ini ia bersantai")
if waktu == 2 :
    kalimat_3 = ("dan pada hari minggu hari ini ia sedang menonton ")
if waktu == 3 :
    kalimat_3 = ("dan pada hari senin ini sedang membersihkan kamar ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("karena hari libur, ")
if story_plot == 2 :
    kalimat_4 = ("karena ia sedang tidak sibuk, ")
if story_plot == 3 :
    kalimat_4 = ("karena tidak ada hal yang dia lakukan, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("ia mengerjakanya di dapur, ")
if tempat == 2 :
    kalimat_5 = ("ia mengerjakan di tengah rumah, ")
if tempat == 3 :
    kalimat_5 = ("ia mengerjakan di kamar, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("sedangkan ayah membaca komik")
if second_character == 2 :
    kalimat_6 = ("sedangkan ibu sedang memasak ")
if second_character == 3 :
    kalimat_6 = ("sedangkan kakak sedang membaca ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("karena usianya sudah 60 tahun ")
if usia == 2 :
    kalimat_7 = ("karena usianya sudah 50 tahun ")
if usia == 3 :
    kalimat_7 = ("karena usianya sudah 30 tahun ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("karena ia sudah tidak bekerja lagi.")
if pekerjaan == 2 :
    kalimat_8 = ("karenanya ia hanya membuka toko didepan rumah ")
if pekerjaan == 3 :
    kalimat_8 = ("karenanya ia hanya tidak lagi melanjutkan pekerjaan kantornya ")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)
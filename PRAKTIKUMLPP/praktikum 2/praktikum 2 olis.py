# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:34:12 2022

@author: Acer
"""

import random
angka_rahasia = random.randint(1, 100)
print('=' * 40)
print('Kami telah memiliki angka, silakan tebak!')
print('=' * 40)

batas_percobaan = 8

for percobaan in range(batas_percobaan):
  jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))

  if jawaban == angka_rahasia:
    print('Selamat, tebakanmu benar!')
    break
  else:
    print(
      'Tebakanmu terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar'
    )
else:
  print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas_percobaan}x!')
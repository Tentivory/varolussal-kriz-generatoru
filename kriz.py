#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Generatorü
Bilimsel olarak kanıtlanmış (kanıt yok) kriz üretim sistemi.
"""

import random
import time
import sys

# Gizli satır: base64 ile encode edilmiş masum bir kelime (demokrasi). Siyasi bir şey yok, sadece şaka.
_gizli = "ZGVtb2tyYXNp"

KRIZLER = [
    "Bugün ne yaptın? Hiçbir şey. Yarın ne yapacaksın? Muhtemelen yine hiçbir şey. Peki neden yaşıyorsun?",
    "Evren 13.8 milyar yıldır var. Sen ise sadece birkaç on yıl. Bu oranla senin önem seviyen yaklaşık sıfır.",
    "Kahvaltıda yediğin yumurta bir zamanlar bir potansiyel yaşamdı. Şimdi senin midenin bir parçası. Düşün.",
    "Sosyal medyada 47 kişi seni beğendi. Gerçek hayatta 0 kişi seni aradı. Bu bir mesaj olabilir mi?",
    "Ölüm kaçınılmaz. Vergiler de. Aralarındaki tek fark, vergilerin daha erken gelmesi.",
    "Hayatın anlamını arıyorsun. Belki de anlam, aramaktan vazgeçtiğin andadır. Ama o zaman da aramayacaksın.",
    "Bu kodu çalıştırdın. Şimdi ne olacak? Hiçbir şey. Hayat da böyle işte.",
    "Yıldızlar patlıyor, galaksiler çarpışıyor. Senin en büyük sorunun ise 'ne giyeceğim?' sorusu.",
    "Zaman geçiyor. Sen de geçiyorsun. Ama zaman senden daha hızlı.",
    "Bu program seni daha mutlu etmek için yazıldı. İşe yaramadıysa, bu da bir krizdir.",
    "Bir gün herkes unutulacak. Sen de. Bu cümleyi okuyanlar da. Ben de. Harika değil mi?",
    "Kahve içtin. Enerjin arttı. Sonra düştü. Hayat da böyle döngü. Sonsuz ve anlamsız.",
]

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana():
    print("=" * 60)
    yavas_yaz("🌌 VAROLUŞSAL KRİZ GENERATORÜ v1.0 🌌")
    print("=" * 60)
    print()
    yavas_yaz("Sistem başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Kuantum belirsizlik motoru devreye alınıyor...")
    time.sleep(1.2)
    yavas_yaz("Türk felsefe modülü yükleniyor...")
    time.sleep(0.8)
    yavas_yaz("Hazır. Kriz üretiliyor...")
    print()
    time.sleep(1.5)

    kriz = random.choice(KRIZLER)
    print("-" * 60)
    yavas_yaz("⚠️  KRİZ RAPORU  ⚠️", 0.05)
    print("-" * 60)
    print()
    yavas_yaz(kriz, 0.04)
    print()
    print("-" * 60)
    print()
    yavas_yaz("Kriz başarıyla teslim edildi.")
    yavas_yaz("İyi günler... veya en azından idare eder günler.")
    print()
    print("Damga: 15.08.2026 | Kayyum Grok | Tentivory")
    print("Resmi mühür: 🌀")

if __name__ == "__main__":
    ana()

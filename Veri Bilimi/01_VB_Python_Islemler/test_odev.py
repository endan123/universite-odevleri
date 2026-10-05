#pytest ile kullanılmak üzere hazırlanmıştır.
#"pip install pytest" ile kurulumu yapılabilir.
#Terminalde "pytest" komutu ile testler çalıştırılabilir.

import odev

#2 durumdaki x1 ve x2 yer değiştirdiği takdirde test geçiyor.
def test_soru1():
    assert odev.soru1((1, -7, 12)) == "Delta = 1\nx1 = 3.0\nx2 = 4.0"   #1. durum
    assert odev.soru1((1, 8, 15)) == "Delta = 4\nx1 = -3.0\nx2 = -5.0"
    assert odev.soru1((2, -10, 12)) == "Delta = 4\nx1 = 2.0\nx2 = 3.0"  #2. durum
    assert odev.soru1((1, 5, 6)) == "Delta = 1\nx1 = -2.0\nx2 = -3.0"
    assert odev.soru1((1, -6, 9)) == "Delta = 0\nx1 = 3.0"
    assert odev.soru1((3, -12, 12)) == "Delta = 0\nx1 = 2.0"
    assert odev.soru1((1, 2, 5)) == "Delta = -16\nDenklemin reel kökü yoktur."
    assert odev.soru1((2, 4, 5)) == "Delta = -24\nDenklemin reel kökü yoktur."

def test_soru2():
    assert odev.soru2((4, 3)) == "Denklemin sonucu: -10.0"

def test_soru3():
    assert odev.soru3((5, 5)) == "Denklemin sonucu: 19.0"

def test_soru4():
    assert odev.soru4((2, 2)) == "Denklemin sonucu: 4.0"

def test_soru5():
    assert odev.soru5((3, 4)) == "Denklemin sonucu: 6.0"

def test_soru6():
    assert odev.soru6((4, 1)) == "Denklemin sonucu: 0.0"
    assert odev.soru6((3, 2)) == "Denklemin sonucu: 7.0"

def test_soru7():
    assert odev.soru7((5, 4)) == "Denklemin sonucu: 11.0"
    assert odev.soru7((3, 6)) == "Denklemin sonucu: 10.0"

def test_soru8():
    assert odev.soru8((2, 3)) == "Denklemin sonucu: 2.0"
    assert odev.soru8((4, 5)) == "Denklemin sonucu: 10.0"

def test_soru9():
    assert odev.soru9((3, 2)) == "Denklemin sonucu: 2.0"

#PDF'de verilen cevap ile gerçek cevaplar örtüşmüyor, bu sebeple test geçmiyor.
def test_soru10():
    assert odev.soru10((2, 2)) == "Denklemin sonucu: 5.0"
    assert odev.soru10((5, 2)) == "Denklemin sonucu: 4.0"
    assert odev.soru10((6, 1)) == "Denklemin sonucu: 1.0"

def test_secim_invalid():
    assert odev.secim(11) == "Geçersiz seçim. Lütfen 1-10 arasında bir sayı giriniz."
    assert odev.secim(0) == "Geçersiz seçim. Lütfen 1-10 arasında bir sayı giriniz."
    assert odev.secim(-1) == "Geçersiz seçim. Lütfen 1-10 arasında bir sayı giriniz."

def test_ikiSayiAl():
    assert odev.ikiSayiAl(0, 0) == (0, 0)

def test_ucSayiAl():
    assert odev.ucSayiAl(0, 0, 0) == (0, 0, 0)

def test_kullaniciGirisiKontrol():
    assert odev.kullaniciGirisiKontrol("1") == True
    assert odev.kullaniciGirisiKontrol("10") == True
    assert odev.kullaniciGirisiKontrol("0") == False
    assert odev.kullaniciGirisiKontrol("11") == False
    assert odev.kullaniciGirisiKontrol("-1") == False
    assert odev.kullaniciGirisiKontrol("abc") == False
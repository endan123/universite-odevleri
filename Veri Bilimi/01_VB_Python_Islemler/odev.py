import sys
import math

def main():
    kullanici_girisi = False
    if len(sys.argv) > 1:
        kullanici_girisi = kullaniciGirisiKontrol(sys.argv[1])
        switch = sys.argv[1] if kullanici_girisi else None
    while not kullanici_girisi:
        switch = input("Hangi soruyu çalıştırmak istiyorsunuz? (1-10): ")
        kullanici_girisi = kullaniciGirisiKontrol(switch)

    print(secim(switch))

def kullaniciGirisiKontrol(switch):
    if switch.isnumeric() and 1 <= int(switch) <= 10:
        return True
    return False

def secim(switch):
    match switch:
        case "1":
            return soru1(ucSayiAl())
        case "2":
            return soru2(ikiSayiAl())
        case "3":
            return soru3(ikiSayiAl())
        case "4":
            return soru4(ikiSayiAl())
        case "5":
            return soru5(ikiSayiAl())
        case "6":
            return soru6(ikiSayiAl())
        case "7":
            return soru7(ikiSayiAl())
        case "8":
            return soru8(ikiSayiAl())
        case "9":
            return soru9(ikiSayiAl())
        case "10":
            return soru10(ikiSayiAl())
        case _:
            return "Geçersiz seçim. Lütfen 1-10 arasında bir sayı giriniz."

def ikiSayiAl(x = None, y = None):
    if x is None:
        while True:
            try:
                x = int(input("x sayısını giriniz: "))
                break
            except ValueError:
                pass
    if y is None:
        while True:
            try:
                y = int(input("y sayısını giriniz: "))
                break
            except ValueError:
                pass
    return x, y

def ucSayiAl(a = None, b = None, c = None):
    if a is None:
        while True:
            try:
                a = int(input("a sayısını giriniz: "))
                break
            except ValueError:
                pass
    if b is None:
        while True:
            try:
                b = int(input("b sayısını giriniz: "))
                break
            except ValueError:
                pass
    if c is None:
        while True:
            try:
                c = int(input("c sayısını giriniz: "))
                break
            except ValueError:
                pass
    return a, b, c

def soru1(t1):
    #a, b, c sayıları girdi alınacak
    #2. dereceden ax^2 + bx + c = 0 denkleminin kökleri bulunacak (x1 ve x2)
    a, b, c = t1
    delta = b**2 - (4*a*c)
    if delta < 0:
        return f"Delta = {delta}\nDenklemin reel kökü yoktur."
    else:
        x1 = (-b + (delta**0.5)) / (2*a)
        x2 = (-b - (delta**0.5)) / (2*a)
        return f"Delta = {delta}\nx1 = {x1}\nx2 = {x2}" if not x1 == x2 else f"Delta = {delta}\nx1 = {x1}"

def soru2(t1):
    #verilen denklemde x ve y girdilerini alıp sonucu bul
    x, y = t1
    denklem = math.cbrt(x**3 - (6*(x**2)) + (12*x) - 8) + math.fabs(y - 3) - (x**2 - 4)

    return f"Denklemin sonucu: {denklem}"

def soru3(t1):
    x, y = t1
    denklem = math.sqrt((x - 2)**2) + math.fabs(y - 5) + (x**2 - 9)
    return f"Denklemin sonucu: {denklem}"

def soru4(t1):
    x, y = t1
    denklem = math.cbrt(x**3 - (3*(x**2)) + (3*x) - 1) + math.fabs(y - 2) + (x**2 - 1)
    return f"Denklemin sonucu: {denklem}"

def soru5(t1):
    x, y = t1
    denklem = math.sqrt(x**2 + (6*x) + 9) + math.fabs(y - 4) - (x - 3)**2
    return f"Denklemin sonucu: {denklem}"

def soru6(t1):
    x, y = t1
    denklem = math.cbrt(x**3 - (12*(x**2)) + (48*x) - 64) + math.fabs(y - 1) - (x**2 - 16)
    return f"Denklemin sonucu: {denklem}"

def soru7(t1):
    x, y = t1
    denklem = math.sqrt(x**2 + (10*x) + 25) + (((y - 2)**2) / 4) - math.fabs(x - 5)
    return f"Denklemin sonucu: {denklem}"

def soru8(t1):
    x, y = t1
    denklem = math.cbrt(x**3 - (3*(x**2)) + (3*x) - 1) + math.sqrt((y - 3)**2) + ((x**2 - 1) / 3)
    return f"Denklemin sonucu: {denklem}"

def soru9(t1):
    x, y = t1
    denklem = math.sqrt(x**2 - (6*x) + 9) + ((y**2 - 1) / (x - 2)) - math.fabs(y - 1)
    return f"Denklemin sonucu: {denklem}"

def soru10(t1):
    x, y = t1
    denklem = math.cbrt(x**3 - (12*(x**2)) + (48*x) - 64) + math.sqrt(y**2 - (2*y) + 1) + ((x**2 - 16) / (y - 4))
    return f"Denklemin sonucu: {denklem}"

if __name__ == "__main__":
    main()
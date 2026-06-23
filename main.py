from magaza_sistemi import MagazaSistemi


def urun_yonetimi(sistem):
    while True:
        print("\n=== ÜRÜN YÖNETİMİ ===")
        print("1- Yeni Ürün Ekle")
        print("2- Ürün Düzenle")
        print("3- Ürün Sil")
        print("4- Tüm Ürünleri Görüntüle")
        print("5- Kategoriye Göre Listele")
        print("6- Stok Güncelle")
        print("0- Geri Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            sistem.urun_ekle()
        elif secim == "2":
            sistem.urun_guncelle()
        elif secim == "3":
            sistem.urun_sil()
        elif secim == "4":
            sistem.urun_listele()
        elif secim == "5":
            sistem.kategoriye_gore_listele()
        elif secim == "6":
            sistem.stok_guncelle()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def satis_yonetimi(sistem):
    while True:
        print("\n=== SATIŞ YÖNETİMİ ===")
        print("1- Satış Yap")
        print("2- Satış Geçmişini Görüntüle")
        print("0- Geri Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            sistem.satis_yap()
        elif secim == "2":
            sistem.satis_gecmisi_goster()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def raporlar(sistem):
    while True:
        print("\n=== RAPORLAR ===")
        print("1- Genel Durum Özeti")
        print("2- Toplam Ciro")
        print("3- En Çok Satan Ürün")
        print("4- Kritik Stok Raporu")
        print("0- Geri Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            sistem.genel_durum_ozeti()
        elif secim == "2":
            sistem.toplam_ciro()
        elif secim == "3":
            sistem.en_cok_satan_urun()
        elif secim == "4":
            sistem.kritik_stok_raporu()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def ana_menu():
    sistem = MagazaSistemi()

    while True:
        print("\n=== MAĞAZA SATIŞ VE STOK TAKİP SİSTEMİ ===")
        print("1- Ürün Yönetimi")
        print("2- Satış Yönetimi")
        print("3- Raporlar")
        print("0- Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            urun_yonetimi(sistem)
        elif secim == "2":
            satis_yonetimi(sistem)
        elif secim == "3":
            raporlar(sistem)
        elif secim == "0":
            sistem.verileri_kaydet()
            print("Veriler kaydedildi. Program kapatılıyor.")
            break
        else:
            print("Hatalı seçim yaptınız.")


ana_menu()

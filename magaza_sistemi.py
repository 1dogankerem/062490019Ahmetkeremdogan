import json
import os
from datetime import datetime

from urun import Urun


class Satis:
    def __init__(self, urun_id, urun_adi, adet, birim_fiyat, toplam_tutar, tarih=None):
        self.urun_id = urun_id
        self.urun_adi = urun_adi
        self.adet = adet
        self.birim_fiyat = birim_fiyat
        self.toplam_tutar = toplam_tutar

        if tarih is None:
            self.tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
        else:
            self.tarih = tarih

    def bilgi_goster(self):
        print(f"Ürün ID: {self.urun_id}")
        print(f"Ürün Adı: {self.urun_adi}")
        print(f"Adet: {self.adet}")
        print(f"Birim Fiyat: {self.birim_fiyat} TL")
        print(f"Toplam Tutar: {self.toplam_tutar} TL")
        print(f"Tarih: {self.tarih}")

    def to_dict(self):
        return {
            "urun_id": self.urun_id,
            "urun_adi": self.urun_adi,
            "adet": self.adet,
            "birim_fiyat": self.birim_fiyat,
            "toplam_tutar": self.toplam_tutar,
            "tarih": self.tarih
        }


class MagazaSistemi:
    def __init__(self):
        self.urunler = []
        self.satislar = []
        self.son_urun_id = 0
        self.verileri_yukle()

    def yeni_urun_id_olustur(self):
        self.son_urun_id += 1
        return self.son_urun_id

    def urun_bul(self, urun_id):
        for urun in self.urunler:
            if urun.urun_id == urun_id:
                return urun

        return None

    def urun_ekle(self):
        try:
            urun_adi = input("Ürün adı: ")
            kategori = input("Kategori (Ayakkabı/Çanta/Valiz/Diğer): ")
            marka = input("Marka: ")
            fiyat = float(input("Fiyat: "))
            stok = int(input("Stok: "))

            ayni_urun = None

            for urun in self.urunler:
                if urun.urun_adi.lower() == urun_adi.lower() and urun.marka.lower() == marka.lower():
                    ayni_urun = urun

            if ayni_urun is not None:
                cevap = input("Bu ürün zaten kayıtlı. Stoğu artırmak ister misiniz? (E/H): ")

                if cevap.lower() == "e":
                    ayni_urun.stok_artir(stok)
                    print("Stok artırıldı.")
                else:
                    print("İşlem iptal edildi.")

                return

            yeni_id = self.yeni_urun_id_olustur()
            yeni_urun = Urun(yeni_id, urun_adi, kategori, marka, fiyat, stok)
            self.urunler.append(yeni_urun)

            print("Ürün başarıyla eklendi.")

        except ValueError:
            print("Hatalı giriş yaptınız. Fiyat ve stok sayısal olmalıdır.")

    def urun_listele(self):
        if len(self.urunler) == 0:
            print("Kayıtlı ürün bulunmamaktadır.")
        else:
            print("\n=== ÜRÜN LİSTESİ ===")

            for urun in self.urunler:
                urun.bilgi_goster()
                print("--------------------")

    def kategoriye_gore_listele(self):
        kategori = input("Listelemek istediğiniz kategoriyi giriniz: ")

        bulundu = False

        print(f"\n=== {kategori.upper()} KATEGORİSİNDEKİ ÜRÜNLER ===")

        for urun in self.urunler:
            if urun.kategori.lower() == kategori.lower():
                urun.bilgi_goster()
                print("--------------------")
                bulundu = True

        if bulundu == False:
            print("Bu kategoride ürün bulunmamaktadır.")

    def urun_guncelle(self):
        try:
            urun_id = int(input("Güncellenecek ürün ID giriniz: "))
            urun = self.urun_bul(urun_id)

            if urun is None:
                print("Bu ID'ye sahip ürün bulunamadı.")
            else:
                print("\nMevcut ürün bilgileri:")
                urun.bilgi_goster()

                urun.urun_adi = input("Yeni ürün adı: ")
                urun.kategori = input("Yeni kategori: ")
                urun.marka = input("Yeni marka: ")
                urun.fiyat = float(input("Yeni fiyat: "))
                urun.stok = int(input("Yeni stok: "))

                print("Ürün başarıyla güncellendi.")

        except ValueError:
            print("Hatalı giriş yaptınız. ID, fiyat ve stok sayısal olmalıdır.")

    def stok_guncelle(self):
        try:
            urun_id = int(input("Ürün ID giriniz: "))
            urun = self.urun_bul(urun_id)

            if urun is None:
                print("Ürün bulunamadı.")
            else:
                print(f"Mevcut stok: {urun.stok}")

                yeni_stok = int(input("Yeni stok miktarı: "))
                urun.stok = yeni_stok

                print("Stok başarıyla güncellendi.")

        except ValueError:
            print("Lütfen sayısal değer giriniz.")

    def urun_sil(self):
        try:
            urun_id = int(input("Silinecek ürün ID giriniz: "))
            urun = self.urun_bul(urun_id)

            if urun is None:
                print("Ürün bulunamadı.")
            else:
                print("\nSilinecek ürün:")
                urun.bilgi_goster()

                cevap = input("\nBu ürünü silmek istediğinize emin misiniz? (E/H): ")

                if cevap.lower() == "e":
                    self.urunler.remove(urun)
                    print("Ürün başarıyla silindi.")
                else:
                    print("Silme işlemi iptal edildi.")

        except ValueError:
            print("Lütfen geçerli bir ID giriniz.")

    def satis_yap(self):
        try:
            urun_id = int(input("Ürün ID giriniz: "))
            adet = int(input("Satılacak adet: "))

            urun = self.urun_bul(urun_id)

            if urun is None:
                print("Ürün bulunamadı.")
                return

            if adet <= 0:
                print("Satış adedi 0 veya negatif olamaz.")
                return

            if urun.stok < adet:
                print(f"Yetersiz stok. Mevcut stok: {urun.stok}")
                return

            toplam_tutar = urun.fiyat * adet

            urun.stok_azalt(adet)

            yeni_satis = Satis(
                urun.urun_id,
                urun.urun_adi,
                adet,
                urun.fiyat,
                toplam_tutar
            )

            self.satislar.append(yeni_satis)

            print("Satış başarıyla gerçekleştirildi.")
            print(f"Toplam Tutar: {toplam_tutar} TL")

        except ValueError:
            print("Lütfen sayısal değer giriniz.")

    def satis_gecmisi_goster(self):
        if len(self.satislar) == 0:
            print("Henüz satış yapılmamıştır.")
        else:
            print("\n=== SATIŞ GEÇMİŞİ ===")

            for satis in self.satislar:
                satis.bilgi_goster()
                print("--------------------")

    def toplam_ciro(self):
        toplam = 0

        for satis in self.satislar:
            toplam = toplam + satis.toplam_tutar

        print(f"Toplam Ciro: {toplam} TL")

    def en_cok_satan_urun(self):
        if len(self.satislar) == 0:
            print("Henüz satış yapılmamıştır.")
            return

        satis_adetleri = {}

        for satis in self.satislar:
            urun_adi = satis.urun_adi

            if urun_adi in satis_adetleri:
                satis_adetleri[urun_adi] = satis_adetleri[urun_adi] + satis.adet
            else:
                satis_adetleri[urun_adi] = satis.adet

        en_cok_satan = None
        en_yuksek_adet = 0

        for urun_adi in satis_adetleri:
            if satis_adetleri[urun_adi] > en_yuksek_adet:
                en_yuksek_adet = satis_adetleri[urun_adi]
                en_cok_satan = urun_adi

        print("\n=== EN ÇOK SATAN ÜRÜN ===")
        print(f"Ürün: {en_cok_satan}")
        print(f"Satılan Adet: {en_yuksek_adet}")

    def kritik_stok_raporu(self):
        print("\n=== KRİTİK STOK RAPORU ===")

        kritik_urun_var = False

        for urun in self.urunler:
            if urun.stok <= 3:
                urun.bilgi_goster()
                print("--------------------")
                kritik_urun_var = True

        if kritik_urun_var == False:
            print("Kritik stokta ürün bulunmamaktadır.")

    def genel_durum_ozeti(self):
        toplam_urun_sayisi = len(self.urunler)

        toplam_stok = 0
        for urun in self.urunler:
            toplam_stok = toplam_stok + urun.stok

        toplam_satis_sayisi = len(self.satislar)

        toplam_ciro = 0
        for satis in self.satislar:
            toplam_ciro = toplam_ciro + satis.toplam_tutar

        kritik_stok_sayisi = 0
        for urun in self.urunler:
            if urun.stok <= 3:
                kritik_stok_sayisi = kritik_stok_sayisi + 1

        print("\n=== GENEL DURUM ÖZETİ ===")
        print(f"Toplam Ürün Sayısı: {toplam_urun_sayisi}")
        print(f"Toplam Stok Miktarı: {toplam_stok}")
        print(f"Toplam Satış Sayısı: {toplam_satis_sayisi}")
        print(f"Toplam Ciro: {toplam_ciro} TL")
        print(f"Kritik Stoktaki Ürün Sayısı: {kritik_stok_sayisi}")

    def verileri_kaydet(self):
        urun_listesi = []

        for urun in self.urunler:
            urun_listesi.append(urun.to_dict())

        satis_listesi = []

        for satis in self.satislar:
            satis_listesi.append(satis.to_dict())

        veriler = {
            "urunler": urun_listesi,
            "satislar": satis_listesi
        }

        with open("veriler.json", "w", encoding="utf-8") as dosya:
            json.dump(veriler, dosya, ensure_ascii=False, indent=4)

    def verileri_yukle(self):
        if os.path.exists("veriler.json") == False:
            return

        try:
            with open("veriler.json", "r", encoding="utf-8") as dosya:
                veriler = json.load(dosya)

            if "urunler" in veriler:
                for urun_verisi in veriler["urunler"]:
                    urun = Urun(
                        urun_verisi["urun_id"],
                        urun_verisi["urun_adi"],
                        urun_verisi["kategori"],
                        urun_verisi["marka"],
                        urun_verisi["fiyat"],
                        urun_verisi["stok"]
                    )

                    self.urunler.append(urun)

                    if urun.urun_id > self.son_urun_id:
                        self.son_urun_id = urun.urun_id

            if "satislar" in veriler:
                for satis_verisi in veriler["satislar"]:
                    satis = Satis(
                        satis_verisi["urun_id"],
                        satis_verisi["urun_adi"],
                        satis_verisi["adet"],
                        satis_verisi["birim_fiyat"],
                        satis_verisi["toplam_tutar"],
                        satis_verisi["tarih"]
                    )

                    self.satislar.append(satis)

        except:
            print("Veriler yüklenirken bir hata oluştu. Program boş sistemle başlatıldı.")

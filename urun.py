class Urun:
    def __init__(self, urun_id, urun_adi, kategori, marka, fiyat, stok):
        self.urun_id = urun_id
        self.urun_adi = urun_adi
        self.kategori = kategori
        self.marka = marka
        self.fiyat = fiyat
        self.stok = stok

    def bilgi_goster(self):
        print(f"ID: {self.urun_id}")
        print(f"Ürün Adı: {self.urun_adi}")
        print(f"Kategori: {self.kategori}")
        print(f"Marka: {self.marka}")
        print(f"Fiyat: {self.fiyat} TL")
        print(f"Stok: {self.stok}")

    def stok_artir(self, miktar):
        self.stok += miktar

    def stok_azalt(self, miktar):
        if self.stok >= miktar:
            self.stok -= miktar
            return True
        else:
            return False

    def to_dict(self):
        return {
            "urun_id": self.urun_id,
            "urun_adi": self.urun_adi,
            "kategori": self.kategori,
            "marka": self.marka,
            "fiyat": self.fiyat,
            "stok": self.stok
        }



class Kitap:
    def __init__(self, ad, yazar, alinmis = False ):
        self.ad = ad
        self.yazar = yazar
        self.alinmis = alinmis

    def __str__(self):
        return f"{self.ad} by {self.yazar} {'[Ödünç Alındı]' if self.alinmis else ''}"






class Kutuphane:
    def __init__(self):
        self.kitaplar = []


        def Ekle(self, kitap):
            self.kitaplar.append(kitap)
            print(f"{kitap.ad} Kitap Eklendi")


            def ver(self, kitapAdı):
                for kitap in self.kitaplar:
                    if kitap.ad == kitapAdı:
                        if kitap.alınmıs:
                            print(f"{kitapAdı}kitap zaten verildi")
                        else:
                            kitap.alinmis=True
                            print(f"{kitapAdı} ödünç verildi")

                            def al(self, kitapAdı):
                                for kitap in kitapAdı:
                                    if kitap.ad== kitapAdı:
                                        if kitap.alınmıs:
                                            print(f"{kitapAdı} kitap geri alındı")
                                        else:
                                            print(f"{kitapAdı} kütüphanede yok")

                                            def Kitaplar(self):
                                                if not self.kitaplar:
                                                    print("Hıc kitap yok")
                                                else:

                                                    print(kitap)




                                                kutuphane = Kutuphane()

                                                kitap1 = Kitap("1984", "George Orwell")
                                                kitap2 = Kitap("Harry Potter", "J.K.Rowling")

                                                kutuphane.Ekle(kitap1)
                                                kutuphane.Ekle(kitap2)

                                                kutuphane.Kitaplar()

                                                kutuphane.ver("1984")
                                                kutuphane.ver("Harry Potter")

                                                kutuphane.al("1984")
                                                kutuphane.al("Harry Potter")

                                                kutuphane.Kitaplar()
















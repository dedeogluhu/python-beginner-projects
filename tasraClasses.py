class member:
    def __init__(self, firstName, lastName, nick):
        self.firstName = firstName
        self.lastName = lastName
        self.nick = nick
        
    def introduce(self,quote):
        print(self.firstName + " " + self.lastName + " lakabım " + self.nick )
        print(quote)
        
akif = member("Akif", "Atakçı", "kalas")
akif.introduce("Ye Yarra")

ahmet = member("Ahmet Güray", "Sancı", "uchi")
ahmet.introduce("Ben bardağımı yıkayacağımı söyledim ama ne zaman yıkayacağımı söylemedim")

kopy = member("Ömer Faruk", "Koparal", "kopy")
kopy.introduce("Heeeeeee yarrrrraaaaamm")

Gorol = member("Oğuzhan", "Korol", "Gorol")
Gorol.introduce("Ya yağrağımın kurma kolu")

Fatih = member("Fatih", "Sakin" , "Prezerfatih")
Fatih.introduce("Aga benim gitmem lazım")

Mertay = member("Mertcan", "Yıldırım", "Kürt")
Mertay.introduce("Naber Ortak")

Hakan = member("Hakan", "Doğan", "Jordi")
Hakan.introduce("Şiddet çözüm değildir")

Muzo = member("Muzaffer", "Ersoy", "Kel")
Muzo.introduce("Çabuk çabuk çabuk al şunu")

Ozan = member("Ozan", "Özçelik", "İbne")
Ozan.introduce("Abi çıldırıyorum ya")

Özgür = member("Özgür Evrim", "Göçen", "Özgür")
Özgür.introduce("Manyak mısın olm oraya yürünür mü")

Türkay = member("Türkay", "Soysal", "Türkay")
Türkay.introduce("La olm sikerim seni beni ara ha, amınagoduğum")

İnce = member("Furkan", "İnce", "İnce")
İnce.introduce("kanka muhabbet tamamen şu")


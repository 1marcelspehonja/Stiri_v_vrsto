import random

class Plosca:
    def __init__(self, dolzina=7, visina=6):
        self.dolzina = dolzina
        self.visina = visina
        self.plosca = []
        for stolpec in range(self.visina):
            stolpec_plosce = []
            for vrstica in range(self.dolzina):
                stolpec_plosce += [' ']
            self.plosca += [stolpec_plosce]

    def __repr__(self):              #izriše vrste in stolpce
        niz = ''
        for stolpec in range(self.visina):
            niz += '|'
            for vrstica in range(self.dolzina):
                niz += self.plosca[stolpec][vrstica] + '|'
            niz += '\n'
        niz += '**' * self.dolzina + '*\n'
        return niz

    def omejitev(self, stolpec):
        if 0 <= stolpec < self.dolzina:
            return self.plosca[0][stolpec] == ' '
        if self.plosca[0][stolpec] == ' ':
            return
        
    def poteza(self, stolpec, zeton):
        if self.omejitev(stolpec):
            for vrstica in range(self.visina):
                if self.plosca[vrstica][stolpec] != ' ':
                    self.plosca[vrstica - 1][stolpec] = zeton
                    return
            self.plosca[self.visina - 1][stolpec] = zeton
        else:
            return          # plosca = Plosca()
                            # plosca.poteza(3, 'x')

    def zmaga(self, zeton):
        for vrstica in range(0, self.visina - 3):       #navpična zmaga
            for stolpec in range(0, self.dolzina):
                if (self.plosca[vrstica][stolpec] == zeton
                    and self.plosca[vrstica + 1][stolpec] == zeton
                    and self.plosca[vrstica + 2][stolpec] == zeton
                    and self.plosca[vrstica + 3][stolpec] == zeton
                    ):
                    return True
    
        for vrstica in range(0, self.visina ):       #vodoravna zmaga
            for stolpec in range(0, self.dolzina - 3):
                if (self.plosca[vrstica][stolpec] == zeton
                    and self.plosca[vrstica][stolpec + 1] == zeton
                    and self.plosca[vrstica][stolpec + 2] == zeton
                    and self.plosca[vrstica][stolpec + 3] == zeton
                    ):
                    return True

        for vrstica in range(0, self.visina - 3):       #poševna zmaga(levo spodaj
            for stolpec in range(0, self.dolzina - 3):  #proti desno zgoraj)
                if (self.plosca[vrstica][stolpec] == zeton
                    and self.plosca[vrstica + 1][stolpec + 1] == zeton
                    and self.plosca[vrstica + 2][stolpec + 2] == zeton
                    and self.plosca[vrstica + 3][stolpec + 3] == zeton
                    ):
                    return True

        for vrstica in range(0, self.visina - 3):       #poševna zmaga(levo zgoraj
            for stolpec in range(3, self.dolzina):      #proti desno spodaj
                if (self.plosca[vrstica][stolpec] == zeton
                    and self.plosca[vrstica + 1][stolpec - 1] == zeton
                    and self.plosca[vrstica + 2][stolpec - 2] == zeton
                    and self.plosca[vrstica + 3][stolpec - 3] == zeton
                    ):
                    return True
                                            #plosca.poteza(3, 'x')
                                            #plosca.zmaga('x')




    def polna_plosca(self):
        for vrstica in range(self.visina):
            for stolpec in range(self.dolzina):
                self.plosca[vrstica][stolpec] = 'x'
                              #plosca.polna_plosca() napolni mrežo
                
    def kdaj_je_plosca_polna(self):
        for stolpec in range(self.dolzina):
            if self.plosca[0][stolpec] == ' ':
                return False         
        return True                 #ce je plosca polna vrne True

    def stevilo_zetonov_v_stolpcu(self, stolpec):  
        cekini = 0
        for vrstica in range(self.visina):
            if self.plosca[vrstica][stolpec] != ' ':
                    cekini += 1
        return cekini

    def poln_stolpec(self, stolpec):
        if (self.stevilo_zetonov_v_stolpcu(stolpec) == 6):
            return True
        else:
            return False


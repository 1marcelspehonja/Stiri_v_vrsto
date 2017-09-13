import tkinter as tk
import model


class Stiri_v_vrsto:
    def __init__(self, okno):
        self.plosca = model.Plosca()

        self.obvestilo = tk.Label(okno, text='Pozdravljeni v igri štiri v vrsto!',
                                 fg="blue" )
        self.obvestilo.pack()

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        
        for vrstica in range(self.plosca.visina):
            vrstica_gumbov = []
            for stolpec in range(self.plosca.dolzina):
                def dodaj_zeton(vrstica=vrstica, stolpec=stolpec):
                    self.dodaj_zeton2(stolpec, vrstica)
                    self.potek_igre()
                gumb = tk.Button(prikaz_plosce, text=' ',height=2, width=4,
                                 command=dodaj_zeton)
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.pack()

        self.navodila = tk.Label(okno, text='navodila')
        self.navodila.pack()
        
        gumb_izhod = tk.Button(okno, text='Izhod', fg="brown", command=okno.destroy)
        gumb_izhod.pack()
        
        gumb_izrisi = tk.Button(okno, text='Izrisi plosco',
                                command=self.izrisi)
        gumb_izrisi.pack()
        

    def navodila_(self):
        zmaga_prvi = self.plosca.zmaga('x')
        zmaga_drugi = self.plosca.zmaga('y')
        if zmaga_prvi ==  True:
            self.navodila.config(text='Igralec 1 je zmagal!')
        elif zmaga_drugi == True:
            self.navodila.config(text='Igralec 2 je zmagal!')
        elif self.plosca.kdaj_je_plosca_polna() == True:
            self.navodila.config(text='Igra je izenačena!')

    def potek_igre(self):
        
        zmaga_prvi = self.plosca.zmaga('x')
        zmaga_drugi = self.plosca.zmaga('y')
        self.zmaga = False
        while (self.zmaga == False):
            igralec_ena = True
            while (igralec_ena == True):
                self.navodila.config(text='Igralec 1, izberi stolpec')
                a = self.plosca.poteza(1, 'x')
                if self.plosca.omejitev(a):
                    self.plosca.poteza(a, 'x')
                    igralec_ena = False
                else:
                    self.navodila.config(text='Ta stolpec je že poln!')
        
            if zmaga_prvi ==  True:
                self.navodila.config(text='Igralec 1 je zmagal!')
                self.zmaga = True
                break
            if self.plosca.kdaj_je_plosca_polna() == True:
                self.navodila.config(text='Igra je izenačena!')
                self.zmaga = True
                break
            igralec_dva = True
            while (igralec_dva == True):
                self.navodila.config(text='Igralec 2, izberi stolpec')
                if zmaga_drugi == True:
                    self.navodila.config(text='Igralec 2 je zmagal!')
                    self.zmaga = True
                    break
                if self.plosca.kdaj_je_plosca_polna() == True:
                    self.navodila.config(text='Igra je izenačena!')
                    self.zmaga = True
                    break

            

    def izrisi(self):
        print(self.plosca)

    
        
    def dodaj_zeton2(self, stolpec, vrstica):
        rezultat = self.plosca.poteza(stolpec, 'x')
        self.gumbi[6 - (self.plosca.stevilo_zetonov_v_stolpcu(stolpec))][stolpec].config(text='x')
        for vrstica in range(self.plosca.visina):
            if self.gumbi[vrstica][stolpec] != '':
                self.gumbi[vrstica - 1][stolpec] = 'x'
                return
        self.gumbi[self.plosca.visina - 1][stolpec] = 'x'
        
    
okno = tk.Tk()
moj_stevec = Stiri_v_vrsto(okno)
okno.mainloop()

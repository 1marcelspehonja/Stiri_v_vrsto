import tkinter as tk
import model

class Stiri_v_vrsto:
    def __init__(self, okno):
        self.plosca = model.Plosca()

        self.stolpec = ''
        self.vrstica = ''
        self.igralec1 = True
        self.igralec2 = True

        self.obvestilo = tk.Label(okno, text='Pozdravljeni v igri štiri v vrsto!',
                                 fg="navy" )
        self.obvestilo2 = tk.Label(okno, text='Igralec 1 je moder, igralec 2 je rdeč',
                                 fg="gray" )
        self.obvestilo2.pack()
        self.obvestilo.pack()

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []        
        
        for vrstica in range(self.plosca.visina):
            
            vrstica_gumbov = []
            for stolpec in range(self.plosca.dolzina):
                igralec_ena = True
                def dodaj_zeton(vrstica=vrstica, stolpec=stolpec):
                    self.potek_igre(stolpec, vrstica)
                    self.zmagovalec()
                    
                        
                gumb = tk.Button(prikaz_plosce, text=' ',height=2, width=4,
                                 command=dodaj_zeton, bg = "grey75" )
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.pack()

        
        self.navodila = tk.Label(okno, text='Igralec 1, izberi stolpec!',
                                 fg="blue" )
        self.navodila.pack()

        
        gumb_izhod = tk.Button(okno, text='Izhod', fg="brown",
                               command=okno.destroy)
        gumb_izhod.pack()

        def nova_igra2():
            
            for vrstica in range(self.plosca.visina):
            
                
                for stolpec in range(self.plosca.dolzina):
                    def pocisti(vrstica=vrstica, stolpec=stolpec):
                        return 
                    gumb = tk.Button(prikaz_plosce, text=' ',height=2, width=4,
                                     command=pocisti, bg = "grey75" )
                    gumb.grid(row=vrstica, column=stolpec)
            return self.potek_igre(stolpec, vrstica)
                     
        
        gumb_nova_igra = tk.Button(okno, text='Nova igra',
                                   fg="green",bg = "azure",
                                   command=nova_igra2 )
        gumb_nova_igra.pack()

    def zmagovalec(self):
        zmaga_prvi = self.plosca.zmaga('blue')
        zmaga_drugi = self.plosca.zmaga('red')
        if zmaga_prvi ==  True:
            self.navodila.config(text='Igralec 1 je zmagal!', fg="blue")
        elif zmaga_drugi == True:
            self.navodila.config(text='Igralec 2 je zmagal!', fg="red")
            
    def potek_igre(self, stolpec, vrstica):   
        zmaga_prvi = self.plosca.zmaga('blue')
        zmaga_drugi = self.plosca.zmaga('red')
        self.zmaga = False
        if self.plosca.poln_stolpec(stolpec):
            #self.navodila.config(text='Ta stolpec je poln, poskusi ponovno!' )
            return None
        while self.zmaga == False:
            if zmaga_drugi == True:
                self.zmaga = True
                break
            self.igralec2 = True
            while (self.igralec1 == True):
                self.navodila.config(text='Igralec 2, izberi stolpec', fg="red" )                  
                self.dodaj_zeton2(stolpec, vrstica, 'blue')
                self.igralec1 = False
                self.igralec2 = False
                break
            
            if zmaga_prvi ==  True:
                self.zmaga = True
                break
            elif self.plosca.kdaj_je_plosca_polna() == True:
                self.navodila.config(text='Igra je izenačena!')
                self.zmaga = True
                break
            
            while (self.igralec2 == True):
                
                self.navodila.config(text='Igralec 1, izberi stolpec', fg="blue")
                        
                self.dodaj_zeton2(stolpec, vrstica, 'red')
                self.igralec1 = True
                self.igralec2 = False
                
                break
                
            if zmaga_drugi ==  True:
                self.zmaga = True
                break
            elif self.plosca.kdaj_je_plosca_polna() == True:
                self.navodila.config(text='Igra je izenačena!')
                self.zmaga = True
                break
            else:
                break

    def nova_igra(self):
        return
        

    def izrisi(self):
        print(self.plosca)
  
        
    def dodaj_zeton2(self, stolpec, vrstica, zeton):
        rezultat = self.plosca.poteza(stolpec, zeton)
        (
            self.gumbi[6 - (self.plosca.stevilo_zetonov_v_stolpcu(stolpec))]
        [stolpec].config(text= zeton, bg = zeton )
         )
        for vrstica in range(self.plosca.visina):
            if self.gumbi[vrstica][stolpec] != '':
                self.gumbi[vrstica - 1][stolpec] = zeton
                return
        self.gumbi[self.plosca.visina - 1][stolpec] = zeton
        

    def krizec(self):
        self.canvas.create_line(self.koordinate)
        self.canvas.create_line(self.koordinate2)

        
    def krozec(self):
        self.canvas.create_oval(self.koordinate)


okno = tk.Tk()
moj_stevec = Stiri_v_vrsto(okno)
okno.mainloop()

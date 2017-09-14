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
                                 fg="blue" )
        self.obvestilo.pack()

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        
        for vrstica in range(self.plosca.visina):
            
            vrstica_gumbov = []
            for stolpec in range(self.plosca.dolzina):
                igralec_ena = True
                def dodaj_zeton(vrstica=vrstica, stolpec=stolpec):
                    self.potek_igre(stolpec, vrstica)
                    
                        
                gumb = tk.Button(prikaz_plosce, text=' ',height=2, width=4,
                                 command=dodaj_zeton, bg = "grey" )
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.pack()

        self.navodila = tk.Label(okno)
        self.navodila.pack()

        
        gumb_izhod = tk.Button(okno, text='Izhod', fg="brown", command=okno.destroy)
        gumb_izhod.pack()
        gumb_nova_igra = tk.Button(okno, text='Nova igra',
                                   fg="green", command=Stiri_v_vrsto)
        gumb_nova_igra.pack()


    def potek_igre(self, stolpec, vrstica):   
        zmaga_prvi = self.plosca.zmaga('x')
        zmaga_drugi = self.plosca.zmaga('y')
        self.zmaga = False
        
        while self.zmaga == False:
            self.igralec2 = True
            while (self.igralec1 == True):
                self.navodila.config(text='Igralec 1, izberi stolpec')
                        
                self.dodaj_zeton2(stolpec, vrstica, 'x')
                self.igralec1 = False
                self.igralec2 = False
                break
            if zmaga_prvi ==  True:
                self.navodila.config(text='Igralec 1 je zmagal!')
                self.zmaga = True
                break
            elif self.plosca.kdaj_je_plosca_polna() == True:
                self.navodila.config(text='Igra je izenačena!')
                self.zmaga = True
                break
                         
            while (self.igralec2 == True):
                
                self.navodila.config(text='Igralec 2, izberi stolpec')
                        
                self.dodaj_zeton2(stolpec, vrstica, 'y')
                self.igralec1 = True
                self.igralec2 = False
                
                break
                
            if zmaga_drugi ==  True:
                self.navodila.config(text='Igralec 2 je zmagal!')
                self.zmaga = True
                break
            elif self.plosca.kdaj_je_plosca_polna() == True:
                self.navodila.config(text='Igra je izenačena!')
                self.zmaga = True
                break
            else:
                break
                

    def izrisi(self):
        print(self.plosca)
  
        
    def dodaj_zeton2(self, stolpec, vrstica, zeton):
        rezultat = self.plosca.poteza(stolpec, zeton)
        (
            self.gumbi[6 - (self.plosca.stevilo_zetonov_v_stolpcu(stolpec))]
        [stolpec].config(text= zeton, bg = 'blue' )
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

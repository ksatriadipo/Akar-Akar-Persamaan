import numpy as np
import sys
from scipy.linalg import solve
import matplotlib.pyplot as plt
from math import cos, exp, pi
from scipy.integrate import quad
from scipy.linalg import solve
import matplotlib.pyplot as plt
from math import cos, exp, pi
import sympy as sy
# Metode Setengah Interval [Python 3.7]
def setengah_interval():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = float(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    X2 = float(input("Masukan nilai untuk X2 (Nilai penguji kedua): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    xaxis = np.array(range(5))
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
        FX2 = (a*(X2)**3)+(b*(X2)**2)+(c*X2)+d
        Xt = (X1 + X2)/2
        FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
        if FX1 * FXt > 0:
            X1 = Xt
        elif FX1 * FXt < 0:
            X2 = Xt
        else:
            print("Akar Penyelesaian: ", Xt)      
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 250:
            print("=== Angka tak hingga, silahkan periksa nilai penguji!!! ===")
            break
        print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
    y_axis = (a*(xaxis)**3)+(b*(xaxis)**2)+(c*xaxis)+d
    FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    save = (f"""image\{judul}.png""")
    label = (f"""Akar Persamaan: {Xt} \nToleransi Error: {error}""")
    plt.title('Grafik Persamaan Menggunakan Metode Setengah Interval')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.grid(alpha=.4,linestyle='--')
    plt.plot(xax, yax, label=sby)
    plt.plot(Xt, FXt, '--r', marker="o", markersize=5, label=label)
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", error)
            
# Metode Interpolasi Linier [Python 3.7]
def interpolasi_linier():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = float(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    X2 = X1 + 1
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    xaxis = np.array(range(5))
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
        FX2 = (a*(X2)**3)+(b*(X2)**2)+(c*X2)+d
        Xt = X2 - ((FX2/(FX2-FX1)))*(X2-X1)
        FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
        if FXt*FX1 > 0:
            X2 = Xt
            FX2 = FXt
        else:
            X1 = Xt
            FX1 = FXt  
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 250:
            print("=== Angka tak hingga, silahkan periksa nilai penguji!!! ===")
            break
        print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
    y_axis = (a*(xaxis)**3)+(b*(xaxis)**2)+(c*xaxis)+d
    FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    save = (f"""image\{judul}.png""")
    label = (f"""Akar Persamaan: {Xt} \nToleransi Error: {error}""")
    plt.title('Grafik Persamaan Menggunakan Metode Interpolasi Linier')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.grid(alpha=.4,linestyle='--')
    plt.plot(xax, yax, label=sby)
    plt.plot(Xt, FXt, '--r', marker="o", markersize=5, label=label)
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", error)
        
# Metode Secant [Python 3.7]
def secan():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = float(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    X2 = X1 - 1
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    xaxis = np.array(range(5))

    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
        FX2 = (a*(X2)**3)+(b*(X2)**2)+(c*X2)+d
        Xt = X1 - ((FX1)*(X1-(X2)))/((FX1)-(FX2))
        FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if error > 0.0001:
            X2 = X1
            X1 = Xt
        else:
            print("Selesai")
        if iterasi > 1000:
            print("Angka tak hingga")
            break
        print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
    y_axis = (a*(xaxis)**3)+(b*(xaxis)**2)+(c*xaxis)+d
    FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    save = (f"""image\{judul}.png""")
    label = (f"""Akar Persamaan: {Xt} \nToleransi Error: {error}""")
    plt.title('Grafik Persamaan Menggunakan Metode Secan')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.grid(alpha=.4,linestyle='--')
    plt.plot(xax, yax, label=sby)
    plt.plot(Xt, FXt, '--r', marker="o", markersize=5, label=label)
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", error)

# Metode Newton-Rapson [Python 3.7]
def newton_rapson():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = float(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    if (X1 < 0):
        X2 = X1*(-1)
    else:
        X2 = X1
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    xaxis = np.array(range(5))
    iterasi = 0
    akar = 1
    while (akar > 0.0001):
        iterasi += 1
        FX1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
        FX2 = (a*(3*X1)**2)+(b*(2*X1))+(c)
        Xt = X1 - (FX1/FX2)
        FXt = (a*(Xt**3))+(b*(Xt**2))+(c*Xt)+d
        Ea = ((Xt-X1)/Xt)*100
        if Ea < 0.0001:
            X1 = Xt
            akar = Ea*(-1)
        else:
            akar = Xt
            print("Nilai akar adalah: ", akar)
            print("Nilai error adalah: ", Ea)
        if iterasi > 1000:
            break
        print(iterasi, "|", X1, "|", Xt, "|", akar, "|", Ea)
    y_axis = (a*(xaxis)**3)+(b*(xaxis)**2)+(c*xaxis)+d
    FX2 = (a*(3*xax)**2)+(b*(2*xax))+(c)
    FXt = (a*(Xt)**3)+(b*(Xt)**2)+(c*Xt)+d
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    fx2 = (f"""$Y = ({a*3}x^2) + ({b*2}x) + ({c})$""")
    save = (f"""image\{judul}.png""")
    label = (f"""Akar Persamaan: {Xt} \nToleransi Error: {Ea}""")
    plt.title('Grafik Persamaan Menggunakan Metode Newton-Rapson')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.grid(alpha=.4,linestyle='--')
    plt.plot(xax, yax, label=sby, color='red')
    plt.plot(xax, FX2, label=fx2, color='blue')
    plt.plot(Xt, FXt, color='black', marker="o", markersize=5, label=label)
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", akar)  
def iterasi():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = float(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    if (X1 < 0):
        X2 = X1*(-1)
    else:
        X2 = X1
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    xaxis = np.array(range(5))
    error = 1
    iterasi = 0
    while (error > 0.0001):
           iterasi +=1
           FX1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
           X2 = (((b*(-X1**2))+(-c*X1)+(-d))/a)**(0.333334)
           Ea = (((X2-X1)/(X2))*100)
           if Ea < error:
                X1 = X2
                if Ea > 0:
                    error = Ea
                else:
                    error = Ea*(-1)
           else:
                error = Ea
           if iterasi > 100:
                print("Angka tak hingga")
                break
           print(iterasi, "|", X1, "|", X2, "|", Ea, "|", error)
    y_axis = (a*(xaxis)**3)+(b*(xaxis)**2)+(c*xaxis)+d
    FXt = (((b*(-X2**2))+(c*X2)+d)/a)**(0.333334)
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    save = (f"""image\{judul}.png""")
    label = (f"""Akar Persamaan: {X2} \nToleransi Error: {error}""")
    plt.title('Grafik Persamaan Menggunakan Metode Iterasi')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.grid(alpha=.4,linestyle='--')
    plt.plot(xax, yax, label=sby, color='red')
    plt.plot(X2, FXt, color='black', marker="o", markersize=5, label=label)
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", X2)
    print("Toleransi Error: ", error)
print("Kode penggunaan akar-akar persamaan: \n",
  "1. Metode Setengah Interval \n",
  "2. Metode Interpolasi Linier \n",
  "3. Metode Secant \n",
  "4. Metode Newton-Rapson \n",
  "5. Metode Iterasi")
setting = int(input("Masukkan kode penggunaan akar-akar persamaan: "))
if (setting == 1):
    X = setengah_interval()
elif(setting == 2):
    X = interpolasi_linier()
elif(setting == 3):
    X = secan()
elif(setting == 4):
    X = newton_rapson()
else:
    X = iterasi()
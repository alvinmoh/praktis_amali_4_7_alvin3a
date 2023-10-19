'''Ini merupakan satu program ringkas untuk mendapatkan isi padu kuboid'''
pi=3.142
def kira_kuboid(tinggi,panjang,lebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid

def kuboid():  #isi padu kuboid
    tinggi=float(input("Masukkan tinggi: "))
    panjang=float(input("Masukkan panjang: "))
    lebar=float(input("Masukkan lebar: "))
    print("Isi padu kuboid= ",kira_kuboid(tinggi,panjang,lebar))\

def kira_silinder(pi,jejari,tinggi):
    isipadu_silinder=pi*(jejari**2)*tinggi
    return isipadu_silinder

def silinder():  #isi padu silinder
    jejari=float(input("Masukkan jejari: "))
    tinggi=float(input("Masukkan tinggi: "))
    print("Isi padu silinder= ",kira_silinder(pi,jejari,tinggi))
    
def kira_kon(pi,jejari,tinggi):  
    isipadu_kon=(1/3)*pi*(jejari**2)*(tinggi)
    return isipadu_kon
    
def kon():  #isi padu kon
    jejari=float(input("Masukkan jejari: "))
    tinggi=float(input("Masukkan tinggi: "))
    print("Isi padu kon= ",kira_kon(pi,jejari,tinggi))
    
def kira_sfera(pi,jejari):
    isipadu_sfera=4/3*pi*(jejari**3)
    return isipadu_sfera
    
def sfera():  #isi padu sfera
    jejari=float(input("Masukkan jejari: "))
    print("Isi padu sfera= ",kira_sfera(pi,jejari))
    
######################################
#Subatur cara utama
######################################
ulang=True

while(ulang):
    print(
'''
    *********************************
    *     MENU MENGIRA ISI PADU     *
    *********************************
    1.Kuboid
    2.Silinder
    3.Kon
    4.Sfera
    5.Keluar dari program
''')
    print("")
    
    pilih=int(input("Sila masukkan pilihan anda: "))
    
    if(pilih==1):
        kuboid()  #memanggil fungsi kuboid
    elif(pilih==2):
        silinder()  #memanggil fungsi silinder
    elif(pilih==3):
        kon()  #memanggil fungsi kon
    elif(pilih==4):
        sfera()  #memanggil fungsi sfera
    elif(pilih==5):
        ulang=False
        print("Bye Bye~!!<3")
        exit
    else:
        print("Pilihan tiada dalam senarai")
        print("")
    


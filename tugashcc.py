import json

dataBase = [{
    "nama":"Iwan",
    "hobi":"makan",
    "asal daerah":"Parepare",
    "tanggal lahir":"7/12/2005",
    "motto hidup":"Dunia harus seimbang"
}]

changed = None
deleted = None

# create
def create():
    while True:
        nama = input("Masukkan nama : ")
        hobi = input("Masukkan hobi : ")
        asal = input("Masukkan asal daerah : ")
        TLahir = input("Masukkan tanggal lahir : ")
        motto = input("Masukkan motto hidup : ")

        if(nama!="" and hobi!="" and asal!="" and TLahir!="" and motto!=""):
           dataBase.append({
            "nama": nama,
            "hobi": hobi,
            "asal": asal,
            "tanggal lahir": TLahir,
            "motto":motto
        })
           print("data berhasil dibuat ")
           break
        else:
            print("\n Harus mengisi semua data !! \n") 
    

# update
def update(nama):
        global changed
        changed = False

        for d in dataBase:
            if d["nama"] == nama: 
                namaNew = input("Masukkan nama baru : ")
                hobiNew = input("Masukkan hobi baru : ")
                asalNew = input("Masukkan asal daerah baru : ")
                TLahirNew = input("Masukkan tanggal lahir baru : ")
                mottoNew = input("Masukkan motto hidup baru : ")

                def change(d, bio,new):
                    d.update({bio : new}) 

                if namaNew != "": change(d, "nama", namaNew)
                if hobiNew != "": change(d, "hobi", hobiNew)
                if asalNew != "": change(d, "asal", asalNew)
                if TLahirNew != "": change(d, "tanggal lahir", TLahirNew)
                if mottoNew != "": change(d, "motto", mottoNew)
                print("data berhasil diubah \n")
                changed=True

# delete
def delete(nama):
    global deleted
    deleted = False
    for d in dataBase[:]:  
        if d["nama"] == nama:
            dataBase.remove(d)
            print(f"Data dengan nama '{nama}' berhasil dihapus!\n")
            deleted = True
            break  
    if not deleted:
        print(f"Data dengan nama '{nama}' tidak ditemukan.\n")

while True:
    print("Pilihan : create|read|update|delete|exit \n")
    pilihan = input("Masukkan pilihan anda : ")

    if(pilihan == "create" or pilihan == "1"):
        print("")
        create()
    
    elif(pilihan == "read" or pilihan == "2"):
        print("")
        # styling data
        database = json.dumps(dataBase,indent=5)
        print(database,"\n")
    
    elif(pilihan =="update" or pilihan == "3"):
        while True:
            nama = input("Masukkan nama dari data yang ingin diubah : ")
            for d in dataBase:
                if d["nama"] == nama:
                    update(nama)
                    
            if(changed == True):
                    break
    
    elif(pilihan == "delete" or pilihan =="4"):
        while True:
            nama = input("Masukkan nama dari data yang ingin dihapus : ")
            for d in dataBase:
                if d["nama"] == nama:
                    delete(nama)

                        
            if deleted == True:
                break

    elif(pilihan =="exit" or pilihan =="5"):
        print("Terima kasih telah menggunakan program ini! jangan lupa bahagia :)")
        break


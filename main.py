# import library
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# data dummy
hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 50, 450))
hunians.append(Rumah("Gustavo Fring", 5, 2, 400, 900))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 150, 1300))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 150, 450))

# title
root = Tk()
root.title("Latihan Praktikum 9 DPBO | 2007392 Arik Rizki Akbar")

# ------------ Data Detail ------------
def details(index):

    # ------------ Detail Frame ------------
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # ------------ Data Residen Frame ------------
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # ------------ display data ------------
    # summary
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    
    # pemilik
    d_pemilik = Label(d_frame, text="Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=1, column=0, sticky="w")
    
    # jumlah kamar jika bukan indekos
    if hunians[index].get_jenis() != "Indekos":
        d_jml_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=2, column=0, sticky="w")
    
    # dokumen
    d_document = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=3, column=0, sticky="w")

    # luas tanah
    d_luasTanah = Label(d_frame, text="Luas Tanah: " + hunians[index].get_luasTanah(), anchor="w").grid(row=4, column=0, sticky="w")

    # listrik
    d_listrik = Label(d_frame, text="Kapasitas Listrik: " + hunians[index].get_listrik(), anchor="w").grid(row=5, column=0, sticky="w")

    # ------------ button frame ------------
    opts_detail = LabelFrame(top, padx=10, pady=10)
    opts_detail.pack(padx=10, pady=10)

    # exit button
    b_exit = Button(opts_detail, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # back button
    b_back = Button (opts_detail, text = "Back", command = top.destroy)
    b_back.grid(row=0, column=0)


# ------------ MAIN FRAME ------------
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ------------ button frame ------------
opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# add button
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

# exit button
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# ------------ Main Data ------------
for index, h in enumerate(hunians):

    # kolom nomer
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # kolom jenis hunian
    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # kolom nama pemilik hunian
    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # detail button
    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()

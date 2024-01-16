import tkinter as tk

def hitung_bmi():
    try:
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get()) / 100  # Mengonversi tinggi ke meter
        bmi = berat / (tinggi ** 2)
        label_hasil.config(text=f"Hasil BMI: {bmi:.2f}")
        
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid untuk berat dan tinggi.")

    if bmi >= 18.5 and bmi <= 22.9:
        label_kategori.config(text="Berat badan anda termasuk kategori Normal")
    elif bmi < 18.5:
        label_kategori.config(text="Berat badan anda termasuk kategori Dibawah Normal")
    elif bmi > 22.9:
        label_kategori.config(text="Berat badan anda termasuk kategori Diatas Normal")
        
# Membuat instance Tkinter
root = tk.Tk()
root.title("Kalkulator BMI")

# Input berat
label_berat = tk.Label(root, text="Berat (kg):")
label_berat.grid(row=0, column=0, padx=10, pady=10)
entry_berat = tk.Entry(root)
entry_berat.grid(row=0, column=1, padx=10, pady=10)

# Input Tinggi 
label_tinggi = tk.Label(root, text="Tinggi (cm):")
label_tinggi.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=1, column=1, padx=10, pady=10)

# Tombol execute
tombol_hitung = tk.Button(root, text="Hitung BMI", command=hitung_bmi)
tombol_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=3, column=0, columnspan=2, pady=10)

# Menampilkan kategori 
label_kategori = tk.Label(root,text="")
label_kategori.grid(row=4, column=0, columnspan=2, pady=10)



# Menjalankan GUI
root.mainloop()

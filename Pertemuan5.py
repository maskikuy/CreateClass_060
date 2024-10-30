class PersegiPanjang:
    # Konstruktor
    def __init__(self, panjang, lebar):
        self.panjang = panjang  # properti panjang
        self.lebar = lebar      # properti lebar
    
    # Fungsi menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    # Fungsi menghitung luas 
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    # Fungsi str untuk menampilkan string object
    def __str__(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

# 6 command untuk testing
# 1. Membuat object persegi panjang
pp = PersegiPanjang(3, 2)

# 2. Menampilkan properti panjang
print(f"Panjang: {pp.panjang} cm")

# 3. Menampilkan properti lebar
print(f"Lebar: {pp.lebar} cm")

# 4. Menghitung dan menampilkan keliling
print(f"Keliling: {pp.hitung_keliling()} cm")

# 5. Menghitung dan menampilkan luas
print(f"Luas: {pp.hitung_luas()} cm²")

# 6. Menampilkan string representasi object
print(pp)
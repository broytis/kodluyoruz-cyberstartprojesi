import math

# Adım 1: Noktaların tanımlanması
# Örnek noktalar (kendi noktalarınızı buraya ekleyin)
noktalar = [(1, 2), (4, 6), (5, 1), (3, 3)]

# Adım 2: İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Adım 3: Mesafelerin hesaplanması ve saklanması
mesafeler = []

for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append((noktalar[i], noktalar[j], mesafe))

# Adım 4: Minimum mesafenin bulunması
min_mesafe = min(mesafeler, key=lambda x: x[2])

# Sonuçların yazdırılması
print("Tüm mesafeler:")
for m in mesafeler:
    print(f"{m[0]} ve {m[1]} arasındaki mesafe: {m[2]:.2f}")

print(f"Minimum mesafe: {min_mesafe[0]} ve {min_mesafe[1]} arasındaki {min_mesafe[2]:.2f}")

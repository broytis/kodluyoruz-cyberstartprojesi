import math

points = [(1, 2), (4, 6), (5, 1), (3, 3)]

# Adım 2: İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Adım 3: Mesafelerin hesaplanması ve saklanması
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))

# Adım 4: Minimum mesafenin bulunması
min_distance = min(distances, key=lambda x: x[2])

# Sonuçların yazdırılması
print("Tüm mesafeler:")
for d in distances:
    print(f"Arasındaki mesafe {d[0]} ve {d[1]}: {d[2]:.2f}")

print(f"Minimum mesafe: {min_distance[0]} ve {min_distance[1]} arasındaki {min_distance[2]:.2f}")

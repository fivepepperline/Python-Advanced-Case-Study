
import random

def generator_iot(n=10):
    for i in range(n):
        suhu = random.uniform(15, 38)
        yield round(suhu, 1)


if __name__ == "__main__":
    jumlah_data = 0
    semua_valid = True

    for suhu in generator_iot():
        jumlah_data += 1

        if not 15 <= suhu <= 38:
            semua_valid = False

        if suhu < 20: 
            kategori = "Dingin"
        elif suhu <= 30:
            kategori = "Normal"
        else:
            kategori = "Panas"

        print(f"Pembacaan {jumlah_data}: {suhu}°C - Kategori: {kategori}")

    print(f"\nJumlah pembacaan: {jumlah_data}")
    print(f"Semua suhu valid: {semua_valid}")
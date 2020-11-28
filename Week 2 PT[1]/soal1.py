import statistics 
import math

arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    # Minimum
    bMin = min(arrBerat)
    # Maksimum
    bMax = max(arrBerat)
    


def rerata(arrBerat):
    total = 0
    
    # Definisikan Proses Mencari Rerata Dari Total Berat
    nilai_rata = sum(arrBerat) / len(arrBerat)

    # Return Hasil Rerata
    return nilai_rata


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    data_berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(data_berat)
    


# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)



# Print Data Minimum, Maximum, dan Rerata Berat
print(f'Rerata Berat Balita  : {round(bMin, 2)} kg')
print(f'Rerata Berat Balita  : {round(bMax, 2)} kg')
print(f'Rerata Berat Balita  : {round(rerata(arrBerat), 2)} kg')
klub_a = input('Klub A : ')
klub_b = input('Klub B : ')
arData = []
kondisi = True
while kondisi:
    for i in range (9999):
        print(f'Pertandingan Ke-{i+1} :', end=' ')
        skor_a,skor_b = input().split()
        convert_a = int(skor_a)
        convert_b = int(skor_b)

        if convert_a > convert_b:
            arData.append(klub_a)
        elif convert_a < convert_b:
            arData.append(klub_b)
        
        if (convert_a | convert_b < 0):
            for i in range (i):
                hasil = arData[i]
                print(f'Hasil {i+1} : ',hasil)
            kondisi = False    
            break    

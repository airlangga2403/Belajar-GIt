def half_pyramid_pattern(rows):
    for i in range(0,rows):
         for j in range(0, i+1):
              print("* " , end="")
         print("\r")
            

def half_pyramid_pattern_inverted(rows):
    for i in range(rows, -1, -1):
           for j in range(0, i + 1):
               print("* ", end="")
           print("\r")
           
def half_pyramid_pattern_mirrored(rows):
    k = 2*rows - 2
    for i in range(0, rows): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 2
        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 

def full_pyramid_pattern(rows):
    
    k = 2*rows - 2
    for i in range(0, rows): 

        for j in range(0, k): 
            print(end=" ") 
      
        k = k - 1
      
        for j in range(0, i+1):
            print("* ", end="") 
      

        print("\r") 

def full_pyramid_pattern_inverted(rows):
    for i in range(rows,0,-1):
        for j in range(rows-i):
            print(' ', end='')    
        for k in range(2*i-1):
            print('*',end='') 
        print()

def print_pattern(pattern,row):
    print(" ")


#¯\_(ツ)_/¯
def tampil_menu_segitiga():
    print('1.Half Pyramid Pattern')
    print('2.Half Pyramid Pattern Inverted')
    print('3.Half Pyramid Pattern Mirrored')
    print('4.Full Pyramid Pattern')
    print('5.Full Pyramid Inverted Pattern')

tampil_menu_segitiga()
pattern = int(input('Pilih jenis pattern \t: '))
rows = int(input('Pilih banyak baris \t: '))
print ("\n")
if pattern == 1:
    half_pyramid_pattern(rows)
elif pattern == 2:
    half_pyramid_pattern_inverted(rows)
elif pattern == 3:
    half_pyramid_pattern_mirrored(rows)
elif pattern == 4:
    full_pyramid_pattern(rows)
elif pattern == 5:
    full_pyramid_pattern_inverted(rows)
else:
    print("Input Salah")
print('===============================')
print_pattern(pattern,rows)
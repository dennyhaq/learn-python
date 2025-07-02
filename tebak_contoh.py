import random

def pilihan(difficulity):
    if(difficulity=='1'):
        return 10
    if(difficulity=='2'):
        return 5
    if(difficulity=='3'):
        return 3
    else:
        return None

def gamestebakangka():
    print("""selamat datang digames tebak angka
          saya berikan nomor 1-100 coba tebak
          
          silahkan pilih level
          1. gampang, 10 kesempatan
          2 sedang 5 kesempatan
          3 susah 3 kesempatan

          """)
    difficulity = input("silahkan pilih 1/2/3: ").strip()
    peluang=pilihan(difficulity)
    
    print(peluang)
    if peluang is None:
        print("salah pilih")
        return
    print(f"bagus, level dipilih {'gampang' if difficulity=='1' else 'sedang' if difficulity =='2' else 'susah'}")
    print("mulai permainan \n")

    jawaban = random.randint(1,100)
    percobaan=0

    while(peluang>0):
        try:
            tebak1=int(input('masukan nonor '))
            percobaan += 1
            if(tebak1==jawaban):
                print(f"selamat jawaban benar dalam {percobaan} ")
                break
            elif(tebak1<jawaban):
                print(f"salah jawaban lebih besar dari {tebak1}")
            else:
                print(f"salah jawaban lebih kecil dari {tebak1}")

            peluang -= 1
            if(peluang>0):
                print(f"masih ada {peluang} kesempatan lagi ")
            else:
                print(f"kesempatan habis, yg benar {jawaban} ")
        except ValueError:
            print("pilih  antara 1 2 3")

if __name__ == "__main__":
    gamestebakangka()







            




import random

def randint(min=0,max=100):
    a = random.randint(min,max)
    return a


print("""program pyton untuk menebak angka
tebak nomor antara 1 dan 100

masukkan nomor """);



num1 = int (input())

if num1 == 1 :
    print("level susah")
    susah()
elif num1 == 2: 
    print ("level sedang")
elif num1 == 3: 
    print ("level mudah")

else: 
    print("pilih 1-3")
    

def susah():
    print("jawaban {jawab}")
    tebakan = int (input())
    if jawab > tebakan:
        print("kuranng dari jawaban") 
    elif jawab > tebakan:
        print("lebih besar dari {jawab}")

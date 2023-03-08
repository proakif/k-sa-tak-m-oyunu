puan1 = int(input("1.takımın puanı: "))
puan2 = int(input("2.takımın puanı: "))
puan3 = int(input("3.takımın puanı: "))
puan4 = int(input("4.takımın puanı: "))

if puan1 > puan2 and puan1 > puan3 and puan1 > puan4 :
    print("1.takım kazandı")
elif puan2 > puan1 and puan2 > puan3 and puan2 > puan4:
    print("2.takım kazandı")
elif puan3 > puan1 and puan3 > puan2 and puan3 > puan4:
    print("3.takım kazandı")
elif puan4 > puan1 and puan4 > puan2 and puan4 > puan3:
    print("4.takım kazandı")
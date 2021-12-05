slovo=""
while len(slovo)<6:
    try:
        slovo=input("Введите слово:")
    except:
        print("Слишком короткое слово")
        ValueError

print("Слово состоит из",len(slovo),"букв")
while True:
    print("Список-1,Сортировка(Букв)-2,в обратном порядке-3,Индекс/Удалить-4,Первый/Последний-5")
    print("Большими буквами-6,Маленькими буквами-7,С заглавной буквы-8,Обмен регистра-9,")
    valik=int(input())
    if valik==1:
        spisok=list(slovo)
        valik=input("Ряд-1,Столбец-2")
        if valik=="1":
            print(spisok)
        elif valik=="2":
            for bukva in spisok:
                print(bukva)
    elif valik==2:
        spisok=list(slovo.lower())
        spisok2=[]
        for bukva in spisok:
            if bukva not in spisok2:spisok2.append(bukva)
        spisok2.sort()
        print(spisok2)
    elif valik==3:
        spisok=list(slovo.lower())
        spisok.reverse()
        print(spisok)
    elif valik==4:
        spisok=list(slovo.lower())
        bukva=input("Введите Букву:")
        print("1.Вариант")
        t=0
        indexs=[]
        for b in spisok:
            t+=1
            if b==bukva:
                print("Буква",bukva,"Расположенна на",t,"месте")
                indexs.append(t-1)
        valik=int(input("Подтвердить? Да-1"))
        if valik==1:
            p=0
            for i in indexs:
                spisok.pop(i-p)
                p+=1
            print(spisok)
    elif valik==5:
        spisok=list(slovo.lower())
        print(spisok[0],"-Первое буква")
        print(spisok[-1],"-Последняя буква")
    elif valik==6:
        spisok=list(slovo.upper())
        print(spisok)
    elif valik==7:
        spisok=list(slovo.lower())
        print(spisok)
    elif valik==8:
        spisok=list(slovo.capitalize())
        print(spisok)
    elif valik==9:
        spisok=list(slovo.swapcase())
        print(spisok)
    elif valik==10:
        spisok=list(slovo.
        print(spisok)

    


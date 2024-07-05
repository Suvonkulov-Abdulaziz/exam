# list=[]
# while(True):
#     print("1. Kitob qo'shish\n2. Kitobni nomi bo'yicha qidirish\n3. Barcha kitoblarni ko'rsatish\n4. Chiqish")
#     choose=int(input("Tanlovingizni kiriting: "))
#     if choose==1:
#         list.append(str(input("kitob nomi: ")))
#     elif choose==2:
#         print(str(input("qidirish: ")) in list)
#     elif choose==3:
#         for l in list:
#             print(l)
#     elif choose==4:
#         break
#     else :
#         print("notogri son")


def unique(l):
    bool=False
    if l[0]==0:
        bool=True
    list=[0]
    for i in range(0,len(l)):
        if l[i] != list[len(list)-1]:
            list.append(l[i])
    if bool:
        pass
    else:
        list.pop(0)
    return list

list=[1, 1, 2, 2, 3,0,0, 3, 3, 4, 4, 5,2,2]
print(unique(list))
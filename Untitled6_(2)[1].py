#!/usr/bin/env python
# coding: utf-8

# In[6]:


for i in range (1,11):
    print("*************************************")
    for j in range (1,11):
        print("{}x{}={}".format(i,j,i*j))


# In[9]:


for i in range (1, 101):
    if(i % 3 == 0)


# In[11]:


list = [x for x in range (1, 101) if x % 3 == 0]
print (list)


# In[2]:


sayac = 1 
while sayac <= 5:
    print(sayac)
    sayac += 1


# In[4]:


i = 0

while ( i < 10 ):
    print("i'nin değeri", i)
    i += 1


# In[5]:


i = 0

while ( i < 20 ):
    print("i'nin değeri", i)
    i += 2


# In[10]:


i = 0

while ( i < 40 ):
    print("Python Öğreniyorum")
    
    i += 1


# In[11]:


list = [1,2,3,4,5,6]

a = 0

while (a < len(list)):
    print("indeks: ", a, "Eleman: ",list [a])
    a +=1


# In[13]:


sayac = 0
giris = "yes"

while giris !="no" and giris !="No":
    print (sayac)
    giris = input("Devam etmek için Yes, Çıkmak için No giriniz:")
    if giris == "Yes" or giris == "yes":
        sayac += 1
    elif giris == "no" and giris == "No":
        print("Giriş geçerli değil")


# In[16]:


sayi = 0
toplam = 0

while sayi >= 0:
    sayi = int(input("Bir sayı giriniz: "))
    toplam += sayi
    print("Toplam = ", toplam)


# In[18]:


karar = False
while not karar:
    giris = int(input())
    if giris == 999:
        karar = True
    else:
        karar =False
        


# In[21]:


while True: 
    isim = input ("İsminiz (Çıkmak için q tuşuna basın): ")
    if (isim == "q"):
        print("çıkış yapılıyor")
        break
    print(isim)


# In[24]:


i = 0

while ( i < 10 ):
    if (i == 2):
        i += 1
        continue
        
    print("i: ", i)
    i += 1
    


# In[39]:


kelime = input("Bir kelime giriniz:")
sesliharfsayisi = 0

for c in kelime:
    if c == "a" or  c == "A" or  c == "E" or  c == "e" or        c == "U" or  c == "u" or  c == "O" or c == "o" or  c == "ı" or         c == "I" or c == "ü" or  c == "Ü" or  c == "Ö" or c == "ö" or        c == "İ" or  c == "i" :
        print (c, ",", end=" ", sep=" ")
        sesliharfsayisi += 1
    elif c == "X" or c == "x":
        break
print("(", seslihafsayisi,"adet sesli harf)", sep=" ")


# In[50]:


sayi = int(input("Bir sayi Giriniz: "))
i = 1
toplam = 0
while (i<sayi):
    if (sayi%i==0):
        toplam += i
    i += 1
if (toplam == sayi):
    print(sayi, "Mükemmel sayıdır")
else:
    print("Mükemmek sayı değildir!")


# In[ ]:


sayi = input("Bir Sayi Giriniz: ")
basamaks = len(sayi)

basamak = 0
toplam = 0
sayi=int(sayi)
gecici_sayi=sayi

while(gecici_sayi>0):
    basamak = gecici_sayi % 10
    toplam += basamak ** basamaks
    gecici_sayi //=10

if (toplam == sayi):
    print(sayi, "Bir armstrong sayıdır")
else:
    print(sayi, "Bir armstrong sayı değildir")


# In[ ]:


while True:
    x = int(input("X değeri giriniz"))
    y = int (input("Y değeri giriniz"))


    if (x>0 and y>0):
        print("{},{} Birinci Bölge".format(x, y))
        
    elif (x<0 and y>0):
        print("{},{} ikinci bölge".format(x, y))
        
    elif (x<0 and y<0):
        print("{},{} Üçüncü Bölge".format(x, y))
        
    else:
        print("{},{} Dördüncü Bölge".format(x, y))
     


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





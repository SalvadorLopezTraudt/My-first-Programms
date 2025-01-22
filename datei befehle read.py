import sys

f = open("name.txt" , "r") # liest alle bytes, (n) kann limit setzen
namen = f.read()
print(namen)
f.close()

f = open("name.txt" , "r") # liest nur eine zeile (3) zeigt byte limit = Fre
namen1 = f.readline(3)
print(namen1)
f.close()

f = open("name.txt" , "r") # liest alle zeilen und macht liste draus 
namen2 = f.readlines()
print(namen2)
f.close()
        






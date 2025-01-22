listeo = [1,2,3,4,5]

listeo.append(6) # name der liste.append und wert in klammern fügt einzelnen wert hinzu
print(listeo)

six = [7,8,9]
listeo.extend(six) #fügt die genannte variable hinzu 
print(listeo)

listeo.insert(0 , 0) # erste zahl ist der index, zweite der wert
print(listeo)

listeo.pop(0) #löscht den wert von dem angegeben index(0)
print(listeo)

listeo.pop() # ohne index wird letzte wert der liste gelöscht
print(listeo)

listeo.remove(8) # Entfernt das erste Element mit dem Wert von value(8)
print(listeo)

listeo.reverse() # dreht die liste um
print(listeo)

listeo.sort() # sortiert nach größe 
print(listeo)

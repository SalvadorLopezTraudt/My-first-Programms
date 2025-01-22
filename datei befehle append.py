f = open("append.txt", "a") # öffnet datei und fügt "text" hinzu
text = f.write(" " "du bist dumm.") # legt datei an wenn nicht existiert
f.close()

f= open("append.txt" , "a")
text = f.write(input())

text2 = ["Hmmmm"," ", "Ahhhh", " ", "Ohhhhh"]
f = open("append.txt" , "a")
text = f.writelines(text2) # fügt liste von strings hinzu
f.close()




f = open("append.txt" ,"r")
text = f.read()
print(text)
        
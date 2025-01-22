f =open("append.txt" , "w") # öffnet datei zum schreiben und überschreibt
text = f.write("nein, du bist schlau.")# wenn nicht existiert, macht neue datei
f.close()

f = open("append.txt" , "r")
text = f.read()
print(text)


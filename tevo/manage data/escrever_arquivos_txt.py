# TXT
with open("tevo/manage data/main.txt", "a") as txt:
    txt.write("Teste número 1\n")

### OR

txt = open("tevo/manage data/main.txt", "a") # OPEN
txt.write("Teste número 2")
txt.close() # CLSOE



arquivo = open("tevo/manage data/main.txt")
print(arquivo.read())


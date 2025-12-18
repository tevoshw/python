#CRIAR UM VERIFICADOR DE NOTA
#RECEBE 3 INPUT DO USUARIO
#CALCULA A MEDIA ENTRE ELES
#SE FOR MENOR QUE 7 ESTÁ REPROVADO
#SE FOR MAIOR QUE 7 ESTÁ APROVADO

noia1 = input("qual foi a sua nota?: ")
noia2 = input("qual foi a sua nota?: ")
noia3 = input("qual foi a sua nota?: ")
media = ( int(noia1) + int(noia2) + int(noia3) / 3
if media < 7:
    print(f"voce foi reprovado, sua nota foi: {media}")
else:
    print(f"voce foi aprovado, sua nota foi: {media}")

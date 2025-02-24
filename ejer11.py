'''






Haz que el usuario ingrese emociones como "feliz", 
"triste" o "sorprendido" y el programa mostrará 
un emoji hecho con caracteres ASCII.

'''
emojis={
    "feliz": "😃",
    "triste": "😭",
    "fachero": "😎",
    "sorprendido": "😱"
}
emocion= input("¿Cómo te sientes hoy? (feliz, triste, fachero, sorprendido): ").lower()
print(emojis.get(emocion, "No entiendo la emoción, no existe esa emoción"))
#FELIZ
#feliz
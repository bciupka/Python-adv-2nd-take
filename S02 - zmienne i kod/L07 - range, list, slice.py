#coding=windows-1250
colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def colorChooser(amount, list):
    colors = list[:amount]
    return colors

for i in range(1, len(colors)+1):
    print(colorChooser(i, colors))


korpo = '''
Korporacja (z �ac. corpo � cia�o, ratus � szczur; pol. cia�o szczura) � organizacja,
kt�ra pod przykrywk� prowadzenia biznesu w�ada dzisiejszym �wiatem. Wydawa� si� mo�e utopijnym miejscem
realizacji pasji zawodowych. W rzeczywisto�ci jednak nie jest wcale tak kolorowo. Korporacja s�u�y do
wyzyskiwania cz�owieka w imi� post�pu. Rz�dzi w niej prawo d�ungli.
'''

print(korpo[korpo.index("(")+1:korpo.index(")")])
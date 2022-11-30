#coding=windows-1250
colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def colorChooser(amount, list):
    colors = list[:amount]
    return colors

for i in range(1, len(colors)+1):
    print(colorChooser(i, colors))


korpo = '''
Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja,
która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem
realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do
wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.
'''

print(korpo[korpo.index("(")+1:korpo.index(")")])
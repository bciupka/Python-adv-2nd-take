#coding=windows-1250

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for i, j in zip(projects, leaders):
    print("Projektu", i, "Liderem", j)


dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i, j, k in zip(projects, dates, leaders):
    print("Projekt:", i, "Data:", j, "Lider:", k)

for i, (j, k, l) in enumerate(zip(projects, dates, leaders)):
    print("Nr:", i+1,"Projekt:", j, "Data:", k, "Lider:", l)

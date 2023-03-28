dautomat={} #dicitonar in dictionar pentru automat
starifinale=[]

sw=0
f = open('exemplu.in', 'r')
linie=f.readlines()
x=[i for i in linie[0].split()]
for i in range(1,len(linie)-1):
    linie[i]=[x for x in linie[i].split()]
    if linie[i][0] not in dautomat.keys():
        dautomat[linie[i][0]]={linie[i][1]: linie[i][2]}

    elif linie[i][1] in dautomat[linie[i][0]]:
        print("Nu este AFD, este un AFN")
        sw=1
    else:
        dautomat[linie[i][0]][linie[i][1]]=linie[i][2]
starifinale=[i for i in linie[len(linie)-1].split()]

if sw==0:
  cuvant=input('Cuvantul testat: ')
  cuvant=[i for i in cuvant]
for z in x:
    starecurenta=z
    drum=[z]
    for i in range(len(cuvant)):
        if cuvant[i] in dautomat[starecurenta]:
          drum.append(dautomat[starecurenta][cuvant[i]])
          starecurenta=drum[len(drum)-1]
        else:
          print("Nu este acceptat")
    if starecurenta in starifinale:
      print("Drumul:", *drum)
    else:
       print("Nu este acceptat")



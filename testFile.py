
f = open("sentence_Box.txt", "r", encoding="utf-8")
fr = f.read()
lfr = fr.split('\n')


f2 = open("BOW.txt", "r", encoding="utf-8")
fr2 = f2.read()
lfr2 = fr2.split('\n')
listm = lfr2+["안녕하세요."]
print(type(listm))

listfr = [list(lfr[i]) for i in range(0, len(list(lfr)))]
comlist = listfr[0]
# print(type(comlist[0]))
import json
# from konlpy.tag import Okt
# okt = Okt()
file_path = "감성대화말뭉치.json"
with open(file_path, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

jdic1 = json_data[0]
jdic2 = jdic1['talk']
jdic3 = jdic2['content']
# HS01 = jdic3['HS01']

HS01 = [k for k in range(0,9171)] # len = 9171
HS02 = [j for j in range(0, 9171)]
HS03 = [q for q in range(0, 9171)]
SS01 = [r for r in range(0, 9171)]
SS02 = [x for x in range(0, 9171)]
SS03 = [z for z in range(0, 9171)]

for i in range(0, len(json_data)):
    jdic1 = json_data[i]
    jdic2 = jdic1['talk']
    jdic3 = jdic2['content']
    HS01[i] = jdic3['HS01']
    HS02[i] = jdic3['HS02']
    HS03[i] = jdic3['HS03']
    SS01[i] = jdic3['SS01']
    SS02[i] = jdic3['SS02']
    SS03[i] = jdic3['SS03']

HSBOX = HS01+HS02+HS03
# f = open("sratings.txt", "r", encoding="utf-8")
# fr = f.read()
# flr = list(fr)
# fr2 = fr.split("\t")
# fr3 = fr2[3:len(fr2)]
# BOW = SSBOX+fr3
# sente = [okt.nouns(BOW[i]) for i in range(0, len(BOW))]
f=open("sentence_BOX.txt","w", encoding="utf-8")

for i in range(0, len(HSBOX)):
    file=f.write(str(HSBOX[i])+"\n")






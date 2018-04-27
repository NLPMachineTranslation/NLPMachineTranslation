from nltk import *

def main():
    #list of the sentences
    engWord = []
    filWord = []

    #read english corpus
    fileEng = open("All.en", "r", encoding="utf-8")
    l1 = fileEng.readlines()
    for i in l1:
        engWord.extend(word_tokenize(i))
    fileEng.close()

    #read filipino corpus
    fileFil = open("All.fl", "r", encoding="utf-8")
    l2 = fileFil.readlines()
    for i in l2:
        filWord.extend(word_tokenize(i))
    fileFil.close()

    fdisteng = FreqDist(engWord)
    fdistfil = FreqDist(filWord)

    engCount = len(fdisteng)
    filCount = len(fdistfil)

    #write
    f1 = open("FreqDistEng.data", "w", encoding="utf-8")
    for i in fdisteng.most_common(engCount):
        temp = i[1]/engCount
        f1.write(str(i[0]) + ' ' +str(temp))
        f1.write("\n")
    f1.close()

    f2 = open("FreqDistFil.data", "w", encoding="utf-8")
    for i in fdistfil.most_common(filCount):
        temp = i[1]/filCount
        f2.write(str(i[0]) + ' ' +str(temp))
        f2.write("\n")
    f2.close()

    print("Success")

if __name__ == "__main__":
    main()
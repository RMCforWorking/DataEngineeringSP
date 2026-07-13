text = 'to be or not to be that is the question whether tis nobler in the mind to suffer'

def sorty(e):
    return e[1]

def sortAlpfa():
    alpa = list(freq.items())
    alpa.sort()
    for tmp in alpa:
        if tmp[1]!=1:
            alpa.remove(tmp)
    print(alpa)

def haveSameCount(word1:str,word2:str)->bool:
    if freq[word1]==freq[word2]:
        return True
    return False
if __name__ == '__main__':
    freq={}
    text=text.lower()
    for word in text.split():
        freq[word]=freq.get(word,0)+1

    words=list(freq.items())
    words.sort(key=sorty,reverse=True)
    k=0
    for word,count in words:
        print(f"{word} : {count}")
        k+=1
        if k==3:
            break
    sortAlpfa()
    first=input("give the first word ")
    second=input("give the second word ")

    print(haveSameCount(first,second))
    print(freq)
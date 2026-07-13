submissions = ['alice','bob','carol','alice','dave','bob','alice','eve','carol']

def duplicateFinder():
    seen = {}
    for item in submissions:
        if item in seen:
            yield item
        else:
            seen[item]=item

def findNrUsers(seen,nr):
    freq={}
    for item in submissions:
        if item in seen:
            freq[item]=freq.get(item,0)+1

    listofusers=[]
    for key,value in freq.items():
        if value == nr:
            listofusers.append(key)
    return listofusers

def istaken(username,seen):
    return username in seen

if __name__=='__main__':
    duplicates=duplicateFinder()
    print(set(duplicates))

    seen = []
    for item in submissions:
        if item not in seen:
            seen.append(item)

    print(seen)

    freq=findNrUsers(seen,2)
    print(f"pentru 2 aparitii {freq}")
    freq = findNrUsers(seen, 3)
    print(f"pentru 3 aparitii {freq}")
    freq = findNrUsers(seen, 4)
    print(f"pentru 4 aparitii {freq}")

    print(f"Is alice taken? {istaken('alice',seen)}")

    unique=findNrUsers(submissions,1)
    print(len(unique))
playlist=[]

def addtoList(song,index=-1):
    if index==-1 or index>len(playlist):
        playlist.append(song)
    else:
        playlist.insert(index,song)

def moveList(i=0,j=-1):
    if j==-1:
        j= len(playlist)-1
    tmp=playlist.pop(i)
    playlist.insert(j,tmp)

def removeSong(name):
    try:
        playlist.remove(name)
        print('Song removed successfully')
    except Exception as e:
        print('The song was already removed due to the fact that it wasnt in the list, great work!\n')


def coolerPrint():
    for i in range(0,len(playlist)):
        print(str(i) + '.' + playlist[i])

if __name__ =="__main__":
    #task 1
    addtoList('Blinding Lights')
    addtoList('Levitating')
    addtoList('Peaches')

    #task 2
    addtoList('Stay',2)
    #task 3
    print(playlist)
    print('\n --------- \n')
    moveList()
    print(playlist)

    #task 4
    """
    print('\n --------- \n')
    removeSong('Smell of the game')
    removeSong('Peaches')
    """

    print('\n --------- \n')
    print('What song does the user want to remove?\n')
    song=input()
    removeSong(song)

    #task 5
    coolerPrint()



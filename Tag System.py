posts = {
 'A': {'python', 'tutorial', 'beginner', 'coding'},
 'B': {'python', 'advanced', 'decorators', 'coding'},
 'C': {'javascript', 'tutorial', 'beginner', 'web','python'},
 'D': {'python', 'tutorial', 'coding', 'tips'},
}

def sametag(given):
    found=[]
    for key,value in posts.items():
        if len(given.intersection(value))==2:
            found.append(key)
    return found
if __name__ == "__main__":
    print(posts['A'].intersection(posts['B']))
    print(posts['A'].difference(posts['B']))
    print(posts['A'].union(posts['B']))

    x=list(posts.values())
    common=x[0].intersection(*x[1:])
    z={}
    k=0
    for post in posts.values():
        if not k:
            z=post
            k+=1
        else:
            z=z.intersection(post)

    print(z)
    print(common)

    givenPost={'python','coding'}
    print(sametag((givenPost)))
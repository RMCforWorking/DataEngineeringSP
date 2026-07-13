logs = [
 'auth: User alice logged in',
 'db: Query executed in 12ms',
'auth: ERROR invalid token for user bob',
 'api: GET /orders 200 OK',
 'db: ERROR connection timeout',
 'api: POST /checkout 201 Created',
 'auth: User carol logged in',
 'api: GET /products 200 OK',
]

if __name__ == '__main__':
    print(logs[-5:])
    print(logs[::2])
    logs.reverse()
    print(logs)

    errors=[]
    for error in logs:
        if 'ERROR' in error:
            errors.append(error)
    print(errors)

    sursa={}
    for line in logs:
        s=line.split(':',1)[0]
        sursa[s]=sursa.get(s,0)+1
    print(sursa)
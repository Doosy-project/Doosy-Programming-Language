
print('This is the pypto module')
print('Use it to make any cryptocurrency related programs')
print('It can also be used to setup a local pypto server')
print('use "instructions()" to show how to use pypto ')
blockchain=[]
block=0
m1=0
m2=0
m3=0
m4=0
mine=120
dta=0
preblock=[]
finder=0
tomine=[]
tick=0
reqdata=0
    
def makeserver(name):
    import os
    from http.server import HTTPServer, CGIHTTPRequestHandler
    os.chdir(name)
    server_object = HTTPServer(server_address=('LOCALPYTOSERVER', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever(name)
    
def dhash(dta):
    import random as r
    toehash = dta
    toehash += 1
    toehash += toehash
    toehash *= 2
    toehash += r.randint(1, 9)
    toehash *= r.randint(11111111, 99999999)
    return toehash

def addblock(toehash):
    blockchain.append(toehash)

def mine():
    while mine != 0:
        m1+=m2
        m2+=m3
        m3+=m4
        m4+=m1
        m1+=toehash
        dhash(m1)
        blockchain.append(m1, m2, m3, m4)
        mine -= 0.5
        print(mine)
    dta = m1 + m2 + m3 + m4 + reqdata
    
def findrequests():
    tick = 12
    while tick != 0:
        tomine.append(preblock[tick])
        tick -= 1
    print(tomine)
def put_in_request(reqdata):
    server_object = HTTPServer(server_address=('requests', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    preblock.append(reqdata)
    
def instructions():
    print('makeserver("server name") makes a server with the name')
    print('dhash("data") hashes the data in the ()')
    print('addblock("hash") adds a block with whatever is in the ()')
    print('mine() mines for you')
    print('findrequests() finds a list of block requests')
    print('put_in_requests("data") makes a block request for the data in the ()')
    print('instructions() brings up this text!')




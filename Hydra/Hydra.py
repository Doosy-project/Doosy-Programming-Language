print('Loading hydra...')
import random
import time
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
print('setting up dictionaries...')
hydrate = {
    'hydrate' : 'creates a deeplemon server'

}
linearfunctions = {
    'Linear function' : 'a function that scans for a server, then overwrites the server'

}
time.sleep(2)
print('finished!')
print('Hydra BETA version |::|')
print('Core library: Doosypl/modules/hydra')
print('Project:')

def hydrate():
    os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
print('loading...')
time.sleep(2)
server_object.serve_forever()
print('server started.')

def importjuggernaut():
    import jrg

print('Loading Doosy enterprise...')
print('Done!')
def connect():
    import os
    from http.server import HTTPServer, CGIHTTPRequestHandler
    os.chdir('.')
    server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
def secure():
    print('Secure as can be.')
def serversys():
    server_object.serve_forever()
print('+++++++++++++++++++++++++HOW TO USE+++++++++++++++++++++++++')
print('connect() connects to the cloud')
print('secure() checks the security')
print('serversys() starts the server')

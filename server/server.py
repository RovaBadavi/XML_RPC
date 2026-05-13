# 1. Write import statements here
import socket
import subprocess
from bs4 import BeautifulSoup

# 2. Write code here to establish connection with the client
host_name = '0.0.0.0'
port = 2222

server_socket = socket.socket()
server_socket.bind((host_name, port))
server_socket.listen()

print(f"Server listening on port {port}...")

# 3. Write code here to start an infinite loop
while True:
    # 4. Write code here to accept client connection and receive XML file
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    
    try:
        data = client_socket.recv(4096)
        print(f"Received XML: {data}")
        
        # 5. Write code here to parse XML file
        # then execute the proper method to get the result
        soup = BeautifulSoup(data, 'xml')
        method_name = soup.find('method').getText()
        args = soup.find_all('arg')
        result = None
        
        if method_name == 'square':
            arg_value = args[0].getText()
            output = subprocess.run(['bash', 'square.sh', arg_value], capture_output=True, text=True)
            result = output.stdout.strip()
            
        elif method_name == 'sum':
            arg_values = []
            for arg in args:
                arg_values.append(arg.getText())

            output = subprocess.run(['bash', 'sum.sh'] + arg_values, capture_output=True, text=True)
            result = output.stdout.strip()
            
        elif method_name == 'gcd':
            arg_values = []
            for arg in args:
                arg_values.append(arg.getText())

            output = subprocess.run(['bash', 'gcd.sh', arg_values[0], arg_values[1]], capture_output=True, text=True)
            result = output.stdout.strip()
        
        else:
            print("Please provide a valid method")
        
        # 6. Write code here to wrap the result in an XML message and send it to the client
        response_xml = f"""<envelope>
                    <result>{result}</result>
                    </envelope>"""
        
        client_socket.sendall(response_xml.encode('utf-8'))
        print(f"Sent response: {result}")
    
    finally:
        client_socket.close()
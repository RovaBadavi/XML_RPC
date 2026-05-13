# client.py
#1. Write import statements here
import socket
import sys
import xml.etree.ElementTree as ET


#2. Write code here to establish connection with the server
SERVER_HOST = '192.168.56.10'  
SERVER_PORT = 2222      

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")


#3. Write code to get the XML file from the command-line argument 
    if len(sys.argv) < 2:
        print("Use the following format: python client.py <xml_file>")
        sys.exit(1)

    xml_file_path = sys.argv[1]
    with open(xml_file_path, 'r') as file:
        xml_data = file.read()
        print(f"Read XML data from {xml_file_path}")


#4. Write code to send the XML file to the server 
    client_socket.send(xml_data.encode('utf-8'))    


#5. Write code to receive the response XML file from the server, 
# and print the result to the screen 
    response_data = client_socket.recv(4096).decode('utf-8')
    print("Received response from server")

    if response_data:
        try:
            root = ET.fromstring(response_data)
            print("Parsed XML Response")
            result = root.find('result').text

            print("_________________")
            print(f"Result: {result}")
            print("-----------------")
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")

except Exception as e:
    print(f"An error occurred: {e}")


#6. Write code to close the connection
finally:
    client_socket.close()    
    print("Connection closed.")
# XML-RPC Client–Server Control System

A Python client–server application that uses socket communication to transfer XML-based remote procedure calls between a local client and a virtual machine server.

## Features
- Sends XML method requests from client to server
- Parses XML messages using Python
- Executes server-side Bash functions
- Supports square, sum, and GCD operations
- Returns XML-formatted responses to the client

## Technologies Used
- Python
- XML
- Socket Programming
- Bash
- Virtual Machine

## How It Works
The client sends an XML message containing a method name and arguments. The server receives the message, parses it, runs the matching Bash script, and sends the result back as an XML response.

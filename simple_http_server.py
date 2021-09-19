from os import read
import socket

host = '0.0.0.0'
port = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)

def handle_request(client_socket: socket,file_path:str):
  file_path_formatted = file_path[1:]
  print(file_path)
  print(file_path_formatted)
  response =""
  with open(file_path_formatted, 'r') as file:
    if(file_path_formatted.split('/')[0] == "html"):
      response = "HTTP/1.0 200 OK\nContent-Type:text/html\n\n" + file.read() 
      client_socket.sendall(response.encode())
    if(file_path_formatted.split('/')[0] == "css"):
      response = "HTTP/1.0 200 OK\nContent-Type:text/css\n\n" + file.read() 
      client_socket.sendall(response.encode())
  with open(file_path_formatted ,"rb") as file:
    if(file_path_formatted.split(".")[1] =="ico"):
      client_socket.send("HTTP/1.0 200 OK".encode())
      client_socket.send("Content-Type:image/x-icon\n\n".encode())
      client_socket.send(file.read())
    if(file_path_formatted.split(".")[1] =="png"):
      client_socket.send("HTTP/1.0 200 OK".encode())
      client_socket.send("Content-Type:image/png\n\n".encode())
      client_socket.send(file.read())
    if(file_path_formatted.split(".")[1] =="jpeg"):
      client_socket.send("HTTP/1.0 200 OK".encode())
      client_socket.send("Content-Type:image/jpeg\n\n".encode())
      client_socket.send(file.read())

while True:
  try:
    cl_socket, cl_addr = server_socket.accept()
    req = cl_socket.recv(1024).decode()
    file_path = req.split("\n")[0].split(" ")[1]
    cl_socket.send
    if file_path == "/":
      file_path =  "/html/index.html"
    elif file_path == "/css/":
      file_path = "/css/style.css"
    handle_request(cl_socket, file_path)
    cl_socket.close()
  except KeyboardInterrupt:
    raise SystemExit


server_socket.close()
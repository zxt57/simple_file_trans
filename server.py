import socket
import threading

PORT = 5678
SIZE = 1024
FORMAT = "utf-8"

def receive_data(conn, addr):
  print(f"{addr} connected.")

  filename = conn.recv(SIZE).decode(FORMAT)
  print(f"Receiving the file : {filename}")
  conn.send(filename.encode(FORMAT))

  with open(filename, 'w') as f:
    data = conn.recv(SIZE)
    while data:
      f.write(data)
      data = conn.recv(SIZE)

  conn.close()
  print(f"{addr} disconnected.")


def start_server():
  
  server = socket.socket()
  server.bind((socket.gethostname(),PORT))
  server.listen(16)
  print("Server is listening.")
  
  while True:
    conn, addr = server.accept()
    threading.Thread(target=receive_data, args=(conn,addr)).start()


if __name__ == "__main__":
  start_server()

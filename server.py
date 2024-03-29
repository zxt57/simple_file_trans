import socket
import threading

PORT = 5678
SIZE = 1024
TIMEOUT = 20
MAX_LISTEN = 16
FORMAT = "utf-8"

def receive_data(conn, addr):

  try:
    print(f"{addr} connected.")
    conn.settimeout(TIMEOUT)
    
    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"Receiving the file : {filename}")
    conn.sendall(filename.encode(FORMAT))

    with open(filename, 'wb') as f:
      data = conn.recv(SIZE)
      while data:
        f.write(data)
        data = conn.recv(SIZE)
        
  except Exception as e:
    print(f"Error on conn {addr} : ", e)

  finally:
    conn.close()
    print(f"{addr} disconnected.")


def start_server():
  
  server = socket.socket()
  server.bind((socket.gethostname(),PORT))
  server.listen(MAX_LISTEN)
  print("Server is listening.")
  
  while True:
    conn, addr = server.accept()
    threading.Thread(target=receive_data, args=(conn,addr)).start()

# from multiprocessing import Process
# Process(target=start_server).start()
start_server()

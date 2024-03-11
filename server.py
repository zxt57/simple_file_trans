import socket
PORT = 5678
SIZE = 1024
FORMAT = "utf-8"

def main():
  print("[STARTING] Server is starting.")
  server = socket.socket()
  server.bind((socket.gethostname(),PORT))
  server.listen(16)
  print("[LISTENING] Server is listening.")
  while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "w")
    conn.send("Filename received.".encode(FORMAT))

    data = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    conn.send("File data received".encode(FORMAT))

    file.close()

    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
    
if __name__ == "__main__":
  main()

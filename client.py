import socket
IP = socket.gethostname()
PORT = 4455
FORMAT = "utf-8"
SIZE = 1024

def main():
  client = socket.socket()
  client.connect((IP,PORT))
  
  file = open("data/yt.txt", "r")
  data = file.read()
  
  client.send("yt.txt".encode(FORMAT))
  msg = client.recv(SIZE).decode(FORMAT)
  print(f"[SERVER]: {msg}")
  
  client.send(data.encode(FORMAT))
  msg = client.recv(SIZE).decode(FORMAT)
  print(f"[SERVER]: {msg}")
  
  file.close()
  client.close()
  
if __name__ == "__main__":
  main()

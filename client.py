import socket
import threading

IP = socket.gethostname()
PORT = 5678
SIZE = 1024
TIMEOUT = 60
FORMAT = "utf-8"

def send(filename, file_data):
  
  try:
    client = socket.socket()
    client.settimeout(TIMEOUT)
    client.connect((IP,PORT))
    client.sendall(filename.encode(FORMAT))
    re_msg = client.recv(SIZE).decode(FORMAT)
    if re_msg != filename:
      raise Exception(f"Received filename {re_msg} different from {filename}")
    print(f"sending file {re_msg}")
    client.sendall(file_data)

  except Exception as e:
    print("Error : ", e)
    
  finally:
    client.close()


def thread_send(filename, file_data):
  threading.Thread(target=send, args=(filename,file_data)).start()
  

if __name__ == "__main__":
  file = open("test_text.txt", "rb")
  data = file.read()
  thread_send("test_rec.txt", data)
  file.close()
  

import base64
import codecs
import json 
import telnetlib

socket = telnetlib.Telnet("socket.cryptohack.org",13377)

try:
  
    stage = 0
    
    while stage <= 100:
      data = json.loads(socket.read_until(b"\n").decode())
      
      encoding_type = data["type"]
      encoded = data["encoded"]
      
      if encoding_type == "base64":
        decoded = base64.b64decode(encoded.encode()).decode
      
      if encoding_type == "hex":
        decoded = bytes.fromhex(encoded).decode("ASCII")
      
      if encodeing_type == "rot13":
        decoded = codecs.decode(encoded, "rot_13")
      
      if encodig_type == "bigint":
        decoded = bytes.formhex(encoded[2:]).decode()
       
      if encoding_type == "utf-8":
        decoded = ""
        
        for char in [chr(b) for b in encoded]:
          decoded += char
      print("[*] {} | Successfully decoded : {}".format(stage + 1, encoded))
      socket.write(json.dumps({"decoded": decoded}).encode())
      stage += 1
except:
  print("\n[+] Flag : {}".format(data["flag"]))

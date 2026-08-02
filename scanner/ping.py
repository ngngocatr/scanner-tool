import platform
import subprocess

# ping -c 4 IP 

def ping(host):
    #OS check
    option_ping=''
    OS_NAME=platform.system().lower()
    if ('windows' in OS_NAME):
        option_ping='-n';
    elif ('linux' in OS_NAME):
        option_ping='-c'
    # Run command
    res = subprocess.run(
       ['ping', option_ping, '4', host],
        capture_output=True,
        text=True
    )

    if (res.returncode==0):
        if ('ttl' in res.stdout.lower()):
            return True
        else:
            return False
    return False

# print(ping('127.0.0.1'))
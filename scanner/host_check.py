import platform
import subprocess
from scanner.port_scan import common_ports_scan

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

def check_live_host(host):
    is_live_host=ping(host)
    if (is_live_host==True):
        return is_live_host
    
    common_ports_scan(host)
    return is_live_host

# print(check_live_host('127.0.0.1'))
    
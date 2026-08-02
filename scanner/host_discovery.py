from scanner.ping import ping
from scanner.port_scan import common_ports_scan

def check_live_host(host):
    is_live_host=ping(host)
    if (is_live_host==True):
        return is_live_host
    
    common_ports_scan(host)
    return is_live_host

# print(check_live_host('127.0.0.1'))
    
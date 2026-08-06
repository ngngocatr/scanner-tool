import socket


def common_ports_scan(host):
    COMMON_PORTS=[21,22,23,25,80,443,3389,8080,8000]
    open_port_list=[]

    for port in COMMON_PORTS:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)
        result = scanner.connect_ex((host, port))
        if (result==0):
            open_port_list.append(port)
            break

    if (len(open_port_list)!=0):
        return True
    else:
        return False

# print(common_ports_scan("192.168.1.201"))

# host: string
# port: list
def scan_ports(host, port_range):
    try:
        open_ports_list={} # dictionary saves ports:services
        for i in port_range:
            # socket(family_address, protocol)
            # TCP
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # timeout = 0.3s
            scanner.settimeout(0.3)
            # connect_ex((IP, port))
            result = scanner.connect_ex((host, i))
            # check and display
            if result==0:
                service_name = get_service_name(i)
                print(f'[+] {i}/tcp\tOPEN\t{service_name}')
                open_ports_list[i] = service_name
        print(f"Total ports scanned: {len(open_ports_list)}")
    finally:
        scanner.close()
        print('\n[OK] Closed socket')

    return open_ports_list

# Get service by port
## port: int
def get_service_name(port):
    service_name = ''
    try:
        service_name = socket.getservbyport(port)
    except:
        service_name = 'unknown'

    return service_name
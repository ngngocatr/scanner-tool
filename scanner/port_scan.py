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
import socket


# 0<= x <=255
def is_ip_number(number):
    if (number <= 255 and number >=0):
        return True
    else:
        return False

'''
IP hợp lệ
--> 4 octet --> là số nguyên --> 0<x<255
'''
def validate_ip(IP):
    try:
        # Check từng octet có valid không
        IP_OCTETS=list(map(int, IP.split(".")))
        if (len(IP_OCTETS)==4 and is_ip_number(IP_OCTETS[0]) and is_ip_number(IP_OCTETS[1]) and is_ip_number(IP_OCTETS[2]) and is_ip_number(IP_OCTETS[3])):
            # print(IP_OCTETS)
            return True
        return False
    except:
        return False

# DNS
def resolve_domain(domain_name):
    domain_name=domain_name.strip()
    try:
        ip = socket.gethostbyname(domain_name)
        return ip
    except(socket.gaierror):
        return None

# Validate port

# Trường hợp 1: một dải port liên tiếp (nhận 1 list 2 phần tử ([start, end]) 
## Phải trong khoảng (1, 65535)
## Start Port phải nhỏ hơn End Port

# Trường hợp 2: Một port duy nhất
## Phải trong khoảng (1, 65535)

# Trường hợp 3: Một list port có sẵn
## Tất cả phải nằm trong khoảng (1, 65535)

def parse_port(ports):  # ports là chuỗi
    try:
        ports=ports.strip()
        if '-' in ports:
            start, end = map(int, ports.split('-'))

            if not validate_port_range(start, end):
                return False

            port_list = list(range(start, end + 1))
            mode = 'range'

        elif ',' in ports:
            port_list = list(map(int, ports.split(',')))

            if not validate_port_list(port_list):
                return False

            mode = 'list'

        else:
            port = int(ports)

            if not validate_single_port(port):
                return False

            port_list = [port]
            mode = 'single'
        port_list.sort()
        return mode, port_list

    except ValueError:
        return False


def validate_single_port(port):
    return 1 <= port <= 65535


def validate_port_range(start, end):
    return 1 <= start <= end <= 65535


def validate_port_list(ports):
    if len(ports) == 0:
        return False

    return all(1 <= port <= 65535 for port in ports)
    
    

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

def resolve_domain(domain_name):
    domain_name=domain_name.strip()
    try:
        ip = socket.gethostbyname(domain_name)
        return ip
    except(socket.gaierror):
        return None
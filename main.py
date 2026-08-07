import argparse
import time
import pyfiglet

from scanner.host_check import check_live_host
from scanner.target import validate_ip, resolve_domain, parse_port
from scanner.port_scan import scan_ports, display_scan_info
from config import COMMON_PORTS

# IS_ERR = False


# Banner
def banner_display():
    text = pyfiglet.figlet_format("SCANNER")
    print(text)

# Load arguments
def parse_arg():
    parser = argparse.ArgumentParser(
        description="Basic Scanner"
    )

    # require arguments
    parser.add_argument(
        "host",
        help="IPv4, URL or domain"
    )

    # check live host
    parser.add_argument(
        '-l','--live-host',
        action="store_true",
        help='Check live host by ping and resonse of port'
    )

    parser.add_argument(
            '-p','--port',
            # action="store_true", # với cờ có giá trị thì không được để action="store_true"
            # type=str, # mặc định nhận string nên không cần 
            help='Specify the port range to scan, for example: 1-1000'
    )

    parser.add_argument(
                '--common',
                action="store_true",
                # type=str, # mặc định nhận string nên không cần 
                help='Scan common ports'
        )
    
    return parser.parse_args()

# Lấy IP trong cả trường hợp nhập IP và domain
def get_target_ip(host):
    # Nếu người dùng nhập IP
    if validate_ip(host):
        return host

    # Nếu người dùng nhập domain
    else:
        print("Đang phân giải tên miền....")
        print('-'*48)
        ip=resolve_domain(host)
        if (ip is None):
            print("[!] Không thể phân giải tên miền!")
            print("[!] Vui lòng nhập lại!")
            return
        else:
            print(f'[+] Phân giải thành công: {ip}')
            return ip

# In trạng thái của host: up/down
def display_host_status(ip):
    if (validate_ip(ip)):
        print(f'Đang kiểm tra live host....')
        print('-'*48)
        if check_live_host(ip):
                print(f'[+] Host {ip} is up')
        else:
                print(f'[+] Host {ip} is down or not response')
    else:
        print(f'[!] IP {ip} invalid!')

# Scan port by range
def scan_port_range(host, port_input):
    parsed_result = parse_port(port_input)
    # print(parsed_result)
    if parsed_result is False:
        print('[!] Invalid ports!')
        return []

    mode, port_list = parsed_result

    display_scan_info(host, mode, port_list)
    print('[+] Scanning.......')


    open_ports = scan_ports(host, port_list)
    return open_ports
    

def main():
    banner_display()
    args = parse_arg()

    host=args.host

    # get IP/domain from user imput
    ip=get_target_ip(host)

    # check live hosts
    if args.live_host:
        display_host_status(ip)

    
    # Scan ports
    if args.port:
        if validate_ip(ip):
            scan_port_range(ip, args.port)

    # Scan common ports
    if args.common:
        if validate_ip(ip):
            scan_port_range(ip, COMMON_PORTS)
    
if __name__=="__main__":
    # Start time
    start = time.perf_counter()

    # Exit by Ctrl + C
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    # End time
    end = time.perf_counter()
    print(f"[+] Tổng thời gian quét: {end - start:.2f} giây")

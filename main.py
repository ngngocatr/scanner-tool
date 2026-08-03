import argparse
from scanner.host_check import check_live_host
from scanner.target import validate_ip, resolve_domain


def parse_arg():
    parser = argparse.ArgumentParser(
        description="Basic Scanner"
    )

    parser.add_argument(
        "host",
        help="IPv4, URL or domain"
    )

    parser.add_argument(
        '-l','--live-host',
        action="store_true",
        help='Check live host by ping and resonse of port'
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
        print('----------------------------')
        ip=resolve_domain(host)
        if (ip is None):
            print("Không thể phân giải tên miền!")
            print("Vui lòng nhập lại!")
            return
        else:
            print(f'Phân giải thành công: {ip}')
            return ip

# In trạng thái của host: up/down
def display_host_status(ip):
    if (validate_ip(ip)):
        print(f'Đang kiểm tra live host....')
        print('----------------------------')
        if check_live_host(ip):
                print(f'Host {ip} is up')
        else:
                print(f'Host {ip} is down or not response')
    else:
        print(f'IP {ip} invalid!')

def main():
    args = parse_arg()

    host=args.host

    ip=get_target_ip(host).strip()

    if args.live_host:
        display_host_status(ip)
    

    
    

if __name__=="__main__":
    main()
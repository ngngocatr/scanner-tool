import socket, threading
from concurrent.futures import ThreadPoolExecutor, as_completed



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


def scan_ports(host, port_range, workers, verbose = False):
    open_ports_list = {}
    completed = 0
    total_ports = len(port_range)
    threads = []
    previous_open_count = 0

    # Multi threads
    # Limit number of thread by max_worker of ThreadPoolExcutor
    with ThreadPoolExecutor(max_workers=workers) as excutor:
        futures = []
        try:
            for port in port_range:
                future = excutor.submit(scan_port, host, port, open_ports_list)
                futures.append(future)

            for future in as_completed(futures):
                completed+=1

                current_open_count = len(open_ports_list)

                if current_open_count != previous_open_count:
                    print(
                        f"\n[+] Found {current_open_count} open port(s)"
                    )

                    previous_open_count = current_open_count

                if verbose==True:
                    percent = completed/total_ports*100.0
                    print(
                        f"\rScanning: {percent:.0f}% "
                        f"[{completed}/{total_ports}]",
                        end=""
                    )
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")

            for future in futures:
                future.cancel()

            excutor.shutdown(
                wait=False,
                cancel_futures=True
            )

            return open_ports_list
        
        if verbose==True:
            print()

    print('-'*48)    
    # In port mở sau khi scan xong
    for port, service in sorted(open_ports_list.items()):
        print(f"[+] {port}/tcp\tOPEN\t{service}")

    print('-'*5)
    print(f"[+] Total ports scanned: {total_ports}")
    print(f"[+] Open ports: {len(open_ports_list)}")

    return open_ports_list

# Each port prints on one line
print_lock = threading.Lock()


def scan_port(host, port, open_ports_list):
    try:
        # TCP
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # timeout = 0.3s
        scanner.settimeout(0.3)
        # connect_ex((IP, port))
        result = scanner.connect_ex((host, port))
        if result==0:
            service_name = get_service_name(port)
            open_ports_list[port] = service_name

    finally:
        if scanner:
            scanner.close()

# Display status scan
def display_scan_info(host, mode, port_list, workers):
    print('-'*48)
    print(f'[+] Target: {host}')
    print(f'[+] Mode: {mode}')
    print(f'[+] Number of Threads: {workers}')


    # Display scope
    scope = ''
    if mode=='range':
        scope=f'{port_list[0]} --> {port_list[-1]}'
    elif mode=='list':
        for port in port_list:
            scope+=str(port)+' '
    else:
        scope=port_list[0]
    print(f'[+] Scope ({mode}): {scope}')

    print('-'*48)

# Get service by port
## port: int
def get_service_name(port):
    service_name = ''
    try:
        service_name = socket.getservbyport(port)
    except:
        service_name = 'unknown'

    return service_name
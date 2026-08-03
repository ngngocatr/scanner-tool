import argparse
from scanner.host_check import check_live_host


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

def main():
    args = parse_arg()

    # print(args.host)
    # print(args.live_host)
    HOST=args.host

    # Check live host
    if (check_live_host(HOST)==True):
            print(f'Host {HOST} is up')
    else:
            print(f'Host {HOST} is down or not response')

    

if __name__=="__main__":
    main()
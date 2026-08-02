# Simple Port Scanner

Công cụ quét cổng TCP đơn giản được viết bằng Python, phục vụ mục đích học tập về lập trình mạng, thư viện `socket` và `argparse`.

> Chỉ sử dụng trên hệ thống của bạn hoặc hệ thống đã được cho phép kiểm tra.

## Chức năng

* Kiểm tra host bằng ICMP Ping
* Kiểm tra các cổng TCP phổ biến
* Quét một cổng hoặc một dải cổng
* Hiển thị danh sách cổng mở
* Hỗ trợ thiết lập timeout

## Cấu trúc project

```text
simple-port-scanner/
├── main.py
├── README.md
├── scanner/
│   ├── __init__.py
│   ├── host_discovery.py
│   └── port_scanner.py
└── tests/
```

* `main.py`: nhận tham số và điều khiển chương trình
* `host_discovery.py`: kiểm tra host có hoạt động không
* `port_scanner.py`: kiểm tra và quét cổng
* `tests/`: chứa các file kiểm thử

## Cách chạy

```bash
python main.py 192.168.1.200
```

Quét một dải cổng:

```bash
python main.py 192.168.1.200 --start-port 1 --end-port 1000
```

Xem hướng dẫn:

```bash
python main.py --help
```

## Luồng hoạt động

```text
Nhận host
    ↓
Ping host
    ↓
Nếu không phản hồi, kiểm tra common ports
    ↓
Quét dải cổng
    ↓
Hiển thị cổng mở
```

## Lưu ý

Host không phản hồi ping chưa chắc đã tắt vì firewall có thể chặn ICMP.

Không tìm thấy cổng mở cũng không chắc chắn host không hoạt động.

## Mục đích

Project được xây dựng để tìm hiểu cách một port scanner hoạt động. Đây không phải công cụ thay thế cho Nmap, Masscan hoặc RustScan.

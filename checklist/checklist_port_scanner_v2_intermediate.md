# CHECKLIST PHÁT TRIỂN PORT SCANNER — V2 INTERMEDIATE

> Mục tiêu: nâng cấp từ port scanner TCP cơ bản lên phiên bản nhanh hơn, linh hoạt hơn và có cấu trúc tốt hơn.

> Chỉ sử dụng trên máy của bạn, môi trường lab hoặc hệ thống được cấp phép kiểm thử.

---

## 1. Quét đa luồng

- [ ] Học `threading.Thread`
- [ ] Hiểu `target=...`
- [ ] Hiểu `args=(...)`
- [ ] Hiểu `start()`
- [ ] Hiểu `join()`
- [ ] Chia danh sách port cho nhiều thread
- [ ] Thử quét bằng 10 thread
- [ ] Thử quét bằng 50 thread
- [ ] So sánh thời gian với bản quét tuần tự
- [ ] Không tạo quá nhiều thread mất kiểm soát
- [ ] Học `ThreadPoolExecutor`
- [ ] Cho phép chọn số worker bằng CLI

Ví dụ:

```bash
python main.py 192.168.1.10 -p 1-1000 -t 50
```

---

## 2. Chế độ quét common ports

- [ ] Tạo danh sách common ports
- [ ] Viết hàm `scan_common_ports()`
- [ ] Thêm tham số `--common`
- [ ] Cho phép quét một port duy nhất
- [ ] Cho phép quét một khoảng port

Ví dụ:

```bash
python main.py 192.168.1.10 --common
```

```bash
python main.py 192.168.1.10 -p 80
```

```bash
python main.py 192.168.1.10 -p 1-1000
```

Common ports gợi ý:

```text
21 22 23 25 53 80 110 135 139 143
443 445 3306 3389 5432 8080
```

---

## 3. Nâng cấp argparse

- [ ] `target` là positional argument
- [ ] Thêm `-p / --ports`
- [ ] Thêm `-t / --threads`
- [ ] Thêm `--common`
- [ ] Thêm `--timeout`
- [ ] Thêm `-v / --verbose`
- [ ] Thêm `-o / --output`
- [ ] Thêm `--skip-ping`
- [ ] Hiển thị help rõ ràng
- [ ] Validate các tham số CLI

Ví dụ:

```bash
python main.py scanme.nmap.org -p 1-1000 -t 50 --timeout 0.5 -v
```

---

## 4. Host discovery

- [ ] Ping target trước khi scan
- [ ] Hiển thị khi host phản hồi
- [ ] Cảnh báo khi host không phản hồi ICMP
- [ ] Không kết luận host chết chỉ vì ping thất bại
- [ ] Cho phép vẫn scan khi ping thất bại
- [ ] Thêm `--skip-ping`
- [ ] Xử lý timeout khi ping

Ví dụ:

```text
Host appears up
```

hoặc:

```text
Host did not respond to ICMP
```

---

## 5. Banner grabbing

- [ ] Viết hàm `grab_banner(ip, port)`
- [ ] Connect tới port đang mở
- [ ] Dùng `recv()` để nhận banner
- [ ] Decode bytes thành string
- [ ] Đặt timeout ngắn
- [ ] Xử lý service không tự gửi banner
- [ ] Xử lý lỗi socket
- [ ] Không để banner grabbing làm treo scanner
- [ ] Test với SSH
- [ ] Test với FTP
- [ ] Test với web server trong lab

Ví dụ:

```text
22/tcp OPEN ssh OpenSSH_9.6
```

---

## 6. Phát hiện service tốt hơn

- [ ] Giữ `socket.getservbyport()`
- [ ] Lấy banner thực tế nếu có
- [ ] So sánh service theo port với banner
- [ ] Lưu service name
- [ ] Lưu version nếu phát hiện được
- [ ] Hiển thị `unknown` nếu không xác định được
- [ ] Không khẳng định service chỉ dựa vào port mặc định

Ví dụ:

```text
8080/tcp OPEN http Apache/2.4.58
```

---

## 7. Xuất kết quả

- [ ] Xuất kết quả `.txt`
- [ ] Xuất kết quả `.json`
- [ ] Xuất kết quả `.csv`
- [ ] Viết hàm `export_txt()`
- [ ] Viết hàm `export_json()`
- [ ] Viết hàm `export_csv()`
- [ ] Không trộn logic scan với logic export
- [ ] Cho phép chọn file bằng `-o / --output`

Ví dụ:

```bash
python main.py 192.168.1.10 -p 1-1000 -o result.json
```

Ví dụ JSON:

```json
{
    "target": "192.168.1.10",
    "open_ports": [
        {
            "port": 22,
            "service": "ssh"
        }
    ]
}
```

---

## 8. Cải thiện output terminal

- [ ] Hiển thị bảng kết quả rõ ràng
- [ ] Dùng màu cho trạng thái `OPEN`
- [ ] Dùng màu cho warning
- [ ] Dùng màu cho error
- [ ] Thêm verbose mode
- [ ] Thêm quiet mode nếu cần
- [ ] Hiển thị progress nếu quét nhiều port
- [ ] Tìm hiểu thư viện `rich`

---

## 9. Refactor cấu trúc project

Cấu trúc gợi ý:

```text
port-scanner/
│
├── main.py
│
├── scanner/
│   ├── __init__.py
│   ├── tcp.py
│   ├── host.py
│   ├── banner.py
│   └── service.py
│
├── utils/
│   ├── validator.py
│   └── output.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

Checklist:

- [ ] `main.py` chủ yếu điều phối chương trình
- [ ] Logic TCP scan nằm trong module riêng
- [ ] Host discovery nằm trong module riêng
- [ ] Banner grabbing nằm trong module riêng
- [ ] Service detection nằm trong module riêng
- [ ] Validation tách riêng
- [ ] Output/export tách riêng
- [ ] Hạn chế biến global
- [ ] Các hàm ưu tiên `return` dữ liệu thay vì `print`

---

## 10. Testing

- [ ] Test một port mở
- [ ] Test một port đóng
- [ ] Test 1000 port
- [ ] Test threaded scan
- [ ] Test với nhiều số lượng worker
- [ ] Test timeout
- [ ] Test host không tồn tại
- [ ] Test host chặn ping
- [ ] Test `--skip-ping`
- [ ] Test banner grabbing
- [ ] Test Ctrl+C khi đang chạy nhiều thread
- [ ] Test export TXT
- [ ] Test export JSON
- [ ] Test export CSV
- [ ] Bắt đầu học `pytest`

---

## Chưa cần làm ở V2

- [ ] Chưa cần SYN scan
- [ ] Chưa cần UDP scan
- [ ] Chưa cần OS fingerprinting
- [ ] Chưa cần subnet scanning
- [ ] Chưa cần packet crafting bằng Scapy
- [ ] Chưa cần vulnerability detection
- [ ] Chưa cần CVE lookup
- [ ] Chưa cần AI analysis
- [ ] Chưa cần giao diện GUI

---

## Thứ tự phát triển đề xuất

```text
BASIC ✅
   ↓
Threading
   ↓
ThreadPoolExecutor
   ↓
Common-port scan
   ↓
Nâng argparse
   ↓
Host discovery
   ↓
Banner grabbing
   ↓
Service/version detection
   ↓
JSON / CSV / TXT
   ↓
Refactor project
   ↓
pytest
   ↓
V2 HOÀN THÀNH
```

---

## Tiêu chí hoàn thành V2

Phiên bản V2 được xem là hoàn thành khi tool có thể:

- [ ] Nhận IP hoặc domain từ CLI
- [ ] Quét một port hoặc một khoảng port
- [ ] Quét common ports
- [ ] Quét đa luồng
- [ ] Cho phép tùy chỉnh số worker
- [ ] Kiểm tra host trước khi scan
- [ ] Có thể bỏ qua host discovery
- [ ] Phát hiện service cơ bản
- [ ] Thử lấy banner/version
- [ ] Hiển thị kết quả rõ ràng
- [ ] Xuất TXT/JSON/CSV
- [ ] Xử lý Ctrl+C và lỗi socket tốt
- [ ] Code được chia module rõ ràng
- [ ] Có test cho các chức năng chính

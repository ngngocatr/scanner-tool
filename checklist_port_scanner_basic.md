# CHECKLIST PHÁT TRIỂN PORT SCANNER — PHIÊN BẢN CƠ BẢN

> Mục tiêu: xây dựng một công cụ quét cổng TCP đơn giản bằng Python.
>
> Chỉ sử dụng trên máy của bạn, môi trường lab hoặc hệ thống được cấp phép kiểm thử.

---

## 1. Nhập mục tiêu

- [X] Cho phép nhập địa chỉ IP hoặc tên miền
--> Nếu IP --> quét\
--> Nếu domain --> Phân giải --> quét
- [X] Xóa khoảng trắng thừa bằng `strip()`
- [X] Chuyển tên miền thành IP bằng `socket.gethostbyname()`
- [X] Báo lỗi khi tên miền không tồn tại
- [X] Hiển thị IP sau khi phân giải thành công

Ví dụ:

```text
Target: example.com
Resolved IP: 93.184.216.34
```

---

## 2. Nhập phạm vi cổng

- [X] Nhập cổng bắt đầu
- [X] Nhập cổng kết thúc
- [X] Chuyển dữ liệu nhập sang kiểu `int`
- [X] Kiểm tra cổng nằm trong khoảng `1–65535`
- [X] Kiểm tra cổng bắt đầu không lớn hơn cổng kết thúc
- [X] Báo lỗi nếu người dùng nhập chữ hoặc ký tự không hợp lệ

Ví dụ:

```text
Start port: 1
End port: 1000
```

---

## 3. Quét TCP

- [ ] Tạo socket bằng `socket.socket()`
- [ ] Sử dụng IPv4 với `socket.AF_INET`
- [ ] Sử dụng TCP với `socket.SOCK_STREAM`
- [ ] Đặt thời gian chờ bằng `settimeout()`
- [ ] Dùng `connect_ex()` để kiểm tra cổng
- [ ] Xác định cổng mở khi `connect_ex()` trả về `0`
- [ ] Quét lần lượt từng cổng trong phạm vi
- [ ] Đóng socket sau mỗi lần kiểm tra
- [ ] Không để chương trình bị treo khi gặp firewall

---

## 4. Hiển thị cổng mở

- [ ] Chỉ hiển thị các cổng đang mở
- [ ] Hiển thị số cổng
- [ ] Hiển thị giao thức `tcp`
- [ ] Hiển thị trạng thái `OPEN`

Ví dụ:

```text
22/tcp   OPEN
80/tcp   OPEN
443/tcp  OPEN
```

---

## 5. Hiển thị tên dịch vụ

- [ ] Dùng `socket.getservbyport(port, "tcp")`
- [ ] Hiển thị tên dịch vụ tương ứng với số cổng
- [ ] Xử lý trường hợp không xác định được dịch vụ
- [ ] Hiển thị `unknown` khi tra cứu thất bại

Ví dụ:

```text
22/tcp    OPEN   ssh
80/tcp    OPEN   http
8080/tcp  OPEN   unknown
```

> Tên dịch vụ chỉ được suy đoán theo số cổng, không khẳng định dịch vụ thực tế đang chạy.

---

## 6. Lưu kết quả quét

- [ ] Tạo danh sách chứa các cổng mở
- [ ] Không chỉ in kết quả trực tiếp trong hàm quét
- [ ] Lưu số cổng và tên dịch vụ
- [ ] Sắp xếp kết quả theo số cổng

Ví dụ:

```python
open_ports = []
```

---

## 7. Đo thời gian quét

- [ ] Import thư viện `time`
- [ ] Ghi thời điểm bắt đầu bằng `time.perf_counter()`
- [ ] Ghi thời điểm kết thúc
- [ ] Tính tổng thời gian quét
- [ ] Hiển thị thời gian với hai chữ số thập phân

Ví dụ:

```text
Scan completed in 3.25 seconds
```

---

## 8. Hiển thị tổng kết

- [ ] Hiển thị target người dùng đã nhập
- [ ] Hiển thị IP đã phân giải
- [ ] Hiển thị phạm vi cổng đã quét
- [ ] Hiển thị danh sách cổng mở
- [ ] Hiển thị tổng số cổng mở
- [ ] Hiển thị tổng thời gian quét
- [ ] Thông báo khi không tìm thấy cổng mở

Ví dụ:

```text
Target: 192.168.1.10
Port range: 1-1000

22/tcp   OPEN   ssh
80/tcp   OPEN   http

Open ports found: 2
Scan completed in 3.25 seconds
```

---

## 9. Xử lý lỗi cơ bản

- [ ] Xử lý IP hoặc tên miền không hợp lệ
- [ ] Xử lý cổng không hợp lệ
- [ ] Xử lý lỗi chuyển chuỗi sang số
- [ ] Xử lý lỗi socket
- [ ] Cho phép dừng chương trình bằng `Ctrl + C`
- [ ] Không để chương trình hiện traceback dài
- [ ] Hiển thị thông báo lỗi rõ ràng

Các lỗi nên xử lý:

```python
socket.gaierror
ValueError
OSError
KeyboardInterrupt
```

---

## 10. Chia chương trình thành các hàm

- [ ] Hàm phân giải target
- [ ] Hàm kiểm tra phạm vi cổng
- [ ] Hàm quét một cổng
- [ ] Hàm lấy tên dịch vụ
- [ ] Hàm quét nhiều cổng
- [ ] Hàm hiển thị kết quả
- [ ] Hàm `main()`

Khung chương trình:

```python
def resolve_target(target):
    pass


def validate_ports(start_port, end_port):
    pass


def scan_port(ip, port):
    pass


def get_service_name(port):
    pass


def scan_ports(ip, start_port, end_port):
    pass


def display_results(results):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## 11. Kiểm thử phiên bản cơ bản

- [ ] Quét `127.0.0.1`
- [ ] Quét một cổng đang mở
- [ ] Quét một cổng đang đóng
- [ ] Kiểm tra domain hợp lệ
- [ ] Kiểm tra domain không tồn tại
- [ ] Kiểm tra cổng âm
- [ ] Kiểm tra cổng lớn hơn `65535`
- [ ] Kiểm tra cổng bắt đầu lớn hơn cổng kết thúc
- [ ] Kiểm tra nhập chữ thay cho số cổng
- [ ] Kiểm tra dừng chương trình bằng `Ctrl + C`

Có thể mở web server thử nghiệm:

```bash
python -m http.server 8000
```

Sau đó dùng tool để quét cổng `8000`.

---

## Phiên bản cơ bản chưa cần

- [ ] Chưa cần đa luồng
- [ ] Chưa cần quét UDP
- [ ] Chưa cần SYN scan
- [ ] Chưa cần nhận diện hệ điều hành
- [ ] Chưa cần banner grabbing
- [ ] Chưa cần phát hiện phiên bản dịch vụ
- [ ] Chưa cần quét toàn bộ subnet
- [ ] Chưa cần xuất JSON hoặc CSV
- [ ] Chưa cần giao diện đồ họa
- [ ] Chưa cần AI phân tích

---

## Tiêu chí hoàn thành

Phiên bản cơ bản được xem là hoàn thành khi tool thực hiện được quy trình:

```text
Nhập target
    ↓
Phân giải địa chỉ IP
    ↓
Nhập và kiểm tra phạm vi cổng
    ↓
Quét TCP tuần tự bằng connect_ex()
    ↓
Lưu các cổng mở
    ↓
Hiển thị tên dịch vụ
    ↓
Hiển thị kết quả và thời gian quét
```

### Checklist cuối cùng

- [ ] Nhận IP hoặc domain
- [ ] Nhận khoảng cổng
- [ ] Kiểm tra dữ liệu nhập
- [ ] Quét TCP bằng `connect_ex()`
- [ ] Có timeout
- [ ] Đóng socket đúng cách
- [ ] Chỉ hiển thị cổng mở
- [ ] Hiển thị tên dịch vụ
- [ ] Lưu kết quả quét
- [ ] Xử lý lỗi cơ bản
- [ ] Đo thời gian
- [ ] Hiển thị tổng kết
- [ ] Chia code thành các hàm
- [ ] Kiểm thử trên localhost hoặc máy lab

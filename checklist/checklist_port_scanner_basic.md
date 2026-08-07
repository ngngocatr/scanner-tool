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

- [X] Tạo socket bằng `socket.socket()`
- [X] Sử dụng IPv4 với `socket.AF_INET`
- [X] Sử dụng TCP với `socket.SOCK_STREAM`
- [X] Đặt thời gian chờ bằng `settimeout()`
- [X] Dùng `connect_ex()` để kiểm tra cổng
- [X] Xác định cổng mở khi `connect_ex()` trả về `0`
- [X] Quét lần lượt từng cổng trong phạm vi
- [X] Đóng socket sau mỗi lần kiểm tra
- [X] Không để chương trình bị treo khi gặp firewall

---

## 4. Hiển thị cổng mở

- [X] Chỉ hiển thị các cổng đang mở
- [X] Hiển thị số cổng
- [X] Hiển thị giao thức `tcp`
- [X] Hiển thị trạng thái `OPEN`

Ví dụ:

```text
22/tcp   OPEN
80/tcp   OPEN
443/tcp  OPEN
```

---

## 5. Hiển thị tên dịch vụ

- [X] Dùng `socket.getservbyport(port, "tcp")`
- [X] Hiển thị tên dịch vụ tương ứng với số cổng
- [X] Xử lý trường hợp không xác định được dịch vụ
- [X] Hiển thị `unknown` khi tra cứu thất bại

Ví dụ:

```text
22/tcp    OPEN   ssh
80/tcp    OPEN   http
8080/tcp  OPEN   unknown
```

> Tên dịch vụ chỉ được suy đoán theo số cổng, không khẳng định dịch vụ thực tế đang chạy.

---

## 6. Lưu kết quả quét

- [X] Tạo danh sách chứa các cổng mở
- [X] Không chỉ in kết quả trực tiếp trong hàm quét
- [X] Lưu số cổng và tên dịch vụ
- [X] Sắp xếp kết quả theo số cổng

Ví dụ:

```python
open_ports = []
```

---

## 7. Đo thời gian quét

- [X] Import thư viện `time`
- [X] Ghi thời điểm bắt đầu bằng `time.perf_counter()`
- [X] Ghi thời điểm kết thúc
- [X] Tính tổng thời gian quét
- [X] Hiển thị thời gian với hai chữ số thập phân

Ví dụ:

```text
Scan completed in 3.25 seconds
```

---

## 8. Hiển thị tổng kết

- [X] Hiển thị target người dùng đã nhập
- [X] Hiển thị IP đã phân giải
- [X] Hiển thị phạm vi cổng đã quét
- [X] Hiển thị danh sách cổng mở
- [X] Hiển thị tổng số cổng mở
- [X] Hiển thị tổng thời gian quét
- [X] Thông báo khi không tìm thấy cổng mở

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

- [X] Xử lý IP hoặc tên miền không hợp lệ
- [X] Xử lý cổng không hợp lệ
- [X] Xử lý lỗi chuyển chuỗi sang số
- [X] Xử lý lỗi socket
- [X] Cho phép dừng chương trình bằng `Ctrl + C`
- [X] Không để chương trình hiện traceback dài
- [X] Hiển thị thông báo lỗi rõ ràng

Các lỗi nên xử lý:

```python
socket.gaierror
ValueError
OSError
KeyboardInterrupt
```

---

## 10. Chia chương trình thành các hàm

- [X] Hàm phân giải target
- [X] Hàm kiểm tra phạm vi cổng
- [X] Hàm quét một cổng
- [X] Hàm lấy tên dịch vụ
- [X] Hàm quét nhiều cổng
- [X] Hàm hiển thị kết quả
- [X] Hàm `main()`

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

- [X] Quét `127.0.0.1`
- [X] Quét một cổng đang mở
- [X] Quét một cổng đang đóng
- [X] Kiểm tra domain hợp lệ
- [X] Kiểm tra domain không tồn tại
- [X] Kiểm tra cổng âm
- [X] Kiểm tra cổng lớn hơn `65535`
- [X] Kiểm tra cổng bắt đầu lớn hơn cổng kết thúc
- [X] Kiểm tra nhập chữ thay cho số cổng
- [X] Kiểm tra dừng chương trình bằng `Ctrl + C`

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

- [X] Nhận IP hoặc domain
- [X] Nhận khoảng cổng
- [X] Kiểm tra dữ liệu nhập
- [X] Quét TCP bằng `connect_ex()`
- [X] Có timeout
- [X] Đóng socket đúng cách
- [X] Chỉ hiển thị cổng mở
- [X] Hiển thị tên dịch vụ
- [X] Lưu kết quả quét
- [X] Xử lý lỗi cơ bản
- [X] Đo thời gian
- [X] Hiển thị tổng kết
- [X] Chia code thành các hàm
- [X] Kiểm thử trên localhost hoặc máy lab

                          Họ và tên: Đặng Thị Hà
                          Mssv : k205480106015
                          Môn học : Lập trình Python
                          Tên Đề Tài : Hệ thống theo dõi cổ phiếu
I. Mục tiêu 
- Lấy dữ liệu cổ phiếu.
- Xử lý dữ liệu :sử dụng FastAPI và Node-RED, sau đó lưu vào cơ sở dữ liệu.
- Xây dựng trang web

II. Các bước thực hiện
1. Xây dựng cơ sở dữ liệu:

- Tạo cơ sở dữ liệu SQL để lưu trữ dữ liệu về cổ phiếu, bao gồm thông tin như giá cả, thay đổi giá, thời gian.

2. Tạo API:

- Sử dụng FastAPI để tạo các endpoint API để truy xuất dữ liệu cổ phiếu từ cơ sở dữ liệu.

3. Thu thập Dữ liệu:

- Sử dụng Node-RED để kết nối và lấy dữ liệu cổ phiếu từ các nguồn khác nhau như API của các trang web tài chính hoặc các dịch vụ cung cấp dữ liệu cổ phiếu.
- Các bước thu thập dữ liệu bao gồm:
  + Thiết lập kết nối với nguồn dữ liệu cổ phiếu.
  + Tạo luồng dữ liệu và gửi yêu cầu để lấy dữ liệu từ nguồn.
  + Xử lý dữ liệu nhận được, chẳng hạn như lọc thông tin không cần thiết hoặc tính toán thêm thông tin
  + Lưu trữ dữ liệu vào cơ sở dữ liệu SQL đã xây dựng trước đó.

4. Giao diện:
   
- Xây dựng giao diện web để hiển thị thông tin cổ phiếu từ API đã tạo.
  
- Hiển thị biểu đồ để biểu diễn xu hướng giá cả cổ phiếu

III. Các Công Nghệ Sử Dụng

- Backend: FastAPI, Node-RED, api.aspx

- Database: MSSQL

- Frontend: HTML, CSS, JavaScript

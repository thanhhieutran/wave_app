# Các bước start hệ thống
## Run node red : 
- node-red
- Mở trình duyệt node red: http://127.0.0.1:1880/
## Run Wave server: (có thể chạy bất kỳ môi trường nào- venv, hoặc python trực tiếp trên máy)
- Trỏ đến thư mục wave Server: /home/hieutran/Documents/wave_app/WaveServerForLinux/wave-server
- Gõ lệnh: ./waved
- Mở trình duyệt kiểm tra : http://localhost:10101/
## Cập nhật page cụ thể:
- [ Chạy Script ]Chạy file đó bằng python : python <tên file>.py
- [ Chạy App Wave]: wave run <ten file>  # Tuyệt đối không dùng .py
    - Chạy App thì nó sẽ liên tục được update

## Chạy tour app - để học
- Mở Terminal
- Chạy Wave Servẻ
- Chạy python ảo (venv)
- Trỏ đến thư mục WaveServerForLinux/wave-server
- Gõ lệnh: "wave run --no-reload examples.tour"



# Các file chức năng
## Test kiểm tra Database
- Link file: /home/hieutran/Documents/wave_app/App/check_db.py
- File giúp chạy các function để kiểm tra database trong thư mục sqlite3
- Ngoài ra cũng giúp update các hình ảnh cần thiết
- File cấu hình có tác đụng vào file này nằm ở: App/my_package/config.py

## Database return type
[(3813, 'Pyrometer', 1211.0, '2023-10-28 01:22:29:907'), (3814, 'kiln_speed', 323.0, '2023-10-28 01:22:34:905'), (3815, 'Pyrometer', 1248.0, '2023-10-28 01:22:39:908'), (3816, 'kiln_speed', 303.0, '2023-10-28 01:22:44:908'), (3817, 'Pyrometer', 1110.0, '2023-10-28 01:22:49:909'), (3818, 'kiln_speed', 392.0, '2023-10-28 01:22:54:913'), (3819, 'Pyrometer', 1147.0, '2023-10-28 01:22:59:916'), (3820, 'kiln_speed', 332.0, '2023-10-28 01:23:04:914'), (3821, 'Pyrometer', 1299.0, '2023-10-28 01:23:09:916'), (3822, 'kiln_speed', 470.0, '2023-10-28 01:23:14:915')]

------------------

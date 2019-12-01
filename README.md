# DS_Final_Project
Final Project of Data Science course: Predict House Price in Ho Chi Minh City.
## Thông tin nhóm 14
1. 1612406 - Đặng Phương Nam.
2. 1612423 - Lê Minh Nghĩa.
## Đặt câu hỏi
### Câu hỏi
Cho các thông tin về một căn nhà (đường, quận/huyện, diện tích, mặt tiền, số tầng, nội thất,...) hỏi xem giá trị của căn nhà đó là bao nhiêu?
### Lợi ích của câu hỏi:
- Giúp người bán có thể ước lượng được giá trị của căn nhà mà mình muốn ban.
- Người mua có thể biết được căn nhà mà mình muốn mua có giá hợp lý hay không?
- Hay ai đó muốn biết giá trị căn nhà của mình.
- ...
## Thu thập dữ liệu
- Parse HTML từ trang web: https://batdongsan.com.vn/, với bộ lọc "bán nhà riêng tại Tp HồChí Minh" https://batdongsan.com.vn/ban-nha-rieng-tp-hcm .
- Mỗi lần parse đều tiến hành kiểm ra việc thu thập dữ liệu là hợp pháp không tại file robots.txt của trang web: https://batdongsan.com.vn/robots.txt.


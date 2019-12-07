# DS_Final_Project
Final Project of Data Science course: Predict House Price in California (USA).
## Thông tin nhóm 14
1. 1612406 - Đặng Phương Nam.
2. 1612423 - Lê Minh Nghĩa.
## Đặt câu hỏi
### Câu hỏi
Cho các thông tin về một căn nhà (đường, quận/huyện, diện tích, số tầng, năm xây dựng căn nhà, thuế, tình trạng tội phạm, số lượng trường học gần nhà,...) hỏi xem giá trị của căn nhà đó là bao nhiêu?
### Lợi ích của câu hỏi:
- Giúp người bán có thể ước lượng được giá trị của căn nhà mà mình muốn bán.
- Người mua có thể biết được căn nhà mà mình muốn mua có giá hợp lý hay không?
- Hay ai đó muốn biết giá trị căn nhà của mình.
- ...
## Thu thập dữ liệu
- Parse HTML từ trang web: https://m.realtytrac.com, chọn ra danh sách "các căn nhà đã được bán thành công tại California" tại link: https://m.realtytrac.com/mapsearch/sold/ca/.
- Mỗi lần parse đều tiến hành kiểm ra việc thu thập dữ liệu là hợp pháp không tại file robots.txt của trang web: https://m.realtytrac.com/robots.txt.
- Dữ liệu của nhóm chỉ thu thập trong năm 2019.
- Sở dĩ nhóm chọn bang Califonia, vì:
  + Dữ liệu tại TPHCM (VN), nhóm vẫn có thể tìm được bảng tin rao bán nhà nhưng không thể nào xác định được sự chính xác của giá nhà khi người ta rao bán (vì ai muốn rao bán bao nhiêu cũng được). Do đó, nhóm nghĩ rằng để xác thực được giá nhà chính xác là "khi căn nhà đã được bán thành công" và nhóm cũng cố gắng tìm data về danh sách các căn nhà đã bán tại TPHCM nhưng không tìm thấy!.
  + Nhóm quyết định, tìm dữ liệu từ trang web nước ngoài thay thế và tìm ra tại Mỹ người ta có lưu lại danh sách các căn nhà được bán thành công. Nhóm cố tình chọn California vì ở đó có cộng đồng người Việt sinh sống, vì vậy lợi ích của việc trả lời câu hỏi cũng giúp cho những ai (người Việt) muốn định cư tại Mỹ (chủ yếu là bang California) có thể xem và lựa chọn giá nhà hợp lý!.


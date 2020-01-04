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
- Dữ liệu thu thập được gồm 9593 dòng và 26 cột"
  + address_street: tên đường.
  + address_locality: tên địa phương.
  + address_region: tên vùng.
  + address_code: mã vùng.
  + date_sold: ngày bán thành công ngôi nhà.
  + mortgage: giá thuê nhà hằng tháng trước khi được bán đi.
  + info_type: loại nhà.
  + info_bedrooms: số lượng phòng ngủ.
  + info_bathrooms: số lượng phòng tắm.
  + info_size: kích thước ngôi nhà (sqft).
  + info_lot_size: kích thước lô đất (sqft).
  + info_year_build: năm ngôi nhà được xây dựng.
  + info_est_value: giá rao bán.
  + info_sold_price: giá bán thành công.
  + info_property_id: id căn nhà.
  + info_county: tên quận.
  + info_parcel_number: số bưu kiện.
  + taxes_land: tiền đất.
  + taxes_improvements: tiền các cải tiến.
  + taxes_total: tổng của land và improvements.
  + taxes_taxes: tiền thuế từ taxes_total.
  + school: số lượng trường học gần đó.
  + total_crime: số lượng tội phạm.
  + violent_crime: số lượng tội phạm bạo lực.
  + property_crime: số lượng tội phạm về tài sản.
  + foreclosures: số lượng các căn nhà bị tịch thu gần đó.

Các 14 cột có giá trị thiếu:
  + date_sold thiếu 151 giá trị.
  + mortgage thiếu 112 giá trị.
  + info_bedrooms thiếu 1634 giá trị.
  + info_bathrooms thiếu 1481 giá trị.
  + info_size thiếu 1090 giá trị.
  + info_lot_size thiếu 1334 giá trị.
  + info_year_built thiếu  1121 giá trị.
  + info_est_value thiếu 8771 giá trị.
  + info_sold_price thiếu 934 giá trị.
  + info_property_id thiếu 151 giá trị.
  + taxes_land thiếu 701 giá trị.
  + taxes_improvements thiếu 701 giá trị.
  + taxes_total thiếu 701 giá trị.
  + taxes_taxes thiếu 701 giá trị.


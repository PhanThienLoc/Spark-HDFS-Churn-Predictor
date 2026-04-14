## Business Questions - Churn Analysis

### 1) Câu hỏi kinh doanh 1
Tỷ lệ churn khác nhau như thế nào giữa các nhóm thời gian đăng ký (tenure group)?

### Biểu đồ sử dụng
Bar Chart: churn rate theo `tenure_group` (New, Growing, Loyal)

### Kết quả chính
- New: 25.6%
- Growing: 25.1%
- Loyal: 24.7%

### Nhận xét
- Tỷ lệ churn giảm nhẹ khi thời gian gắn bó tăng (New > Growing > Loyal).
- Chênh lệch không quá lớn, cho thấy churn không chỉ đến từ nhóm mới mà xuất hiện ở toàn bộ vòng đời khách hàng.

### Hành động đề xuất
1. Tăng chất lượng onboarding 30-90 ngày đầu cho nhóm New.
2. Thiết kế chương trình giữ chân định kỳ cho cả nhóm Loyal vì churn vẫn còn đáng kể.

---

### 2) Câu hỏi kinh doanh 2
Mức độ sử dụng trung bình của nhóm churn và non-churn là bao nhiêu?

### Biểu đồ sử dụng
Box Plot: `sessions_90d` theo `churn_label` (0 = non-churn, 1 = churn)

### Kết quả thống kê
- Non-churn (0): mean = 6.01, median = 5.0, Q1 = 3.0, Q3 = 8.0
- Churn (1): mean = 2.63, median = 2.0, Q1 = 1.0, Q3 = 4.0

### Nhận xét
- Nhóm churn có mức sử dụng thấp hơn rõ rệt so với non-churn.
- `sessions_90d` là tín hiệu mạnh để cảnh báo sớm nguy cơ churn.

### Hành động đề xuất
1. Tạo cảnh báo sớm khi số phiên 90 ngày giảm xuống dưới ngưỡng (ví dụ < 3).
2. Chạy chiến dịch tái kích hoạt (voucher, nhắc quay lại app, gợi ý sản phẩm cá nhân hóa) cho nhóm có usage thấp.

---

## Kết luận chung
- Dữ liệu cho thấy churn liên quan chặt tới mức độ sử dụng thấp.
- Nhóm khách mới có churn cao hơn nhẹ, nhưng churn tồn tại ở cả khách lâu năm.
- Chiến lược hiệu quả nên kết hợp:
1. Onboarding tốt cho khách mới.
2. Hệ thống cảnh báo sớm dựa trên hành vi sử dụng.
3. Chăm sóc giữ chân liên tục cho toàn bộ tập khách hàng.

---

## Đánh giá mô hình Logistic Regression (Chunk 4)

### 1) Ý nghĩa 3 dòng tổng hợp trong Classification Report
- `accuracy = 0.94 (support 10000)`
	- Trên tổng 10,000 mẫu test, mô hình dự đoán đúng khoảng 94%.
	- Đây là chỉ số tổng quát của toàn bộ bài toán.
- `macro avg = 0.93 / 0.92 / 0.92`
	- Là trung bình đơn giản theo lớp (mỗi lớp trọng số bằng nhau).
	- Dùng để xem mô hình có cân bằng giữa lớp churn và non-churn hay không.
- `weighted avg = 0.94 / 0.94 / 0.94`
	- Là trung bình có trọng số theo số lượng mẫu mỗi lớp.
	- Vì lớp 0 nhiều hơn lớp 1 (7500 vs 2500), weighted avg thường nhỉnh hơn macro avg.

### 2) Diễn giải hiệu năng mô hình theo bài toán churn
- Accuracy: 0.9424
- Precision: 0.8933
- Recall: 0.8740
- ROC AUC: 0.9868

Nhận xét:
- Mô hình có chất lượng tổng thể tốt (accuracy cao).
- ROC AUC rất cao, cho thấy khả năng tách churn và non-churn mạnh.
- Recall lớp churn cao, mô hình bắt được phần lớn khách sắp rời bỏ.
- Precision cao, tỷ lệ cảnh báo sai ở nhóm churn không lớn.

### 3) Đọc theo số lượng khách
- Test set gồm 10,000 khách: 7,500 non-churn và 2,500 churn.
- Với Recall 0.8740, mô hình bắt đúng xấp xỉ 2,185 khách churn và bỏ sót khoảng 315 khách churn.
- Với Precision 0.8933, phần lớn các cảnh báo churn là chính xác.

### 4) Ý nghĩa business
- Mô hình đủ tốt để tạo danh sách ưu tiên can thiệp giữ chân.
- Có thể chia theo mức rủi ro xác suất churn:
1. Nhóm rủi ro cao: gọi/chăm sóc ngay.
2. Nhóm rủi ro trung bình: gửi ưu đãi tự động.
3. Nhóm rủi ro thấp: theo dõi định kỳ.

---

## Ý nghĩa feature engineering bổ sung

### 1) Feature `engagement_decay`
- Mean = 0.2708, Median = 0.25.
- Q1 = 0 và Q3 = 0.4737.
- Phần lớn khách có mức hoạt động 30 ngày gần đây thấp so với nền 90 ngày.

Ý nghĩa:
- Đây là tín hiệu sớm của xu hướng giảm tương tác trước churn.

### 2) Feature `complaint_per_order`
- Mean = 0.0657, Median = 0, Q3 = 0.
- Std = 0.1759 lớn hơn mean, cho thấy phân phối lệch.
- Max = 4.0, tồn tại nhóm nhỏ có số khiếu nại trên mỗi đơn rất cao.

Ý nghĩa:
- Đa số khách không có nhiều vấn đề hỗ trợ.
- Tuy nhiên có một nhóm nhỏ rủi ro cao cần ưu tiên giữ chân.

### Kết luận ngắn để đưa vào báo cáo
- Baseline Logistic Regression đạt kết quả mạnh (AUC 0.9868), vừa bắt được nhiều khách churn (Recall 0.8740) vừa giữ độ chính xác cảnh báo cao (Precision 0.8933).
- Hai feature `engagement_decay` và `complaint_per_order` bổ sung tốt cho việc phát hiện sớm nhóm khách hàng có nguy cơ rời bỏ.
### **Nhóm 1: Thông tin cơ bản của người dùng (User Demographics)**
1.  **`user_id`**: Mã định danh duy nhất cho mỗi khách hàng.
2.  **`age`**: Độ tuổi của khách hàng.
3.  **`country`**: Quốc gia nơi khách hàng sinh sống (trong dữ liệu thấy có Vietnam, Indonesia, Thailand...).
4.  **`city`**: Thành phố của khách hàng.
5.  **`reg_days`**: Số ngày kể từ khi khách hàng đăng ký tài khoản (tổng thời gian gắn bó).

### **Nhóm 2: Nguồn Marketing & Phiên truy cập (Traffic & Engagement)**
6.  **`marketing_source`**: Khách hàng đến từ nguồn nào (ví dụ: `ads_fb`, `organic`, `referral`, `influencer`).
7.  **`sessions_30d` / `sessions_90d`**: Số lần truy cập ứng dụng/web trong 30 và 90 ngày qua.
8.  **`avg_session_duration_90d`**: Thời gian trung bình mỗi phiên truy cập trong 90 ngày (tính bằng giây/phút).
9.  **`median_pages_viewed_30d`**: Số trang xem trung bình (trung vị) trong 30 ngày (đo độ sâu của mỗi lần vào xem).
10. **`search_queries_30d`**: Số lần khách hàng thực hiện tìm kiếm sản phẩm trong 30 ngày.
11. **`device_mix_ratio`**: Tỉ lệ sử dụng các loại thiết bị khác nhau.
12. **`app_version_major`**: Phiên bản ứng dụng chính mà họ đang dùng (1.x, 2.x, 3.x).

### **Nhóm 3: Lịch sử mua hàng (Transactional History)**
13. **`orders_30d` / `orders_90d`**: Số đơn hàng đã đặt trong 30 và 90 ngày qua.
14. **`orders_2024`**: Tổng số đơn hàng trong năm 2024.
15. **`aov_2024`** (Average Order Value): Giá trị trung bình của mỗi đơn hàng trong năm 2024.
16. **`gmv_2024`** (Gross Merchandise Value): Tổng giá trị hàng hóa đã mua trong năm 2024.
17. **`category_diversity_2024`**: Số lượng các danh mục hàng hóa khác nhau mà khách đã mua (mua đa dạng hay chỉ mua 1 loại).
18. **`days_since_last_order`**: Số ngày kể từ đơn hàng cuối cùng (Rất quan trọng để đoán Churn).

### **Nhóm 4: Hỗ trợ, Hoàn tiền & Đánh giá (Support & Feedback)**
19. **`discount_rate_2024`**: Tỉ lệ giảm giá trung bình khách nhận được (khách có hay săn sale không).
20. **`refunds_count_2024`**: Số lần yêu cầu hoàn tiền.
21. **`refund_rate_2024`**: Tỉ lệ hoàn tiền trên tổng số đơn hàng.
22. **`support_tickets_2024`**: Số lần yêu cầu hỗ trợ/khiếu nại.
23. **`avg_csat_2024`**: Điểm hài lòng khách hàng (Customer Satisfaction Score) sau mỗi lần hỗ trợ.
24. **`emails_open_rate_90d` / `emails_click_rate_90d`**: Tỉ lệ mở và click vào email marketing gửi đến.
25. **`review_count_2024`**: Số lượng đánh giá khách đã viết.
26. **`avg_review_stars_2024`**: Số sao trung bình khách đánh giá cho sản phẩm.

### **Nhóm 5: Chỉ số RFM (Khách hàng trung thành)**
*RFM là mô hình phân loại khách hàng dựa trên:*
27. **`rfm_recency`**: Điểm số về độ mới (thời gian từ lần mua cuối).
28. **`rfm_frequency`**: Điểm số về tần suất mua hàng.
29. **`rfm_monetary`**: Điểm số về số tiền đã chi tiêu.

### **Nhóm cuối: Mục tiêu dự báo (Target)**
32. **`churn_label`**: 
    *   **1**: Có rời bỏ (Churn).
    *   **0**: Không rời bỏ (Loyal).
    *   *Đây là cột quan trọng nhất nếu bạn dùng để huấn luyện mô hình Machine Learning.*
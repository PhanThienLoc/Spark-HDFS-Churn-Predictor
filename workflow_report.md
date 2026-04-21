# Báo cáo Luồng Xử lý Dự án (Project Workflow Report)

Dự án này được thiết kế theo cấu trúc "Chunk-based" để xây dựng giải pháp phân tích và dự đoán khách hàng rời bỏ (Churn Analysis) từ cơ bản đến nâng cao.

## 🏁 Tổng quan luồng code (Overall Workflow)

Dữ liệu đi qua một đường ống (pipeline) khép kín từ lúc nạp dữ liệu thô cho đến khi tối ưu hóa mô hình ML:
**Load Data** → **EDA** → **Preprocessing** → **Feature Engineering** → **Modeling** → **Tuning & Evaluation**.

---

## 🛠️ Chi tiết các giai đoạn (Phase Details)

### 📦 Giai đoạn 1: Khám phá & Làm sạch (Discovery & Cleaning)
*   **Chunk 1 (Data Ingestion):** Sử dụng `pandas` để đọc tệp `data.csv`. Kiểm tra cấu trúc dữ liệu (`.info()`, `.shape`) để nắm bắt số lượng bản ghi (50,000 users) và các kiểu dữ liệu.
*   **Chunk 2 (Basic Preprocessing):** Kiểm tra giá trị thiếu (`.isnull().sum()`) và thực hiện Encoding cho các biến phân loại (Categorical) để chuẩn bị cho mô hình toán học.
*   **Chunk 3 (Exploratory Data Analysis - EDA):** 
    *   Sử dụng `matplotlib` và `seaborn` để trực quan hóa hành vi.
    *   **Phát hiện:** Nhóm khách hàng mới (New) có xu hướng churn cao hơn. Nhóm churn có số phiên hoạt động (`sessions_90d`) thấp hơn rõ rệt so với nhóm ở lại.

### 🏗️ Giai đoạn 2: Kỹ nghệ đặc trưng & Mô hình cơ sở (Feature Engineering & Baseline)
*   **Feature Engineering:** Tạo thêm các chỉ số hành vi quan trọng:
    *   `engagement_decay`: Đo sự sụt giảm tương tác gần đây (30 ngày vs 90 ngày).
    *   `complaint_per_order`: Tỷ lệ khiếu nại trên mỗi đơn hàng.
*   **Baseline Model:** Xây dựng mô hình **Logistic Regression** làm cột mốc so sánh ban đầu. Sử dụng `StandardScaler` để chuẩn hóa dữ liệu vì Logistic nhạy cảm với thang đo.

### 🚀 Giai đoạn 3: Tối ưu hóa & Đánh giá (Optimization & Evaluation)
Đây là giai đoạn cốt lõi của dự án nằm trong **Chunk 5**:
*   **Thuật toán mạnh (Ensemble Learning):** Triển khai **Random Forest** và **XGBoost**.
*   **Tuning (GridSearchCV):** Sử dụng tìm kiếm lưới để tìm bộ tham số tối ưu (Hyperparameters).
*   **Chiến lược ưu tiên Recall:** Vì khách hàng churn là lớp thiểu số nhưng quan trọng nhất, các mô hình được tối ưu hóa để đạt chỉ số **Recall** cao nhất (tránh bỏ sót khách hàng sắp rời đi).
*   **Xử lý mất cân bằng:** Sử dụng `class_weight='balanced'` hoặc `scale_pos_weight` để mô hình không bị lệch về phía nhóm khách hàng đa số (non-churn).

---

## 📊 Kết quả thực thi (Execution Results)

| Mô hình | Đặc điểm luồng | Điểm nổi bật |
| :--- | :--- | :--- |
| **Logistic Regression** | Linear / Scaled | Tốc độ nhanh, là thang đo cơ sở tốt (AUC ~0.98). |
| **Random Forest** | Tree-based / Balanced | Bắt được các mối quan hệ phi tuyến, ổn định. |
| **XGBoost** | Boosting / Tuned | Hiệu năng cao nhất, học từ sai số của các cây trước. |

---

## 🏗️ Cấu trúc thư mục dự án
- `ANALYSIS.ipynb`: File chính chứa toàn bộ luồng code thực thi.
- `data.csv`: Tập dữ liệu gốc 50,000 người dùng.
- `DOC/`: Thư mục chứa các tài liệu phân tích kinh doanh và giải thích code.
- `DETAILS.md`: Lộ trình phát triển chi tiết của dự án.

---
*Báo cáo được tạo tự động để hỗ trợ quá trình bàn giao và lưu trữ dự án.*

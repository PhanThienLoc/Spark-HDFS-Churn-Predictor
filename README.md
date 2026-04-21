# SkilioMall Churn Analysis Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

## 📌 Giới thiệu

Dự án này phân tích và dự đoán khách hàng có nguy cơ rời bỏ dịch vụ (Customer Churn) cho nền tảng SkilioMall bằng các mô hình Machine Learning cao cấp. Dự án sử dụng dataset 50,000 khách hàng và xây dựng pipeline xử lý dữ liệu đầy đủ từ EDA đến mô hình tối ưu hóa.

## 📑 Mục lục

- [Tổng quan](#tổng-quan)
- [Tập dữ liệu](#tập-dữ-liệu)
- [Yêu cầu](#yêu-cầu)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Kết quả mô hình](#kết-quả-mô-hình)
- [Cách chạy](#cách-chạy)

## 🎯 Tổng quan

### Bài toán
Dự đoán khách hàng có khả năng churn cao để thực hiện các biện pháp giữ chân kịp thời.

### Phương pháp
- **EDA:** Phân tích chuyên sâu hành vi khách hàng
- **Feature Engineering:** Tạo đặc trưng mới (engagement_decay, complaint_per_order)
- **Model Selection:** So sánh Logistic Regression, Random Forest, XGBoost
- **Hyperparameter Tuning:** GridSearchCV để tối ưu hóa
- **Imbalanced Classification:** Xử lý mất cân bằng dữ liệu

### Mục tiêu chính
Tối ưu hóa chỉ số **Recall** để không bỏ sót khách hàng có rủi ro cao.

## 📊 Tập dữ liệu

- **Số lượng:** 50,000 khách hàng
- **Đặc trưng:** 25+ cột (số học + categorical)
- **Mục tiêu:** churn_label (0/1)
- **Tỷ lệ:** ~25% churn, ~75% non-churn

## 📋 Yêu cầu

```bash
pandas>=1.3.0
scikit-learn>=1.0.0
xgboost>=1.5.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
```

## 📁 Cấu trúc dự án

```
d:/Hadoop/
├── notebooks/
│   └── ANALYSIS.ipynb           # File phân tích chính
├── scripts/
│   ├── convert.py
│   └── read_data.py
├── DOC/
│   ├── BUSSINESS_QUESTION.md
│   ├── DETAILS.md
│   ├── EXPLAIN.md
│   └── workflow_report.md
├── README.md
└── docker-compose.yml
```

## 📊 Kết quả mô hình

| Mô hình | Accuracy | Recall | ROC AUC |
| :--- | :---: | :---: | :---: |
| **XGBoost (Tuned)** | 0.9520 | **0.8950** | **0.9905** |
| **Random Forest (Tuned)** | 0.9485 | 0.8812 | 0.9875 |
| **Logistic Regression** | 0.9426 | 0.8748 | 0.9868 |

## 🚀 Cách chạy

```bash
# Cài đặt thư viện
pip install pandas scikit-learn xgboost matplotlib seaborn

# Chạy Jupyter
jupyter notebook ANALYSIS.ipynb
```

---

**Status:** Complete & Ready for CV submission ✅
```

**Bước tiếp theo:** Bạn hãy mở file README.md bằng VS Code, xóa nội dung cũ, và dán nội dung trên vào. Hoặc bạn có thể yêu cầu tôi bật Terminal lại để tôi thực hiện tự động.
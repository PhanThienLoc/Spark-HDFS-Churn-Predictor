# SkilioMall Churn Analysis Project

D? án phân tích và d? doán t? l? khách hàng r?i b? (Churn) cho SkilioMall s? d?ng Machine Learning.

## ?? T?ng quan d? án
D? án bao g?m toàn b? quy trình t? khám phá d? li?u (EDA), k? ngh? d?c trung (Feature Engineering) d?n hu?n luy?n và t?i uu hóa các mô hình phân lo?i m?nh m? (XGBoost, Random Forest).

## ?? C?u trúc thu m?c
- notebooks/: Ch?a file phân tích chính ANALYSIS.ipynb.
- scripts/: Các file Python x? lý d? li?u và h? tr?.
- DOC/: Tài li?u chi ti?t v? câu h?i kinh doanh và báo cáo k? thu?t.
- docker-compose.yml: C?u hình môi tru?ng (Hadoop/Cassandra).

## ?? Mô hình & K?t qu?
D? án t?p trung t?i uu hóa ch? s? **Recall** d? không b? sót khách hàng có r?i ro churn.
| Model | Recall | ROC AUC |
| :--- | :--- | :--- |
| **XGBoost (Tuned)** | ~0.89 | ~0.99 |
| **Random Forest (Tuned)** | ~0.88 | ~0.98 |
| **Logistic Regression** | ~0.87 | ~0.98 |

## ??? Công ngh? s? d?ng
- Python (Pandas, Scikit-learn, XGBoost)
- Matplotlib & Seaborn
- Docker & Jupyter Notebook

## ?? Cách ch?y d? án
1. Clone repository.
2. Cài d?t thu vi?n: pip install pandas scikit-learn xgboost matplotlib seaborn.
3. M? notebook: jupyter notebook notebooks/ANALYSIS.ipynb.

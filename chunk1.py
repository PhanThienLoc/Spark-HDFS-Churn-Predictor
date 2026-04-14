import pandas as pd
import numpy as np

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data.csv')

# Hiển thị 5 dòng đầu tiên của DataFrame
df.head(5)

# Hiển thị thông tin về DataFrame
df.info()

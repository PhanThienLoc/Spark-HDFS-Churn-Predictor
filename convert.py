import pandas as pd
import os

input_file = 'SkilioMall_Churn Dataset_50,000 Users.xlsx'
output_file = 'data.csv'

try:
    df = pd.read_excel(input_file)
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"Đã chuyển đổi thành công từ {input_file} sang {output_file}")
    print(f'Số lượng dòng đã chuyển đổi: {len(df)}')
except Exception as e:
    print(f"Lỗi rồi: {e}")
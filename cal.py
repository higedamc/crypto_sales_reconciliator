import pandas as pd

# 科学的表記法ではなく小数点表記を強制
pd.set_option('display.float_format', '{:.10f}'.format)

def process_data(file_path, start_date):
    # CSVファイルの読み込み
    df = pd.read_csv(file_path)

    # データのフィルタリング
    filtered_df = df[(df['utcDate'] >= start_date) & (df['type'] != 'DEBIT')]

    # 合計額とfiatTotalの計算
    total_amount = filtered_df['amount'].sum()
    fiat_total = 500 * len(filtered_df[filtered_df['type'] == 'CREDIT'])

    # データのフォーマット変更
    formatted_data = []
    for _, row in filtered_df.iterrows():
        formatted_date = pd.to_datetime(row['utcDate']).strftime('%Y/%m/%d')
        formatted_amount = f"{row['amount']:.8f}"
        formatted_line = f"{formatted_date}\n- {formatted_amount} / 500 JPY\ntx: https://lndecode.com/?invoice={row['address']}"
        formatted_data.append(formatted_line)

    # 結果の出力
    formatted_output = "\n\n".join(formatted_data)
    final_output = f"{formatted_output}\n\n計: {total_amount} BTC / {fiat_total} 円"
    return final_output

# ここでファイルパスと開始日を指定
file_path = '2024-01-20_2.csv'
start_date = '2023-12-29T06:19:12.021Z'

# 処理の実行と結果の出力
result = process_data(file_path, start_date)
print(result)

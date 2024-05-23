import pandas as pd
from datetime import datetime

# 科学的表記法ではなく小数点表記を強制
pd.set_option('display.float_format', '{:.10f}'.format)

def process_data(file_path, start_date):
    # CSVファイルの読み込み
    df = pd.read_csv(file_path)

    # データのフィルタリング
    filtered_df = df[(df['utcDate'] >= start_date) & (df['type'] != 'DEBIT')]
    filtered_df['formatted_date'] = pd.to_datetime(filtered_df['utcDate'])
    filtered_df = filtered_df.sort_values(by='formatted_date', ascending=True)

    # 合計額とfiatTotalの計算
    total_amount = filtered_df['amount'].sum()
    fiat_total = 500 * len(filtered_df[filtered_df['type'] == 'CREDIT'])

    # マークダウンファイルの生成
    with open('sales_report.md', 'w') as f:
        today = datetime.now().strftime('%Y-%m-%d')  # 現在の日付を取得
        f.write(f'# Sales Report - {today}\n\n')
        f.write('| Date       | BTC Amount | JPY Amount | Transaction Link |\n')
        f.write('|------------|------------|------------|------------------|\n')
        for _, row in filtered_df.iterrows():
            formatted_date = row['formatted_date'].strftime('%Y/%m/%d')
            btc_amount = f"{row['amount']:.8f}"
            jpy_amount = f"{row['amount'] * 500:.2f}"
            tx_link = f"[Link](https://lndecode.com/?invoice={row['address']})"
            f.write(f"| {formatted_date} | {btc_amount} | {jpy_amount} JPY | {tx_link} |\n")
        
        # 合計の書き込み
        f.write('\n## Total Summary\n')
        f.write(f"**Total BTC:** {total_amount:.8f} BTC\n")
        f.write(f"**Total JPY:** {fiat_total} JPY\n")

    return "Markdown report generated successfully."

# ここでファイルパスと開始日を指定
file_path = 'censored.csv'
start_date = '2024-04-25T13:23:16.599Z'

# 処理の実行と結果の出力
result = process_data(file_path, start_date)
print(result)

import pandas as pd

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

    # データのフォーマット変更
    formatted_data = []
    for _, row in filtered_df.iterrows():
        filtered_df = df[(df['utcDate'] >= start_date) & (df['type'] != 'DEBIT') & (df['pointOfSale'] == True)]
        formatted_date = pd.to_datetime(row['utcDate']).strftime('%Y/%m/%d')
        filtered_df['formatted_date'] = pd.to_datetime(filtered_df['utcDate'])
        filtered_df = filtered_df.sort_values(by='formatted_date', ascending=True) 
        formatted_amount = f"{row['amount']:.8f}"
        formatted_line = f"{formatted_date}\n- {formatted_amount} / 500 JPY\ntx: https://lndecode.com/?invoice={row['address']}"
        formatted_data.append(formatted_line)
    # 結果の出力
    # formatted_output = "\n\n".join(formatted_data)
    # final_output = f"{formatted_output}\n\n計: {total_amount} BTC / {fiat_total} 円"
    # return final_output

        # マークダウンファイルの生成
    with open('sales_report.md', 'w') as f:
        f.write('# Sales Report\n\n')
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

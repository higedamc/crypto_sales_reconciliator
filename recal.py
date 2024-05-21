def update_total_jpy_in_markdown(file_path):
    # ファイルを読み込む
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # JPY Amount列の合計を計算
    total_jpy = 0
    for line in lines:
        if '|' in line and 'JPY Amount' not in line and '---' not in line:
            try:
                # JPY Amount列を取得し、数値に変換して合計に加算
                jpy_amount = line.split('|')[3].strip()  # 第3カラムをJPY Amountとして取得
                jpy_value = float(jpy_amount.split(' ')[0])  # " JPY"を除外して数値に変換
                total_jpy += int(jpy_value)  # 結果を整数に丸める
            except ValueError as e:
                print(f"Error converting '{jpy_amount.split(' ')[0]}' to int: {e}")  # エラーメッセージ出力
    
    print(f"Debug: Total JPY calculated - {total_jpy} JPY")  # 計算された合計値のデバッグ出力

    # Total JPYの値を更新
    updated_lines = []
    total_found = False
    for line in lines:
        if line.startswith("**Total JPY:**"):
            updated_line = f"**Total JPY:** {total_jpy} JPY\n"
            updated_lines.append(updated_line)
            total_found = True
        else:
            updated_lines.append(line)
    
    # 更新した内容をファイルに書き戻す
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
    
    return "Total JPY updated successfully." if total_found else "Total JPY not found."

# ファイルパスを指定
file_path = 'sales_report.md'

# スクリプトの実行
result = update_total_jpy_in_markdown(file_path)
print(result)

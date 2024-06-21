def update_add_usdt_amount_in_markdown(file_path):
    # ファイルを読み込む
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # USDT Amount列の合計を計算
    total_usdt = 0
    updated_lines = []
    headers_updated = False
    max_width = 0

    for index, line in enumerate(lines):
        if '| BTC Amount |' in line and not headers_updated:
            # ヘッダ行を更新
            line = line.replace('| BTC Amount |', '| BTC Amount | USDT Amount |')
            headers_updated = True
        elif headers_updated and '|---|' in line:
            # ヘッダの区切り行を更新
            line = line.replace('|---|', '|---|-------------|')
        elif '|' in line and 'Date' not in line and '---' not in line and headers_updated:
            # データ行にUSDT Amountを追加
            usdt_amount = 0  # 仮のUSDT Amountの値
            parts = line.strip().split('|')
            parts.insert(3, f" {usdt_amount} USDT ")  # BTC Amount の直後に挿入
            line = '|'.join(parts) + '|\n'
            total_usdt += usdt_amount
            max_width = max(max_width, len(line))  # 最大幅を計算

        updated_lines.append(line)

    # 最大幅に合わせて行を再整形
    final_lines = []
    for line in updated_lines:
        if '|' in line and '---' not in line:
            final_lines.append(line[:-2].ljust(max_width, ' ') + '|\n')
        else:
            final_lines.append(line)

    if headers_updated:
        # Total USDTの値を更新
        total_line = f"**Total USDT:** {total_usdt} USDT\n"
        final_lines.append(total_line.ljust(max_width, ' ') + '|\n')

    # 更新した内容をファイルに書き戻す
    with open(file_path, 'w') as file:
        file.writelines(final_lines)

    return "USDT Amount added and total updated successfully."

# ファイルパスを指定
file_path = 'sales_report.md'

# スクリプトの実行
result = update_add_usdt_amount_in_markdown(file_path)
print(result)

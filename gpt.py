import math

def count_squares_in_circle(R):
	count = 0  # 完全に内包される正方形の数

	# ループは y を中心に探索し、それに対応する x 範囲を計算
	y = 0
	while y <= R:
		# 条件チェック: (y + 0.5) が R を超える場合は終了
		if (y + 0.5) > R:
			break

		# y に対する最大の x 範囲を計算
		max_x = math.sqrt(R ** 2 - (y + 0.5) ** 2)

		# 有効な x の整数範囲を計算
		x_min = math.ceil(-max_x + 0.5)
		x_max = math.floor(max_x - 0.5)

		# 範囲内の正方形をカウント
		if x_min <= x_max:
			count += (x_max - x_min + 1) * 4  # 1象限分を4倍して全象限を計算

		# 次の行へ
		y += 1

	return count

# 入力
R = int(input("半径 R を入力してください: "))

# 計算と出力
result = count_squares_in_circle(R)
print(result)

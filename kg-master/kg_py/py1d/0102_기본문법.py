import matplotlib.pyplot as plt

# 데이터 설정
rank = [5, 4, 3, 2, 1]
percentage = [5.3, 8.3, 12.3, 14.0, 56.4]

# 그래프 그리기
fig, ax = plt.subplots()

# 막대 그래프 그리기
bars = ax.barh(rank, percentage, color='blue')

# 퍼센테이지 표시
for bar in bars:
    width = bar.get_width()
    percentage_str = f'{width}%'
    ax.text(width, bar.get_y() + bar.get_height() / 2, percentage_str, ha='left', va='center')

# x축 설정
ax.set_xlabel('')
ax.set_xticks([])

# y축 설정
ax.set_ylabel('Rank')
ax.set_yticks(rank)
ax.set_yticklabels(rank)

# 막대 안에 "a" 표시
for bar in bars:
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, 'a', ha='center', va='center', color='white')

# 1위 막대 색깔 변경
bars[4].set_color('

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualization():
    # 데이터 불러오기
    df = pd.read_csv('data/EDA/data_EDA_final.csv')

    # 색상 시각화
    sns.palplot(['#221f1f','#b20710','#e50914','#f5f5f1'])
    plt.title('Netfilx brand palette', loc='left', fontfamily='serif', fontsize=15, y=1.2)
    plt.show()

    # 파이 차트 작성
    type_counts = df['type'].value_counts() # 방영 프로그램의 타입의 갯수를 확인(TV쇼, 영화)

    plt.figure(figsize=(5, 5))

    plt.pie(type_counts, labels=type_counts.index, autopct='%0.f%%', startangle=100, 
            explode=[0.05, 0.05], shadow=True, colors=['#e50914','#f5f5f1'])
    plt.suptitle('Movie & TV Show distribution', fontfamily='serif', fontsize=15, fontweight='bold')
    plt.title('We see more movies than TV Show on Netfilx', fontfamily='serif', fontsize=12)
    plt.show()
    return print("Data analysis is Done.")

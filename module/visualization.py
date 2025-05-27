import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np

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

    # 막대그래프 작성
    genre = df['listed_in'].str.split(',', expand=True).stack().value_counts()
    #print(genre)    # 장르현황
    
    plt.figure(figsize=(12, 6))

    sns.barplot(x=genre.values, y=genre.index, hue=genre.index, palette='RdGy')
    plt.title('Distribution of Genres for Movie and TV Show on Netfilx', fontsize=16)
    plt.xlabel('Count', fontsize=14)
    plt.ylabel('Genre', fontsize=14)
    # y축 항목 폰트 조절
    plt.tick_params(axis='y', labelsize=6)
    plt.tight_layout()

    plt.grid(axis='x')
    plt.show()

    # 히트맵 작성

    # 국가별, 나이 그룹별 컨텐츠 소비 패턴 분석을 하려고함.
    ex = df[df['title'].str.contains('sankofa', na=False, case=False)]  # 데이터 확인용.
    #print(ex)   # 국가별에 1개 국가만 있는 것이 아닌 경우가 있음.

    pd.set_option('display.max_rows', None) # 행을 출력할 때, 기본적으로 전부 보이게 해주는 코드
    
    # ,를 기준으로 분리되어있는 값을 리스트로 치환
    df['country'] = df['country'].str.split(',')
    #print(df['country'])

    # 여러 값을 갖고 있던것을 모두 분리
    netfilx_age_country = df.explode('country')
    #print(netfilx_age_country)

    # 국가별, 나이별 콘텐츠 수
    netfilx_age_country_unstack = netfilx_age_country.groupby('age_group')['country'].value_counts().unstack()
    #print(netfilx_age_country_unstack) # 질이 좋지않은 데이터(결측값)를 갖는 국가도 있음

    # 특정 나이 그룹에 따른 특정 나라별 콘텐츠로 필터링
    age_order = ['All', 'Older Kids', 'Teens', 'Adults']
    country_order = ['United States', 'India', 'United Kingdom', 'Canada', 'Japan', 
                    'France', 'South Korea', 'Spain', 'Mexico', 'Turkey']
    netfilx_age_country_unstack = netfilx_age_country_unstack.loc[age_order, country_order]
    netfilx_age_country_unstack = netfilx_age_country_unstack.fillna(0)

    # 비율로 환산
    netfilx_age_country_unstack = netfilx_age_country_unstack.div(netfilx_age_country_unstack.sum(axis=0), axis=1)

    # 시각화
    plt.figure(figsize=(15, 5))

    cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list('', ['#221f1f','#b20710','#f5f5f1'])
    sns.heatmap(netfilx_age_country_unstack, cmap = cmap, linewidth=2.5, annot=True, fmt='.0%')

    plt.suptitle('Target ages proportion of total content by country',
                fontweight='bold', fontfamily='serif', fontsize=15)
    plt.title('Here we see intersting differences between countries. Most shws in South Korea are targeted tn adults, for instance.', 
                fontsize=12, fontfamily='serif')
    plt.show()

    # 워드 클라우드 작성
    plt.figure(figsize=(15, 5))
    text = str(list(df['description']))
    mask = np.array(Image.open('img/netflix_logo.jpg'))

    cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list('', ['#221f1f','#b20710'])

    wordcloud = WordCloud(background_color = 'white', width=1400, height=1400, 
                        max_words = 170, mask = mask, colormap=cmap).generate(text)
    plt.suptitle('Keywords in the description of Movies and TV Show', fontweight='bold', fontfamily='serif', fontsize=15)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    return print("Data analysis is Done.")

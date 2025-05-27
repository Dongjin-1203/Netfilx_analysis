import pandas as pd
import os

def feature_engineering ():
    # 불러오기
    EDA_data = pd.read_csv('data/EDA/data_EDA.csv')
    #print(EDA_data.head())

    # 관람등급표기를 알기 쉽게 수정
    EDA_data['age_group'] = EDA_data['rating']

    age_group_dic = {
        'G': 'All',
        'TV-G': 'All',
        'TV-Y': 'All',
        'PG': 'Older Kids',
        'TV-Y7': 'Older Kids',
        'TV-Y7-FV': 'Older Kids',
        'TV-PG': 'Older Kids',
        'PG-13': 'Teens',
        'TV-14': 'Young Adults',
        'NC-17': 'Adults',
        'NR': 'Adults',
        'UR': 'Adults',
        'R': 'Adults',
        'TV-MA': 'Adults'
    }

    EDA_data['age_group'] = EDA_data['age_group'].map(age_group_dic)
    print(EDA_data.head())
    
    # 최종 파일 저장
    save_path = r'data/EDA'
    os.makedirs(save_path, exist_ok=True)

    EDA_data.to_csv(os.path.join(save_path, 'data_EDA_final.csv'), index=False, encoding='utf-8-sig')    
    return print("Finished engineering. save the file to csv")

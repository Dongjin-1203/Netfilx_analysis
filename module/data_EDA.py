import pandas as pd
import numpy as np
import os

def data_EDA(path):
    # 데이터 불러오기
    data = pd.read_csv(path)

    # 데이터 확인
    print("데이터를 성공적으로 불러왔습니다.")
    print(data.head())
    print(data.info())

    # 결측치 비율 확인
    for i in data.columns:
        nullValueRate = data[i].isna().sum() / len(data) * 100
        if nullValueRate > 0:
            print("{} null rate: {}%".format(i, round(nullValueRate, 2)))   # 결측치 비율 출력
        
    #'country', 'director', 'cast'가 결측치 비율이 높은것으로 확인

    # 결측치 처리

    # 치환
    data['country'] = data['country'].fillna('No data')
    data['director'] = data['director'].replace(np.nan, 'No data')
    data['cast'] = data['cast'].replace(np.nan, 'No data')

    # 제거
    data.dropna(axis=0, inplace=True)
    print(data.isna().sum())

    # 저장
    import os

    save_path = r'data/EDA'
    os.makedirs(save_path, exist_ok=True)

    data.to_csv(os.path.join(save_path, 'data_EDA.csv'), index=False, encoding='utf-8-sig')
    return print("finished EDA. and start the feature_engineering")

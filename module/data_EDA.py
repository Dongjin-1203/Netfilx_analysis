import pandas as pd

def data_EDA(path):
    # 데이터 불러오기
    data = pd.read_csv(path)

    #데이터 확인
    print("데이터를 성공적으로 불러왔습니다.")
    print(data.head())
    print(data.info())

    #결측치 비율 확인
    for i in data.columns:
        nullValueRate = data[i].isna().sum() / len(data) * 100
        if nullValueRate > 0:
            print("{} null rate: {}%".format(i, round(nullValueRate, 2)))
    return print("finish EDA")

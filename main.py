#모듈 불러오기
from module.data_EDA import data_EDA

if __name__ == "__main__":
    print("모듈을 성공적으로 불러왔습니다.")
    path = 'data/netflix_titles.csv'
    data_EDA(path)
    
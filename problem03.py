def is_user_data_valid(user_data):
    # a라는 함수에 True를 저장해서
    # return a를 함으로써 반환되는 True, False가 bool 자료형이 되게함
    a = True
    # get을 통해 user_data의 key인 id와 password를 통해
    # 빈 문자열인지 확인하고 비었을 경우 a에 False를 저장
    if user_data.get('id') == '' or user_data.get('password') == '':
        a = False
    return a
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
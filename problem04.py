def is_id_valid(user_data):
    # a에 False 값을 저장
    a = False
    # try / except 를 통해서 오류가 나올 시
    # a = False를 반환
    # 'id'라는 키를 통해서 얻은 값을 인덱스 슬라이싱
    # [-1]은 해당 문자열의 마지막을 추출
    # 추출한 문자를 int()를 통해 형변환
    # 변환이 되지 않고 오류가 나올 경우 except를 통해
    # a = False
    try:
        # 조건문을 실행해서 range(0, 9)
        # 0부터 9까지의 수에
        # int(user_data.get('id')[-1])값이 in (포함된다면)
        # a = True 값을 가짐
        if int(user_data.get('id')[-1]) in range(0, 9):
            a = True
    except:
        a = False
    # bool 자료형을 가진 a를 추출함으로써 함수 반환
    return a
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
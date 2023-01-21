def over(scores):
    # 60점 이상을 담을 리스트 생성
    over60 = []
    for i in scores:
        # i가 60점 보다 크다면
        # over60이라는 리스트에 값을 추가하는
        # 조건문 생성
        if i >= 60:
            over60.append(i)
    # return함수를 통해서 값을 반환
    # len을 통해서 60점 이상인 과목이 들어있는
    # over60의 개수를 측정함.
    return len(over60)
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3

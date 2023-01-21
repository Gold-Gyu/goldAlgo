def max_score(scores):
    # 최고점을 저장할 변수 생성
    max_memory = 0
    # 인덱스 0번부터 비교하는 반복문 실행
    # 30부터 70점까지 실행됨
    for i in scores:
        # i가 max_memory보다 크거나 같다면
        # 처음 만든 변수 max_memory에 해당 값을 저장
        if i >= max_memory:
            max_memory = i
    # 반복문이 끝나고 return함수를 통해서
    # max_memory, 즉 최고점을 반환해서 함수를 완성        
    return max_memory
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90

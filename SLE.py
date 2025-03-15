
# 소수점 보정
def correction(x):
    return round(x, 3)


# 싱귤러인지 체크
def check_singular(matrix, sum):
    if set(matrix) == set([0]) and sum!=0:
        print("error : Singular")

        exit(code=0)


# 각 행렬 n**2 형태로 만들 것 x_1 : 4.231  x_2 : 1.123  x_3 : 2.125
matrix=[
    [2, 1, 3],
    [3, 3, 2],
    [1, 2, 3],
]


#각 열의 합
sum = [
    15.96,
    20.312,
    12.852,
]


# 기입을 잘못 했울 경우 error
if len(matrix) != len(sum):
    print("sum과 matrix의 개수가 맞지 않습니다. 다시한번 확인해주시기 바랍니다.")
    print("sum의 수 : %d \n matrix의 수 : %d", len(sum), len(matrix) )

    exit(code=0)

elif len(matrix) != len(matrix[0]):
    print("matrix 가 n**2 형태가 아닙니다.")
    exit(code=0)


# 본 코드
else:

    # 주대각선을 1로 만드는 코드

    LEN_OF_MATRIX = len(matrix)


    for i in range(LEN_OF_MATRIX-1):

        # 기준이 되는 열의 주대각선 원소로 연산
        standard_num_now = matrix[i][i]


        # 기준이 되는 열의 주대각선 원소로 각 항과 모든 항의 합을 나눔 (주대각선 1 만들기)
        for j in range(LEN_OF_MATRIX):
                matrix[i][j] = matrix[i][j]/standard_num_now

        sum[i] /= standard_num_now


        # 기준이 되는 열의 주대각선 밑에 있는 수를 모두 0으로 조작함
        for j in range(i+1, LEN_OF_MATRIX ):
            standard_num_next = matrix[j][i]

            for k in range(LEN_OF_MATRIX):
                matrix[j][k] -= matrix[i][k]*standard_num_next

            sum[j] -= sum[i]*standard_num_next

        check_singular(matrix[i+1], sum[i+1])



    # 마지막 열 보정(주대각선을 1로 만드는 코드가 마지막에는 적용되지 않음)
    sum[-1] /= matrix[-1][-1]
    matrix[-1][-1] = 1




# 주대각선 뒤 수들을 없애는 코드

    for i in range(LEN_OF_MATRIX-1):
        # 이미 구한 근을 이용해 밑에서 부터 차례대로 뒤 숫자들을 없앰
        standard_num_root = sum[-(i+1)]

        for j in range(2+i,LEN_OF_MATRIX+1):
            sum[(-1)*j] -= matrix[(-1)*j][-(i+1)]*standard_num_root
            matrix[-1*j][-(i+1)] = 0



for c in sum:
    # 근 보정 후 출력
    print(correction(c))


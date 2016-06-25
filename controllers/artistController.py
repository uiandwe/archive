__author__ = 'hyeonsj'
import collections


def get_artists(dc, filed, page):

    filed_list = []

    #특정 필드가 아니면 artist테이블의 모든 칼럼 이름을 가져와서 filed_list에 넣음
    if not filed:
        filed = "*"
        sql = " SHOW COLUMNS FROM artists; "
        cur = dc.find(sql)

        for item in cur:
            filed_list.append(item[0])
    else:
        for item in filed.split(","):
            filed_list.append(item)
    sql = "SELECT "+filed+"  FROM artists "
    cur = dc.find(sql)

    if type(cur) is tuple:
        #알 수 없는 컬럼일 경우
        if cur[0] == 1054:
            return {'status': "400", 'data': "", 'message': cur[1]}

    json_list = []

    for item in cur:
        d = collections.OrderedDict()
        #입력된 칼럼별로 dict 생성
        for idx, column in enumerate(filed_list):
            d[column] = item[idx]

        json_list.append(d)

    return {'status': "200", 'data': json_list, 'message': "success"}

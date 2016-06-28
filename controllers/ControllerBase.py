__author__ = 'hyeonsj'


def check_sql_error(sql_code, sql_message):
    #객체가 아닌 int 형일 경우 에러 코드로 판단
    if isinstance(sql_code, int):
        #알 수 없는 컬럼일 경우
        if sql_code == 1054:
            return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': sql_message}
    if len(sql_code) <= 0:
        return {'status': "400", 'code': "UnknownFiled", 'data': "", 'message': "잘못된 파라미터 요청입니다."}

    return True


def sql_to_dict(sql_data, sql_filed):
    json_data_list = []
    for item in sql_data:
        json_data_list.append(item.to_dict(item, sql_filed))

    if len(json_data_list) <= 1:
        return json_data_list[0]

    return json_data_list
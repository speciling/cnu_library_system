from config.config_db import connection_db


# 회원목록 조회
def get_members():
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = "SELECT * FROM tbl_member;"
        curs.execute(sql)
        rows = curs.fetchall()
    finally:
        conn.close()

    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: ID\tNAME\tPHONE\tDATE')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# 회원여부 판단
def member_match(member_num):
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = f"""
                    SELECT *
                    FROM tbl_member
                    WHERE member_id = "{member_num}"
                """
        curs.execute(sql)
        result = curs.rowcount
    finally:
        conn.close()

    return result


# 회원 검색
def find_members():
    print(':: 회원번호를 입력하세요.')
    member_num = input('>> 회원 번호: ')

    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = f"""
                    SELECT *
                    FROM tbl_member
                    WHERE member_id = "{member_num}"
                """
        curs.execute(sql)
        result = curs.fetchall()
    finally:
        conn.close()

    print(f':: {result[0].values()}' if result else '회원이 존재하지 않습니다.')

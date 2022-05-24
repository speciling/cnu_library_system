######################################################################
# 프로그램: 도서관리 프로그램
# 작성자: 지연우
# 작성일자: 2022.05.10
# 내용:
#  - 메인화면 출력
#  - 프로그램 번호 입력 -> 실행
######################################################################

import sys
import service.BookService as bookService

# BookService(실제 코드) -> bookService(사용)

while True:  # 조건 1
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: CNU LIBRARY')
    print('::   - ADMIN Mode')
    print('::   - ver1.0')
    print('::   - made by Yeonwj')
    print('::   - last update 2022.05.10')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('::   1.도서 목록')
    print('::   2.도서 검색')
    print('::   3.도서 대출')
    print('::   4.도서 반납')
    print('::   5.회원 목록')
    print('::   6.회원 검색')
    print('::   7.프로그램 종료')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

    while True:  # 조건 2
        print(':: 실행하고 싶은 서비스의 번호를 입력하세요.')
        select_num = int(input('>> 입력: '))
        if 1 <= select_num <= 7:
            break
        else:
            print("경고! 1부터 7 사이의 숫자를 입력해주세요")

    if select_num == 1:  # 도서 목록
        bookService.get_books()
    elif select_num == 2:  # 도서 검색
        bookService.search_books()
    elif select_num == 3:  # 도서 대출
        pass
    elif select_num == 4:  # 도서 반납
        pass
    elif select_num == 5:  # 회원 목록
        pass
    elif select_num == 6:  # 회원 검색
        pass
    elif select_num == 7:  # 프로그램 종료
        print('Exit program, Bye Bye :)')
        sys.exit()
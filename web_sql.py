import sqlite3
conn = sqlite3.connect("lib.db",check_same_thread = False)
cursor = conn.cursor()
#查
class search:
    class book:
        def book_name_author(bookname,author):
            sql = "select * " \
                  "from book " \
                  "where BookName LIKE ('%%%s%%') " \
                  "and writer like ('%%%s%%')" % (bookname,author)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def book_name(str):#搜索图书名称
            sql = "select * from book where BookName LIKE ('%%%s%%')" %(str)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def writer(str):#搜索图书作者
            sql = "select * from book where Writer LIKE ('%%%s%%')" %(str)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def ISBN(str):#搜索图书编号
            sql = "select * from book where ISBN LIKE ('%%%s%%')" %(str)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def publisherDate(str):#搜索图书出版日期
            sql = "select * from book where PublisherDate LIKE ('%%%s%%')" %(str)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def publiserNo(self):#搜索出版社编号
            sql = "select * from book where PublisherNo LIKE ('%%%s%%')" %(self)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def publisherName(self):#搜索出版社名称
            sql = "select ISBN,BookName,Writer,WhereFloor,State,Price,PublisherDate,book.PublisherNo,PublisherName " \
                  "from book,publisher " \
                  "where book.PublisherNo=publisher.PublisherNo AND PublisherName LIKE ('%%%s%%')" %(self)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
    class document:
        pass
    class teacher:
        def teacherNo(self):
            sql = "select * from teacher where TeacherNo = LIKE ('%%%s%%')" %(self)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def teacherName(self):
            sql = "select * from teacher where TeacherName LIKE ('%%%s%%')" %(self)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
        def office(self):
            sql = "select * from teacher where office LIKE ('%%%s%%')" %(self)
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
            return res
#增
class insert:
    def book(self):
        pass
    def bookcalss(self):
        pass
    def borrow(self):
        pass
    def publisher(self):
        pass
    def student(self):
        pass
    def teacher(self):
        pass
#删
class delete:
    def book(self):
        pass
    def bookcalss(self):
        pass
    def borrow(self):
        pass
    def publisher(self):
        pass
    def student(self):
        pass
    def teacher(self):
        pass
#改
class update:
    def book(self):
        pass
    def bookcalss(self):
        pass
    def borrow(self):
        pass
    def publisher(self):
        pass
    def student(self):
        pass
    def teacher(self):
        pass

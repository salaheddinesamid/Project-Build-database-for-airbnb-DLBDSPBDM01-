import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    
    def test_select_all_employees(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user;")
        result = cursor.fetchall()
        expected = (
    (1, 'Alice Smith', 'alice.smith@example.com', '123-456-7890', 'https://example.com/profiles/alice.jpg', True),
    (2, 'Bob Johnson', 'bob.johnson@example.com', '098-765-4321', 'https://example.com/profiles/bob.jpg', False),
    (3, 'Charlie Brown', 'charlie.brown@example.com', '555-555-5555', 'https://example.com/profiles/charlie.jpg', True),
    (4, 'Dana White', 'dana.white@example.com', '444-444-4444', 'https://example.com/profiles/dana.jpg', False),
    (5, 'Eve Black', 'eve.black@example.com', '333-333-3333', 'https://example.com/profiles/eve.jpg', True),
    (6, 'Frank Adams', 'frank.adams@example.com', '222-222-2222', 'https://example.com/profiles/frank.jpg', False),
    (7, 'Grace Taylor', 'grace.taylor@example.com', '777-777-7777', 'https://example.com/profiles/grace.jpg', True),
    (8, 'Henry Lee', 'henry.lee@example.com', '666-666-6666', 'https://example.com/profiles/henry.jpg', False),
    (9, 'Ivy Clark', 'ivy.clark@example.com', '999-999-9999', 'https://example.com/profiles/ivy.jpg', True),
    (10, 'Jack Harris', 'jack.harris@example.com', '111-111-1111', 'https://example.com/profiles/jack.jpg', False),
    (11, 'Kate Miller', 'kate.miller@example.com', '444-555-6666', 'https://example.com/profiles/kate.jpg', True),
    (12, 'Luke Evans', 'luke.evans@example.com', '777-888-9999', 'https://example.com/profiles/luke.jpg', False),
    (13, 'Mia Roberts', 'mia.roberts@example.com', '222-333-4444', 'https://example.com/profiles/mia.jpg', True),
    (14, 'Nick Wilson', 'nick.wilson@example.com', '555-666-7777', 'https://example.com/profiles/nick.jpg', False),
    (15, 'Olivia Brown', 'olivia.brown@example.com', '888-999-0000', 'https://example.com/profiles/olivia.jpg', True),
    (16, 'Paul Davis', 'paul.davis@example.com', '111-222-3333', 'https://example.com/profiles/paul.jpg', False),
    (17, 'Quinn Allen', 'quinn.allen@example.com', '333-444-5555', 'https://example.com/profiles/quinn.jpg', True),
    (18, 'Rachel Young', 'rachel.young@example.com', '666-777-8888', 'https://example.com/profiles/rachel.jpg', False),
    (19, 'Samuel Hill', 'samuel.hill@example.com', '999-000-1111', 'https://example.com/profiles/samuel.jpg', True),
    (20, 'Tina Carter', 'tina.carter@example.com', '222-333-4444', 'https://example.com/profiles/tina.jpg', False)
        )
        self.assertEqual(result, expected)
        conn.close()

    def test_count(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user;")
        result = cursor.fetchall().__len__()
        self.assertEqual(result, 20)
        conn.close()


        
if __name__ == '__main__':
    unittest.main()
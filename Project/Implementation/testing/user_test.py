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
    (5, 'Eve Black', 'eve.black@example.com', '333-333-3333', 'https://example.com/profiles/eve.jpg', True)
        )
        self.assertEqual(result, expected)
        conn.close()

if __name__ == '__main__':
    unittest.main()
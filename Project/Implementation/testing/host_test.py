import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    
    def test_select_all_employees(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM host;")
        result = cursor.fetchall()
        expected = (
            (1, 1, 4.5),
    (2, 2, 4.0),
    (3, 3, 3.5),
    (4, 4, 4.2),
    (5, 5, 4.8)
        )
        self.assertEqual(result, expected)
        conn.close()

if __name__ == '__main__':
    unittest.main()
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
(5, 5, 4.8),
(6, 6, 4.7),
(7, 7, 4.3),
(8, 8, 4.6),
(9, 9, 4.1),
(10, 10, 3.9),
(11, 11, 4.4),
(12, 12, 4.9),
(13, 13, 3.8),
(14, 14, 4.0),
(15, 15, 4.3),
(16, 16, 4.2),
(17, 17, 4.7),
(18, 18, 3.6),
(19, 19, 4.5),
(20, 20, 4.8)

        )
        self.assertEqual(result, expected)
        conn.close()

if __name__ == '__main__':
    unittest.main()
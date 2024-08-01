import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    def test_select_all_employees(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transaction;")
        result = cursor.fetchall()
        expected = (
            (1, 1, 1, 100.00),
    (2, 2, 2, 250.00),
    (3, 3, 3, 80.00),
    (4, 4, 4, 150.00),
    (5, 5, 5, 120.00),
    (6, 1, 6, 200.00),
    (7, 2, 7, 500.00),
    (8, 3, 8, 180.00),
    (9, 4, 9, 250.00),
    (10, 5, 10, 120.00),
    (11, 1, 11, 300.00),
    (12, 2, 12, 400.00),
    (13, 3, 13, 150.00),
    (14, 4, 14, 600.00),
    (15, 5, 15, 800.00),
    (16, 1, 16, 80.00),
    (17, 2, 17, 120.00),
    (18, 3, 18, 100.00),
    (19, 4, 19, 350.00),
    (20, 5, 20, 150.00)

        )
        self.assertEqual(result, expected)
        conn.close()

    def test_number_rows(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transaction;")
        result = cursor.fetchall().__len__()
        self.assertGreaterEqual(result,20)
if __name__ == '__main__':
    unittest.main()
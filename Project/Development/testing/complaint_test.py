import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    
    def test_select_all_employees(self):
        conn = pymysql.connect(host='localhost', user='root', password='samidsamid', db='airbnb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM complaint;")
        result = cursor.fetchall()
        expected = (
            (1, 1, 'The apartment was not clean upon arrival.', '2024-01-15'),
    (2, 2, 'The host was unresponsive.', '2024-02-10'),
    (3, 3, 'There was no hot water in the shower.', '2024-03-05'),
    (4, 4, 'The Wi-Fi was not working.', '2024-03-22'),
    (5, 5, 'The property was not as described.', '2024-04-10'),
    (6, 6, 'The bed was uncomfortable.', '2024-04-25'),
    (7, 7, 'The host canceled the booking last minute.', '2024-05-05'),
    (8, 8, 'The location was noisy at night.', '2024-05-15'),
    (9, 9, 'The check-in process was very difficult.', '2024-05-25'),
    (10, 10, 'The amenities listed were not available.', '2024-06-01'),
    (11, 11, 'The heating system was not working.', '2024-06-10'),
    (12, 12, 'There were bugs in the apartment.', '2024-06-20'),
    (13, 13, 'The kitchen was not equipped as promised.', '2024-07-01'),
    (14, 14, 'The host was rude and unprofessional.', '2024-07-10'),
    (15, 15, 'The air conditioning was not working.', '2024-07-20'),
    (16, 16, 'There was no parking available as listed.', '2024-08-01'),
    (17, 17, 'The property had a bad smell.', '2024-08-15'),
    (18, 18, 'The host entered the property without notice.', '2024-08-25'),
    (19, 19, 'The apartment was too cold.', '2024-09-05'),
    (20, 20, 'The host charged extra fees not listed.', '2024-09-15')
        )
        self.assertEqual(result, expected)
        conn.close()

if __name__ == '__main__':
    unittest.main()
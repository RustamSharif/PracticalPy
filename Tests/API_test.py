import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.token = "YOUR_TOKEN_HERE"  # Замените YOUR_TOKEN_HERE на ваш токен
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {"Authorization": f"OAuth {self.token}"}
        
    def test_create_folder_success(self):
        folder_name = "testFolder"
        response = requests.put(f"{self.base_url}?path={folder_name}", headers=self.headers)
        self.assertEqual(response.status_code, 201)
        
        # Проверка наличия папки
        response = requests.get(f"{self.base_url}?path={folder_name}", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
    def test_create_folder_already_exists(self):
        folder_name = "existingFolder"
        # Предварительно создаем папку
        requests.put(f"{self.base_url}?path={folder_name}", headers=self.headers)
        # Попытка создать папку с тем же именем
        response = requests.put(f"{self.base_url}?path={folder_name}", headers=self.headers)
        self.assertEqual(response.status_code, 409)  # Код 409 означает конфликт из-за уже существующей папки
        
    def tearDown(self):
        # Очистка после тестов
        folder_name = "testFolder"
        requests.delete(f"{self.base_url}?path={folder_name}", headers=self.headers)

if __name__ == '__main__':
    unittest.main()
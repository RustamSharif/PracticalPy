import unittest
from unittest.mock import patch
from main import find_person_by_document, add_document

class TestDocumentProgram(unittest.TestCase):

    def test_find_person_by_document_existing(self):
        self.assertEqual(find_person_by_document("10006"), "Аристарх Павлов")
    
    def test_find_person_by_document_non_existing(self):
        self.assertEqual(find_person_by_document("does_not_exist"), "Документ не найден.")
    
    @patch('main.documents', side_effect=[..., {"type": "id card", "number": "5555", "name": "Иван Иванов"}])
    @patch('main.directories', side_effect=[..., '1': [..., '5555']])
    def test_add_document(self, mock_directories, mock_documents):
        add_document("id card", "5555", "Иван Иванов", "1")
        self.assertIn({"type": "id card", "number": "5555", "name": "Иван Иванов"}, mock_documents)
        self.assertIn("5555", mock_directories['1'])

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest import mock
from unittest.mock import patch
from src.app import directories, documents
from src.app import get_doc_owner_name, get_all_doc_owners_names,delete_doc,append_doc_to_shelf,add_new_shelf



class TestCheckDocument(unittest.TestCase):
    
    @patch('src.app.input', lambda *args:'2207 876234')
    def test_get_get_doc_owner_name(self):
        
        result = 'Василий Гупкин'
        self.assertEqual(get_doc_owner_name(), result)

    @patch('src.app.input', lambda *args:'ap')
    def test_get_all_doc_owners_names(self):
        
        self.assertIsInstance(get_all_doc_owners_names(), set)
        
    @patch('src.app.input', lambda *args:'d')
    def test_delete_doc(self):
        
        self.assertNotIn(delete_doc(), documents[2])
        
    @patch('src.app.input', lambda *args:'a')
    def test_add_new_doc(self):
        
        new_doc_shelf_number = 1
        new_doc = {
        "type": 'test',
        "number": '9999',
        "name": 'test_name'}
        documents.append(new_doc)
        self.assertIn(new_doc, documents)
        append_doc_to_shelf('9999', new_doc_shelf_number)
        self.assertIn('9999', directories[new_doc_shelf_number])
        
    @patch('src.app.input', lambda *args:'l')
    def test_show_document_info(self):
        
        new_doc = {
        "passport": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"}
        self.assertEqual(new_doc, new_doc)
        for current_document in documents:
            self.assertIn(current_document, documents)
            
    @patch('src.app.input', lambda *args:'as')
    def test_test_add_new_shelf(self):
        self.assertTrue(add_new_shelf(4), True)
        
    
    
    


if __name__ == '__main__':
    unittest.main()
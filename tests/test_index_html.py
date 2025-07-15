import os
import unittest
from bs4 import BeautifulSoup

class TestIndexHtml(unittest.TestCase):
    def setUp(self):
        html_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
        with open(html_path, 'r', encoding='utf-8') as f:
            self.soup = BeautifulSoup(f, 'html.parser')

    def test_title_present(self):
        title_tag = self.soup.title
        self.assertIsNotNone(title_tag, 'No <title> tag found')
        self.assertEqual(title_tag.string.strip(), 'Sukhmander Singh')

    def test_link_to_style(self):
        link_tag = self.soup.find('link', rel='stylesheet', href='css/style.css')
        self.assertIsNotNone(link_tag, 'No link to css/style.css found')

if __name__ == '__main__':
    unittest.main()

import unittest
from huffman_algorithm import huffman_encode, huffman_decode
from file_processor import File

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.file = File()
        self.text = "This is an test for huffman encoding."
        self.encoded_text, self.huffman_codes = huffman_encode(self.text)

    def test_huffman_encode(self):
        self.assertIsInstance(self.encoded_text, str)
        self.assertIsInstance(self.huffman_codes, dict)
        self.assertGreater(len(self.encoded_text), 0)
        self.assertGreater(len(self.huffman_codes), 0)

    def test_huffman_decode(self):
        decoded_text = huffman_decode(self.encoded_text, self.huffman_codes)
        self.assertEqual(decoded_text, self.text)

    def test_file_compression(self):
        compressed_text = self.file.compressed_file("test_compressed.bin", self.encoded_text)
        decoded_text = huffman_decode(compressed_text, self.huffman_codes)
        self.assertEqual(decoded_text, self.text)
        
    def test_file_size(self):
        original_size, compressed_size = self.file.compare_files_size("input.txt", "test_compressed.bin")
        self.assertGreater(original_size, compressed_size)

if __name__ == "__main__":
    unittest.main()
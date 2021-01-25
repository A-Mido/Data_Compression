import sys
from huffman_coding import HuffmanCoding

path = "test.txt"

output_path = HuffmanCoding(path).compress()

print("Compressed file path: " + output_path)
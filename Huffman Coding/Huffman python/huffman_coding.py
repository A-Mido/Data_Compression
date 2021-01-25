import os
import heapq
from heap_node import HeapNode

class HuffmanCoding(HeapNode):

    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
            
    # functions for compression:

    def frequency_dictionary(self, text):
        # this function will return the feq of each word
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency        

    def priority_queue(self, frequency):
        # make a prio queue based on the fequency
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        # if the tree has more than one node
        while(len(self.heap) > 1):
            node_1 = heapq.heappop(self.heap)
            node_2 = heapq.heappop(self.heap)
            # merge to  one upper node 
            merged = HeapNode(None, node_1.freq + node_2.freq)
            merged.left = node_1
            merged.right = node_2
            heapq.heappush(self.heap, merged)

    def code_book(self, node, code):
        if (node == None):
            return
        # assign every char to a cretain code
        # the root has no code
        if (node.char != None):
            self.codes[node.char] = code

        # mapping every left branch to 0 and right to 1
        self.code_book(node.left, code + "0")
        self.code_book(node.right, code + "1")


    def generate_code(self):
        root = heapq.heappop(self.heap)
        code = ""
        # sending a empty code with the root
        self.code_book(root, code)

    def get_encoded_text(self, text):
        code_length = ""
        for character in text:
            code_length += self.codes[character]
        return code_length
        
    def padded_encoded_text(self, encoded_text):

        extra_padding = 8 - (len(encoded_text) % 8)
        for i in range(extra_padding):
            encoded_text += "0"

        padding_info = "{0:08b}".format(extra_padding)
        encoded_text = padding_info + encoded_text
        return encoded_text

    def byte_conversion(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        arr = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            arr.append(int(byte, 2))
        return arr


    def compress(self):
        file_name, file_ext = os.path.splitext(self.path)
        # we make a binary file to store our output in binary
        output_file = file_name + ".bin"

        with open(self.path, 'r') as file, open(output_file, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.frequency_dictionary(text)
            self.priority_queue(frequency)
            self.merge_nodes()
            self.generate_code()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.padded_encoded_text(encoded_text)

            txt_bytes = self.byte_conversion(padded_encoded_text)
            output.write(bytes(txt_bytes))

        print('Compressed')
        return output_file



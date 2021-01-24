import os
import heapq
from heap_node import HeapNode

class HuffmanCoding():
    def __init__(self, path):
        self.path = path

    def frequency_dictionary(self, text):
        # this function will return the feq of each word
        frequency = {}
        for character in text:
            if character not in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency        

    def priority_queue(self, frequency):
        # make a prio queue based on the fequency
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            # pushing the node into heap queue 
            heapq.heappush(self.heap, node)

    def compress(self):
        file_name, file_ext = os.path.splitext(self.path)
        # we make a binary file to store our output in binary
        output_file = file_name + ".bin"

        with open(self.path, 'r') as file, open(output_file, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.frequency_dictionary(text)
            self.priority_queue(frequency)


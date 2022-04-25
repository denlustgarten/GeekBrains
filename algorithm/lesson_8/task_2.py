"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""
from collections import Counter, defaultdict


def get_frequency_table(text):
    result = dict()
    for char, freq in Counter(text).items():
        result[char] = freq
    return result


class MyNode(object):
    def __init__(self, name=None, value=None, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}=>left {self.left} - right {self.right}'


class HuffmanTree(object):
    def __init__(self, frequency_table):
        self.leafs = [MyNode(name=k, value=v) for k, v in frequency_table.items()]
        self.encode_char = defaultdict(str)

        while len(self.leafs) != 1:
            self.leafs.sort(key=lambda node: node.value, reverse=True)
            n = MyNode(value=(self.leafs[-1].value + self.leafs[-2].value))
            n.left = self.leafs.pop()
            n.right = self.leafs.pop()
            self.leafs.append(n)
        self.root = self.leafs[0]
        self.buffer = list(range(10))

    def huffman_encode(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(f'"{node.name}" в кодировке Хаффмана:', end='')
            for i in range(length):
                self.encode_char[node.name] += str(self.buffer[i])
                print(self.buffer[i], end='')
            print('\n')
            return
        self.buffer[length] = 0
        self.huffman_encode(node.left, length + 1)
        self.buffer[length] = 1
        self.huffman_encode(node.right, length + 1)

    def show_code(self, text):
        self.huffman_encode(self.root, 0)
        print(f'"{text}" в Кодировке Хаффмана:')
        for ch in text:
            print(self.encode_char.get(ch), end=' ')


if __name__ == '__main__':
    text = 'hello, my name is Denis'
    result = get_frequency_table(text)
    # print(result)
    tree = HuffmanTree(result)
    tree.show_code(text)

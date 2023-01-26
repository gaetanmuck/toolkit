import toolkit as tk
import os
import unittest


class TestFile(unittest.TestCase):

    def test_read_file(self):
        path = './temp.txt'
        f = open(path, 'w')
        f.write('Hello world!')
        f.close()
        content = tk.read_file(path)
        self.assertEqual(content, 'Hello world!')


    def test_read_lines(self):
        path = './temp.txt'
        f = open(path, 'w')
        f.write('Hello world!\nFooBar')
        f.close()
        lines = tk.read_lines(path)
        self.assertEqual(lines[-2], 'Hello world!\n')
        self.assertEqual(lines[-1], 'FooBar')
        

    def test_create_file(self):
        path = './temp.txt'
        tk.create_file(path, 'Hello world!')
        self.assertTrue(os.path.exists(path))

        f = open(path, 'r')
        content = f.read()
        f.close()
        self.assertEqual(content, 'Hello world!')

        os.remove(path)

    
    def test_append_file(self):
        path = './temp.txt'
        f = open(path, 'w')
        f.write('Hello world!\nFooBar')
        f.close()
        tk.append_file(path, 'Baz')

        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        self.assertEqual(lines[-1], 'FooBarBaz')




    





if __name__ == '__main__': unittest.main()
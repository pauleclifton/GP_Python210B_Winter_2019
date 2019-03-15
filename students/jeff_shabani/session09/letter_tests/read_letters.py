import os
import unittest

with open('Karsten Willems.txt', 'rt') as infile:
    lines = infile.readlines()
    for n, line in enumerate(lines):
        print(n, line)
    print(lines)

cd = os.getcwd()


for i in os.walk(cd):
    files = [j for j in i[2]]
print(files)




class TextTests(unittest.TestCase):

    def test_text(self):
        with open('Karsten Willems.txt', 'rt') as infile:
            lines = infile.readlines()
            self.assertEqual(lines[0], 'Dear Karsten Willems,\n')
            self.assertEqual(lines[1], '\n')
            self.assertEqual(lines[2], 'Thank you for your kind donation of $0\n')
            self.assertEqual(lines[3], '\n')
            self.assertEqual(lines[4], 'Rest assured that these funds will be put to optimal use.\n')
            self.assertEqual(lines[5], '\n')
            self.assertEqual(lines[6], 'Best regards,\n')
            self.assertEqual(lines[7], 'The Charitable Charities Team')

    def test_files_written(self):
        files_to_test=['Karsten Willems.txt', 'read_letters.py', 'Sammy Maudlin.txt']
        for file in files:
            self.assertIn(file, files_to_test)




if __name__ == '__main__':
    unittest.main()

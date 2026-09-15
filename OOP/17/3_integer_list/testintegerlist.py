from integerlist import IntegerList
from unittest import TestCase,main

class TestIntegerList(TestCase):

    def test_add(self):
        i=IntegerList([1,2,3])
        init_len=len(i.__data)
        i.add(4)
        self.assertEqual(init_len+1,len(i.__data))

if __name__=='__main__':
    main()
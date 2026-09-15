class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
    

from unittest import TestCase,main

class TestIntegerList(TestCase):

    def test_add(self):
        i=IntegerList(1,2,3)
        result = i.add(4)
        self.assertEqual([1, 2, 3, 4], result)
        self.assertEqual([1, 2, 3, 4], i.get_data())
    
    def test_add_not_int(self):
        i=IntegerList(1,2,3)
        with self.assertRaises(ValueError) as ex:
            i.add('Cat')
        self.assertEqual('Element is not Integer',str(ex.exception))
    
    def test_remove_index(self):
        i=IntegerList(1,2,3)
        result = i.remove_index(1)
        self.assertEqual(2, result)
        self.assertEqual([1, 3], i.get_data())
    
    def test_remove_index_exception(self):
        i=IntegerList(1,2,3)
        with self.assertRaises(IndexError) as ex:
            i.remove_index(5)
        self.assertEqual('Index is out of range',str(ex.exception))
    
    def test_init_int(self):
        i=IntegerList(1,2,3,'Two', 4.5, None)
        arr=i.get_data()
        self.assertEqual([1,2,3],arr)
    
    def test_get_int_at_position(self):
        i=IntegerList(1,2,3,4)
        idx=i.get(2)
        self.assertEqual(3,idx)
    
    def test_get_int_at_position_exception(self):
        i=IntegerList(1,2,3,4)
        with self.assertRaises(IndexError) as ex:
            i.get(5)
        self.assertEqual('Index is out of range',str(ex.exception))

    def test_insert(self):
        i=IntegerList(1,2,3)
        i.insert(1, 4)
        self.assertEqual([1, 4, 2, 3], i.get_data())
    
    def test_insert_out_of_range(self):
        i=IntegerList(1,2,3)
        with self.assertRaises(IndexError) as ex:
            i.insert(4,5)
        self.assertEqual('Index is out of range',str(ex.exception))
    
    def test_insert_el_not_int(self):
        i=IntegerList(1,2,3)
        with self.assertRaises(ValueError) as ex:
            i.insert(2,"word")
        self.assertEqual("Element is not Integer",str(ex.exception))
    
    def test_get_biggest(self):
        i=IntegerList(2,4,1,3)
        self.assertEqual(4,i.get_biggest())

    def test_get_index(self):
        i=IntegerList(4,1,3,2)
        self.assertEqual(3,i.get_index(2))


if __name__=='__main__':
    main()
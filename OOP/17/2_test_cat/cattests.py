from cat import Cat
from unittest import TestCase,main

class CatTests(TestCase):

    def setUp(self):
        self.c=Cat('Pussy')
    

    def test_cat_size(self):
        current_size=self.c.size
        self.c.eat()
        self.assertEqual(current_size+1,self.c.size)
    
    def test_cat_is_fed(self):
        self.c.eat()
        self.assertTrue(self.c.fed)
    
    def test_cat_cannot_eat(self):
        self.c.fed=True
        with self.assertRaises(Exception) as ex:
            self.c.eat()
        self.assertEqual('Already fed.',str(ex.exception))
        self.c.fed=False

    def test_cat_cannot_sleep(self):
        self.c.fed=False
        with self.assertRaises(Exception) as ex:
            self.c.sleep()
        self.assertEqual('Cannot sleep while hungry',str(ex.exception))
    
    def test_cat_not_sleepy_after_sleeping(self):
        self.c.eat()
        self.c.sleep()
        self.assertFalse(self.c.sleepy)
        

if __name__=='__main__':
    main()
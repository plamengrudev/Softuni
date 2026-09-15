from worker import Worker
import unittest


class TestWorker(unittest.TestCase):

    def setUp(self):
        self.w=Worker("George",1000,100)

    def test_init(self):
        self.assertEqual("George",self.w.name)
        self.assertEqual(1000,self.w.salary)
        self.assertEqual(100,self.w.energy)
        self.assertEqual(0,self.w.money)
    
    def test_rest(self):
        current_energy=self.w.energy
        self.w.rest()
        self.assertEqual(current_energy+1,self.w.energy)
    
    def test_work_raises_exception(self):
        current_energy=self.w.energy
        self.w.energy=0
        with self.assertRaises(Exception) as ex:
            self.w.work()
        self.assertEqual('Not enough energy.',str(ex.exception))
        self.w.energy=current_energy
    
    def test_money(self):
        current_money=self.w.money
        self.w.work()
        self.assertEqual(current_money+self.w.salary,self.w.money)

    def test_energy(self):
        current_energy=self.w.energy
        self.w.work()
        self.assertEqual(current_energy-1,self.w.energy)
    
    def test_get_info(self):
        returned_string=f'{self.w.name} has saved {self.w.money} money.'
        self.assertEqual(returned_string,self.w.get_info())


if __name__=="__main__":
    unittest.main()

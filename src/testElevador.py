import unittest
from elevador import Elevador


class TestElevador(unittest.TestCase):
    def setUp(self):
        self.elevator = Elevador("Test Elevator", [])
    """
    def test_initialization(self):
        self.assertEqual(self.elevator.name, "Test Elevator")
        self.assertEqual(self.elevator.current, 0)
        self.assertIsNone(self.elevator.direction)
        self.assertEqual(self.elevator.lift, [])

    def test_increment(self):
        self.elevator.current = 0
        self.elevator.increment()
        self.assertEqual(self.elevator.current, 1)

    def test_decrement(self):
        self.elevator.current = 2
        self.elevator.decrement()
        self.assertEqual(self.elevator.current, 1)

    def test_move_up(self):
        self.elevator.current = 3
        self.elevator.lift = ["5"]
        self.elevator.move()
        self.assertEqual(self.elevator.current, 5)
    
    def test_move_down(self):
        self.elevator.current = 3
        self.elevator.lift = ["2"]
        self.elevator.move()
        self.assertEqual(self.elevator.current, 2)

    def test_stop_at_floor(self):
        self.elevator.current = 3
        self.elevator.lift = ["3"]
        self.assertEqual(self.elevator.current, 3)

    def test_move_stop_at_floor_equals(self):
        self.elevator.current = 3
        self.elevator.lift = ["3"]
        self.elevator.move()
        self.assertEqual(self.elevator.current, 3)
        self.assertNotIn("3", self.elevator.lift)
    
    def test_move_stop_at_floor_up(self):
        self.elevator.current = 3
        self.elevator.lift = ["10"]
        self.elevator.move()
        self.assertEqual(self.elevator.current, 10)
        self.assertNotIn("10", self.elevator.lift)
 
    def test_move_stop_at_floor_down(self):
        self.elevator.current = 3
        self.elevator.lift = ["0"]
        self.elevator.move()
        self.assertEqual(self.elevator.current, 0)
        self.assertNotIn("0", self.elevator.lift)
    """
    def test_move_multiple_lift_requests(self):
        self.elevator.current = 0
        self.elevator.lift = ["2", "5"]
        self.elevator.move()
        self.elevator.move()
        self.assertEqual(self.elevator.current, 5)
        self.assertEqual(self.elevator.lift, [])

if __name__ == '__main__':
    unittest.main()

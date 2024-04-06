import unittest
from elevador import Elevador

lift = [] #store user requests to get on or off the elevator
NUM_ELEVATORS = 2 

class TestAssignElevator(unittest.TestCase):
    def setUp(self):
        self.elevators = [Elevador(f"E_{i}", lift) for i in range(2)]
        # 
        self.elevators[0].current = 4
        self.elevators[1].current = 0
        #self.elevators[2].current = 2
        # 
        self.elevators[0].direction = "Up"
        self.elevators[1].direction = "Up"
        #self.elevators[2].direction = "Down"

    def test_assign_elevator_up(self):
        # Probamos una solicitud de ascensor para ir hacia arriba desde el piso 6
        for elevator in self.elevators:
            assigned_elevator = elevator.assign_elevator(6, self.elevators)
              # El ascensor más cercano al piso 6 es el ascensor 0
        self.assertEqual(assigned_elevator.name, "E_0")

    def test_assign_elevator_down(self):
        for elevator in self.elevators:
            assigned_elevator = elevator.assign_elevator(2, self.elevators)
        # El ascensor más cercano al piso 7 es el ascensor 1
        self.assertEqual(assigned_elevator.name, "E_1")

    def test_assign_multiple_lift_requests(self):
        self.lift = ["2", "5"]
        assigned_elevator = None
        for floor in self.lift:
            for elevator in self.elevators:
                assigned_elevator = elevator.assign_elevator(floor, self.elevators)
                assigned_elevator.move()
        
        self.assertEqual(assigned_elevator.name, "E_0")
        

if __name__ == '__main__':
    unittest.main()

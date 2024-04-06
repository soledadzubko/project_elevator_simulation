import time

class Elevador:
    def __init__(self,name, lift):
        self.name = name
        self.current = 0
        self.direction = "Up"
        self.lift = lift

    def increment(self):
        self.current+=1
        time.sleep(1)
        print(f" ⬆ {self.name}, : ", self.current)
    
    def decrement(self):
        self.current-=1
        time.sleep(1)
        print(f"⬇ {self.name}, : ", self.current)
    
    def move(self):
        while True:
            if not self.lift:  # Si no hay solicitudes pendientes, detenerse
                break

            # Obtener el próximo piso al que se debe mover el ascensor
            next_floor = int(self.lift[0])

            if self.current > next_floor:  # Mover hacia abajo si es necesario
                self.decrement()
                self.direction = "Down"
            elif self.current < next_floor:  # Mover hacia arriba si es necesario
                self.increment()
                self.direction = "Up"
            else:  # Detenerse si se alcanza el piso deseado
                print(f"{self.name}, STOP =>: ", self.current)
                self.lift.remove(str(self.current))
                break
    
    def assign_elevator(selft, floor, elevators):
        floor = int(floor)
        closest_elevator = None
        min_distance = float('inf')

        for elevator in elevators:  
            print("mindistance:", min_distance)
            print("elevador:", elevator.name, ", ", elevator.direction)

            if elevator.direction == "Down"  and floor >= int(elevator.current):
                print("up ", floor, " < ", elevator.current)
                distance = abs(floor - elevator.current )
                if distance <= min_distance:
                    min_distance = distance
                    closest_elevator = elevator

            elif elevator.direction == "Down"  and floor <= int(elevator.current):
                distance = abs(floor - elevator.current )
                if distance <= min_distance:
                    min_distance = distance
                    closest_elevator = elevator
            elif elevator.direction == "Up" and floor <= int(elevator.current):
                distance = abs(floor - elevator.current )
                if distance <= min_distance:
                    min_distance = distance
                    closest_elevator = elevator
            elif elevator.direction == "Up"  and floor >= int(elevator.current):
                distance = abs(floor - elevator.current )
                if distance <= min_distance:
                    min_distance = distance
                    closest_elevator = elevator

        print("closest elevator:", closest_elevator.name)
        return closest_elevator
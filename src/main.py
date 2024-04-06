import threading
import time
import elevador
lift = [] #store user requests to get on or off the elevator
NUM_ELEVATORS = 2 


def get_input():
    input1 = input()
    lift.append(input1)

elevators = [elevador.Elevador(f"E_{i}", lift) for i in range(NUM_ELEVATORS)]
elevators[0].current = 3 #change the initial floor of an elevator

if __name__ == '__main__':
    print("Enter floor numbers: ", end="")
    while(True):
        t1= threading.Thread(target=get_input, name='t1')
    
        threads = []
        for i, elevator in enumerate(elevators, start=2):
            thread = threading.Thread(target=elevator.move, name=f't{i}')
            threads.append(thread)
       
        t1.start()
        
        time.sleep(3)
        #choose who which elevator should move
        if lift:
            elevator_select = elevator.assign_elevator(lift[0], elevators)
            for elevator_instance, thread_instance in zip(elevators, threads):
                if elevator_instance.name == elevator_select.name:
                    elevator_instance.move()
                    thread_instance.start()
                    break
        else:
            continue
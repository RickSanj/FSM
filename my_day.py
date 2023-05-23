"""simulator of my life"""
from queue import Queue
import random

class State:
    """class representing a state of a person"""
    def __init__(self, name: str, message: str) -> None:
        """
        init for class State
        """
        self.name = name
        self.message = message

    def __str__(self) -> str:
        """
        :return: str - message of the state
        """
        return self.message


class FSM:
    """Finite state machine class"""
    def __init__(self) -> None:
        """
        init for FSM class
        """
        self.current_state = queue.get()

    def random_events(self, hour: int) -> None:
        """
        handle different random events like
        - air alert
        - unexpected deadline
        - burnt out
        """
        random_num = random.random()

        # UNEXPECTED DEADLINE
        if random_num <= 0.30:
            print('====================')
            if self.current_state.name != 'STUDY' and self.current_state.name != 'SLEEP':
                print('Oh, there is a deadline today')
                print('I am sad')
                self.current_state = cry
                print(cry)
                print('I need to study')
                self.current_state = study
                print(study)
                queue.put("UNEXPECTED DEADLINE")
                return None

        # BURNT OUT
        elif random_num <= 0.60:
            if 8 <= hour <= 22 and self.current_state.name == 'STUDY':
                print('Oh, I am burnt out. I cannot study anymore')
                print('I need to relax')
                self.current_state = relax
                print(relax)
                queue.put("BURNT OUT")
                return None
        # AIR ALERT
        print("Oh, the air alert is on...")
        print("Rushes to the shelter")
        if (0 <= hour <= 6 or hour == 23) and self.current_state.name == 'SLEEP':
            if random.random() <= 0.25:
                print('It is too crowded to sleep. I am sad')
                self.current_state = cry
                print(cry)
            else:
                print("Luckily, it's not very crowded, so I can sleep here")
                self.current_state = sleep
                print(sleep)
        else:
            print("Let's do some studying while here")
            self.current_state = study
            print(study)
        queue.put("AIR ALERT")


    def simulate_day(self):
        """run the day"""
        hours = 24
        for hour in range(hours):
            print(hour, "o'clock:")
            if queue.empty() is False:
                # if last hour was AIR ALERT
                event = queue.get()
                if event == 'AIR ALERT':
                    if self.current_state == 'SLEEP':
                        self.current_state = sleep
                        print(sleep)
                        print("The air alert is over")
                        print("Let's get out of the shelter")
                    else:
                        print('I cannot concentrate')
                        self.current_state = relax
                        print(relax)
                        print("The air alert is over")
                        print("Let's get out of the shelter")
                elif event == 'BURNT OUT':
                    self.current_state = relax
                    print('Still relaxing.', relax)
                    print('I feel recharged and motivated again')
                else:
                    self.current_state = study
                    print(study)
                    print('Yey, I met the deadline')
            else:
                if random.random() <= 0.2:
                    self.random_events(hour)
                else:
                    if hour in [0, 1, 2, 3, 4, 5, 6]:
                        self.current_state = sleep
                        print(sleep)
                    if hour == 7:
                        print('Good morning sunshine!')
                        print("I am hungry. Let's have some breakfast")
                        self.current_state = eat
                        print(eat)
                    if hour == 8:
                        print("Let's go to classes")
                        self.current_state = study
                        print(study)
                    if hour in [9, 11, 12]:
                        self.current_state = study
                        print(study)
                    if hour == 10:
                        print('I need to make a break from studying')
                        self.current_state = relax
                        print(relax)
                    if hour == 13:
                        print("I am hungry. Let's have some lunch")
                        self.current_state = eat
                        print(eat)
                    if hour == 14:
                        print("Let's do some homework")
                        self.current_state = study
                        print(study)
                    if hour in [15, 16, 18, 19, 20]:
                        self.current_state = study
                        print(study)
                    if hour == 17:
                        print('I need to make a break from studying')
                        self.current_state = relax
                        print(relax)
                    if hour == 21:
                        print("I am hungry. Let's have some dinner")
                        self.current_state = eat
                        print(eat)
                    if hour == 22:
                        print("I don't want to study anymore. Let's have some personal time")
                        self.current_state = relax
                        print(relax)
                    if hour == 23:
                        print("It's late and I'm tired. Let's sleep")
                        self.current_state = sleep
                        print(sleep)
            print('------')


sleep = State('SLEEP', 'Zzzzzz...')
eat = State('EAT', 'YUM... The food is so delicious')
study = State('STUDY', 'I am studying')
cry = State('CRY', 'Cry...')
relax = State('RELAX', 'I am watching some TV show')

# create queue (by default sleeping at 0 o'clock)
queue = Queue()
queue.put(sleep)
if __name__ == '__main__':
    fsm = FSM()
    fsm.simulate_day()

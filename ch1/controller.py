class Controller:

    def __init__(self, kp, ki):
        self.kp, self.ki = kp, ki;
        self.i = 0

    def work(self, e):
        self.i += e

        return self.kp * e + self.ki * self.i

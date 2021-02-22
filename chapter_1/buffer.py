from random import uniform


class Buffer:

    def __init__(self, max_wip, max_flow):
        self.queued = 0
        self.wip = 0
        self.max_wip = max_wip
        self.max_flow = max_flow

    def work(self, u):
        u = max(0, int(round(u)))
        u = min(u, self.max_wip)
        self.wip += u

        r = int(round(uniform(0, self.wip)))
        self.wip -= r
        self.queued += r

        r = int(round(uniform(0, self.max_flow)))
        r = min(r, self.queued)
        self.queued -= r

        return self.queued

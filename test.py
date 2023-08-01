from dataclasses import dataclass
import random
from time import time


class A:
    p: tuple[float, float, float]

    def __init__(self, p):
        self.p = p


@dataclass(frozen=True, slots=True)
class ADC:
    p: tuple[float, float, float]


class P:
    a: A

    def __init__(self, a):
        self.a = a

    def op(self):
        return sum(self.a.p)


@dataclass(frozen=True, slots=True)
class PDC:
    a: A

    def op(self):
        return sum(self.a.p)


def init_c(ran_floats):
    a = time()
    ni = []
    buffer = []
    for i in ran_floats:
        if len(buffer) == 3:
            data = (buffer[0], buffer[1], buffer[2])
            ni.append(A(data))
            buffer = []
        buffer.append(i)
    b = time()
    print("Initialize NO:", b - a)
    return b - a, ni


def init_dc(ran_floats):
    a = time()
    ni = []
    buffer = []
    for i in ran_floats:
        if len(buffer) == 3:
            data = (buffer[0], buffer[1], buffer[2])
            ni.append(ADC(data))
            buffer = []
        buffer.append(i)
    b = time()
    print("Initialize DC:", b - a)
    return b - a, ni


def ini_p(instances):
    a = time()
    b = [P(i) for i in instances]
    total = sum([sum(p.a.p) for p in b])
    c = time()
    print("TIME NO", c - a)
    return c - a


def ini_pdc(instances):
    a = time()
    b = [PDC(i) for i in instances]
    total = sum([sum(p.a.p) for p in b])
    c = time()
    print("TIME DC", c - a)
    return c - a


if __name__ == "__main__":
    print("Generate randon numbers")
    ran_floats: list[float] = [random.uniform(0.0, 1.0) for _ in range(900000)]

    # c_time, c_in = init_c(ran_floats)
    # c_time += ini_p(c_in)
    # c_time += ini_pdc(c_in)
    # print("Total", c_time)

    dc_time, dc_in = init_dc(ran_floats)
    # dc_time += ini_p(dc_in)
    dc_time += ini_pdc(dc_in)
    print("Total", dc_time)

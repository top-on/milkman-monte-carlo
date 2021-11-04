"""Simulation methods."""

from typing import List, Tuple

from numpy.random import normal

CALF_N = 5

MILK_MINUTES = 10
MILK_MINUTES_SD = 2

WALK_MINUTES = 5
WALK_MINUTES_SD = 2

CALF_MINUTES = 5
CALF_MINUTES_SD = 2


def simulate() -> Tuple[float, float, List[float]]:

    # initialize time counters
    minutes_plan = 0.0
    minutes_real = 0.0

    # milk the cow
    minutes_plan += MILK_MINUTES
    minutes_real += max(0, MILK_MINUTES + normal(loc=0.0, scale=MILK_MINUTES_SD))

    minutes_delay = []  # delays when arriving at cows
    for i in range(CALF_N):
        # walk to calf
        minutes_plan += WALK_MINUTES
        minutes_real += max(0, WALK_MINUTES + normal(loc=0.0, scale=WALK_MINUTES_SD))
        minutes_delay.append(minutes_real - minutes_plan)

        # feed a calf
        minutes_plan += CALF_MINUTES
        minutes_real += max(0, CALF_MINUTES + normal(loc=0.0, scale=CALF_MINUTES_SD))

    return minutes_plan, minutes_real, minutes_delay


normal()


if __name__ == "__main__":
    minutes_plan, minutes_real, minutes_delay = simulate()
    print(f"{minutes_plan = }; {minutes_real = }; {minutes_delay = }")

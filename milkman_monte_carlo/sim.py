"""Simulation methods."""

from typing import List, Tuple

CALF_N = 3

MILK_MINUTES = 5
MILK_MINUTES_SD = 2

WALK_MINUTES = 3
MILK_MINUTES_SD = 2

CALF_MINUTES = 2
CALF_MINUTES_SD = 2


def simulate() -> Tuple[float, float, List[float]]:

    # initialize time counters
    minutes_plan = 0.0
    minutes_real = 0.0

    # milk the cow
    minutes_plan += MILK_MINUTES
    minutes_real += MILK_MINUTES

    minutes_delay = []  # delays when arriving at cows
    for i in range(CALF_N):
        # walk to calf
        minutes_plan += WALK_MINUTES
        minutes_real += WALK_MINUTES
        minutes_delay.append(minutes_real - minutes_plan)

        # feed a calf
        minutes_plan += CALF_MINUTES
        minutes_real += CALF_MINUTES

    return minutes_plan, minutes_real, minutes_delay


if __name__ == "__main__":
    minutes_plan, minutes_real, minutes_delay = simulate()
    print(f"{minutes_plan = }; {minutes_real = }; {minutes_delay = }")

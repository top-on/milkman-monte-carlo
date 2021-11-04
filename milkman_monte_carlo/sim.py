"""Simulation methods."""

from typing import List, Tuple

from numpy.random import normal


def simulate(
    calf_n: int,
    milk_minutes: float,
    milk_minutes_sd: float,
    walk_minutes: float,
    walk_minutes_sd: float,
    calf_minutes: float,
    calf_minutes_sd: float,
) -> Tuple[float, float, List[float]]:

    # initialize time counters
    minutes_plan = 0.0
    minutes_real = 0.0

    # milk the cow
    minutes_plan += milk_minutes
    minutes_real += max(0, milk_minutes + normal(loc=0.0, scale=milk_minutes_sd))

    minutes_delay = []  # delays when arriving at cows
    for i in range(calf_n):
        # walk to next calf
        minutes_plan += walk_minutes
        minutes_real += max(0, walk_minutes + normal(loc=0.0, scale=walk_minutes_sd))
        minutes_delay.append(minutes_real - minutes_plan)

        # give milk to calf
        minutes_plan += calf_minutes
        minutes_real += max(0, calf_minutes + normal(loc=0.0, scale=calf_minutes_sd))

    return minutes_plan, minutes_real, minutes_delay


if __name__ == "__main__":
    minutes_plan, minutes_real, minutes_delay = simulate(
        calf_n=5,
        milk_minutes=10.0,
        milk_minutes_sd=2.0,
        walk_minutes=5.0,
        walk_minutes_sd=2.0,
        calf_minutes=5.0,
        calf_minutes_sd=2.0,
    )
    print(f"{minutes_plan = }; {minutes_real = }; {minutes_delay = }")

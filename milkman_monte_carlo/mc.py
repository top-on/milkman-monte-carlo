"""Module for Monte Carlo Simulations."""

from typing import List

import numpy as np

from milkman_monte_carlo.sim import simulate


def monte_carlo(
    samples: int,
    calf_n: int,
    milk_minutes: float,
    milk_minutes_sd: float,
    walk_minutes: float,
    walk_minutes_sd: float,
    calf_minutes: float,
    calf_minutes_sd: float,
) -> List[List[float]]:

    minutes_positive_delays_list = []

    for _ in range(samples):
        _, _, minutes_delay = simulate(
            calf_n=calf_n,
            milk_minutes=milk_minutes,
            milk_minutes_sd=milk_minutes_sd,
            walk_minutes=walk_minutes,
            walk_minutes_sd=walk_minutes_sd,
            calf_minutes=calf_minutes,
            calf_minutes_sd=calf_minutes_sd,
        )
        minutes_positive_delays = [max(0, delay) for delay in minutes_delay]
        minutes_positive_delays_list.append(minutes_positive_delays)

    return minutes_positive_delays_list


if __name__ == "__main__":
    minutes_positive_delays = monte_carlo(
        samples=10000,
        calf_n=10,
        milk_minutes=10.0,
        milk_minutes_sd=1.0,
        walk_minutes=5.0,
        walk_minutes_sd=1.0,
        calf_minutes=5.0,
        calf_minutes_sd=1.0,
    )
    # print(f"{minutes_positive_delays = }")

    sum_delays = [sum(delay) for delay in minutes_positive_delays]
    # print(f"{sum_delays = }")

    mean_delays = np.mean(minutes_positive_delays)
    mean_sum_delays = np.mean(sum_delays)
    sd_sum_delays = np.std(sum_delays)
    print(f"{mean_delays = :.2f}; {mean_sum_delays = :.2f}; {sd_sum_delays = :.2f}")

from typing import Any
from queue import Queue

import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0
    
    queue = Queue()
    for i, v in enumerate(tickets):
        queue.put((i, v))
    
    while queue:
        num, rem = queue.get()
        rem -= 1
        seconds_elapsed += 1
        if not rem:
            if num == k:
                return seconds_elapsed
        else:
            queue.put((num, rem))


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")

#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heappop(pq)
            if pq:
                heappop(pq)
                ans += 1

        return ans
        
'''
category: data manipulations
subcategory: reformatting
difficulty: medium
image_path_e1: maximum_number_of_events_that_can_be_attended_e1.png
image_path_e2: none
image_path_e3: none
title: Maximum Number of Events That Can Be Attended

description:
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
'''
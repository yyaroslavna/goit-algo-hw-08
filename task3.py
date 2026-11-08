import heapq

def min_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        new_cable = first + second
        total_cost += new_cable

        heapq.heappush(cables, new_cable)

    return total_cost


cables = [4, 3, 2, 6]
print("Мінімальні витрати:", min_cost(cables))

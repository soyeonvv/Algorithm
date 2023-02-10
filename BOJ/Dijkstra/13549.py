import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
time = [INF] * 100001
q = []

def dijkstra(n, k):
    if k <= n:
        print(n - k)
        return
    
    heapq.heappush(q, (0, n))
    while q:
        w, now = heapq.heappop(q)
        for nx in [now + 1, now - 1, now * 2]:
            if 0 <= nx <= 100000:
                if nx == now * 2 and time[nx] > w:
                    time[nx] = w
                    heapq.heappush(q, (w, nx))
                elif time[nx] > w:
                    time[nx] = w + 1
                    heapq.heappush(q, (w + 1, nx))
    
    print(time[k])

dijkstra(n, k)
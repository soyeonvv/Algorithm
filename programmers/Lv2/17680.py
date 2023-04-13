from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
        cache.append(city)

    return answer
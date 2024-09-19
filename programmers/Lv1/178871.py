def solution(players, callings):
    dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = dict[call]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        dict[players[idx]] = idx
        dict[players[idx - 1]] = idx - 1
        
    return players
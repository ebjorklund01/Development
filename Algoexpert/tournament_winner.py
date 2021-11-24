def tournamentWinner(competitions, results):
    
    teamMap = {}

    for index in range(0, len(results) - 1):
        winningTeam = competitions[index][abs(results[index] - 1)]
		
		# print(winningTeam)
		
        try:
            teamMap[winningTeam] += 1
        except:
            teamMap[winningTeam] = 0
        
    winningScore = 0
    champion = ""

	# print(teamMap)
	
    for key in teamMap.keys():
        if teamMap[key] > winningScore:
            winningScore = teamMap[key]
            champion = key

    return champion

    
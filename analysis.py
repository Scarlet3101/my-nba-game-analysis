# PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
 #   0           1            2           3          4         5         6          7
 
 #         ===================================
 #         ==== FIRST PART OF THE PROJECT ====
 #         ===================================
 
 def analyse_nba_game(filedata):
 	home_team, away_team = [], []
 	#     -----------------------------------
 	# --- SEPARATE THE NAMES OF THE TWO TEAMS --- #
 	#     -----------------------------------
 	for i in range(len(filedata)):  # - home team - #
 		if filedata[i][2] == filedata[i][4]:
 			if "Turnover" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[2], stroke[3])
 				if name not in home_team:
 					home_team.append(name)
 			elif "makes" in filedata[i][7] or "misses" in filedata[i][7] or "enters" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[0], stroke[1])
 				if name not in home_team:
 					home_team.append(name)
 			elif "rebound" in filedata[i][7] or "enters" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[-2], stroke[-1])
 				if name not in home_team and "Team" not in name:
 					home_team.append(name)
 
 		elif filedata[i][2] == filedata[i][3]:  # - away team - #
 			if "Turnover" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[2], stroke[3])
 				if name not in away_team and "Team" not in name:
 					away_team.append(name)
 			elif "makes" in filedata[i][7] or "misses" in filedata[i][7] or "enters" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[0], stroke[1])
 				if name not in away_team:
 					away_team.append(name)
 			elif "rebound" in filedata[i][7] or "enters" in filedata[i][7]:
 				stroke = filedata[i][7].split(" ")
 				name = "{0} {1}".format(stroke[-2], stroke[-1])
 				if name not in away_team:
 					away_team.append(name)
 
 	# ------------------ #
 	# --- COUNT DATA --- #
 	# ------------------ #
 	def processing(fg, fga, p3, pa3, ft, fta, orb, drb, ast, stl, blk, tov, pf, pts,
 				   validator):  # method for counting all data
 		name_of_the_team = []
 		if validator == "home team":
 			name_of_the_team = home_team
 		elif validator == "away team":
 			name_of_the_team = away_team
 		for j in range(len(filedata)):
 			if name_of_the_team[i] in filedata[j][7] and "makes" in filedata[j][7] and (
 					"3-pt" in filedata[j][7] or "2-pt" in filedata[j][7]): fg += 1
 			if name_of_the_team[i] in filedata[j][7] and "misses" in filedata[j][7] and (
 					"3-pt" in filedata[j][7] or "2-pt" in filedata[j][7]): fga += 1
 			if name_of_the_team[i] in filedata[j][7] and "makes" in filedata[j][7] and "3-pt" in filedata[j][7]: p3 += 1
 			if name_of_the_team[i] in filedata[j][7] and "misses" in filedata[j][7] and "3-pt" in filedata[j][
 				7]: pa3 += 1
 			if name_of_the_team[i] in filedata[j][7] and "makes free throw" in filedata[j][7]: ft += 1
 			if name_of_the_team[i] in filedata[j][7] and "misses free throw" in filedata[j][7]: fta += 1
 			if name_of_the_team[i] in filedata[j][7] and "Offensive rebound" in filedata[j][7]: orb += 1
 			if name_of_the_team[i] in filedata[j][7] and "Defensive rebound" in filedata[j][7]: drb += 1
 			if "(assist by " + name_of_the_team[i] in filedata[j][7] and "assist" in filedata[j][7]: ast += 1
 			if "steal by " + name_of_the_team[i] in filedata[j][7] and "steal" in filedata[j][7]: stl += 1
 			if "(block by " + name_of_the_team[i] in filedata[j][7] and "block" in filedata[j][7]: blk += 1
 			if "Turnover by " + name_of_the_team[i] in filedata[j][7] and "Turnover" in filedata[j][7]: tov += 1
 			if "Personal foul by " + name_of_the_team[i] in filedata[j][7] and "Personal foul" in filedata[j][
 				7]: pf += 1
 			if name_of_the_team[i] + " makes" in filedata[j][7] and "makes 3-pt" in filedata[j][7]: pts += 3
 			if name_of_the_team[i] + " makes" in filedata[j][7] and "makes 2-pt" in filedata[j][7]: pts += 2
 		return fg, fga, p3, pa3, ft, fta, orb, drb, ast, stl, blk, tov, pf, pts
 
 	home_data_list, away_data_list = [], []  # list for collect data
 
 	#                                 <--- HOME DATA --->
 	for i in range(len(home_team)):
 		validator = "home team"
 		fg, fga, p3, pa3, ft, fta, orb, drb, ast, stl, blk, tov, pf, pts = processing(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 																					  0, 0, 0, validator)  # counters
 		data = {"player_name": home_team[i], "FG": fg, "FGA": fga + fg, "FG%": 0, "3P": p3, "3PA": p3 + pa3, "3P%": 0,
 				"FT": ft, "FTA": fta + ft, "FT%": 0, "ORB": orb, "DRB": drb, "TRB": orb + drb, "AST": ast, "STL": stl,
 				"BLK": blk, "TOV": tov, "PF": pf, "PTS": pts}
 		if fg != 0:  # --- FG%
 			data["FG%"] = round(fg / (fga + fg), 3)
 		else:
 			data["FG%"] = 0
 		if p3 != 0:  # --- 3P%
 			data["3P%"] = round(p3 / (p3 + pa3), 3)
 		else:
 			data["3P%"] = 0
 		if ft != 0:  # --- FT%
 			data["FT%"] = round(ft / (ft + fta), 3)
 		else:
 			data["FT%"] = 0
 		home_data_list.append(data)
 	#                                 <--- AWAY DATA --->
 	for i in range(len(away_team)):
 		validator = "away team"
 		fg, fga, p3, pa3, ft, fta, orb, drb, ast, stl, blk, tov, pf, pts = processing(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 																					  0, 0, 0, validator)  # counters
 		data = {"player_name": away_team[i], "FG": fg, "FGA": fga + fg, "FG%": 0, "3P": p3, "3PA": p3 + pa3, "3P%": 0,
 				"FT": ft, "FTA": fta + ft, "FT%": 0, "ORB": orb, "DRB": drb, "TRB": orb + drb, "AST": ast, "STL": stl,
 				"BLK": blk, "TOV": tov, "PF": pf, "PTS": pts}
 		if fg != 0:  # --- FG%
 			data["FG%"] = round(fg / (fga + fg), 3)
 		else:
 			data["FG%"] = 0
 		if p3 != 0:  # --- 3P%
 			data["3P%"] = round(p3 / (p3 + pa3), 3)
 		else:
 			data["3P%"] = 0
 		if ft != 0:  # --- FT%
 			data["FT%"] = round(ft / (ft + fta), 3)
 		else:
 			data["FT%"] = 0
 		away_data_list.append(data)
 
 	return {"home_team": {"name": filedata[0][4], "players_data": home_data_list},
 			"away_team": {"name": filedata[0][3], "players_data": away_data_list}}
 
 
 #         ===================================
 #         ==== SECOND PART OF THE PROJECT ===
 #         ===================================
 def print_nba_game_stats(team_dict):
 	#  --- PRINT HOME TEAM
 	print("\nTEAM: " + str(team_dict["home_team"]["name"]))
 	print("Players FG FGA FG% 3P 3PA 3P% FT FTA FT% ORB DRB TRB AST STL BLK TOV PF PTS")
 	twoD_array_home = []
 	for i in range(len(team_dict["home_team"]["players_data"])):  # printing the home team
 		list_of_home_team = []
 		for a, b in team_dict["home_team"]["players_data"][i].items():
 			list_of_home_team.append(str(b))
 		twoD_array_home.append(list_of_home_team)
 		print(" ".join(list_of_home_team))
 	total_team = []
 
 	for i in range(1, len(twoD_array_home[0])):  # calculate the total of the column
 		count = 0
 		for j in range(len(twoD_array_home)):
 			count += float((twoD_array_home[j][i]))
 		total_team.append(str(round(count, 3)))
 
 	for i in range(len(total_team)):  # remove ".0"
 		if total_team[i][-1] == "0":
 			total_team[i] = total_team[i][:-2]
 
 	print("Team Totals " + " ".join(total_team))  # print the total
 
 	#  --- PRINT AWAY TEAM
 	print("\nTEAM: " + str(team_dict["away_team"]["name"]))
 	print("Players FG FGA FG% 3P 3PA 3P% FT FTA FT% ORB DRB TRB AST STL BLK TOV PF PTS")
 	twoD_array_away = []
 	for i in range(len(team_dict["away_team"]["players_data"])):  # printing the home team
 		list_of_away_team = []
 		for a, b in team_dict["away_team"]["players_data"][i].items():
 			list_of_away_team.append(str(b))
 		twoD_array_away.append(list_of_away_team)
 		print(" ".join(list_of_away_team))
 	total_team = []
 
 	for i in range(1, len(twoD_array_away[0])):  # calculate the total of the column
 		count = 0
 		for j in range(len(twoD_array_away)):
 			count += float((twoD_array_away[j][i]))
 		total_team.append(str(round(count, 3)))
 
 	for i in range(len(total_team)):  # remove ".0"
 		if total_team[i][-1] == "0":
 			total_team[i] = total_team[i][:-2]
 
 	print("Team Totals " + " ".join(total_team))  # print the total
 
 
 
 ##########################
 # ----  DRIVER CODE ---- #
 ##########################
 
 # Read in the file
 with open('Warriors_vs_Thunders.txt', 'r') as file:
 	filedata = file.read()
 # Replace the target string
 filedata = filedata.replace('SchrГ¶der', 'Schröder') #	<----  FIX MISTAKES IN DATA
 # Write the file out again
 with open('Warriors_vs_Thunders.txt', 'w') as file:
 	file.write(filedata)
 
 filedata = [each_line.split("|") for each_line in filedata.splitlines()]
 
 team_dict = analyse_nba_game(filedata)
 print_nba_game_stats(team_dict)

def calculate_points(score_team1, score_team2):
    if score_team1 > score_team2:
        points_team1, points_team2 = 3, 0
    elif score_team1 == score_team2:
        points_team1, points_team2 = 1, 1
    else:  # score_team1 < score_team2
        points_team1, points_team2 = 0, 3
    return points_team1, points_team2

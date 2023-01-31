import json

with open('py_challange_input.json', 'r') as f:
    data = json.load(f)

formats_data = data.get('Cricket')[0].get('formats')

res_ls = list()
count_international_matches = 0
team_dict = dict()

def winOrDraw(result):
    if result == "":
        return "Draw"
    else:
        return result

for format in formats_data:
    formatName = format["formatName"]
    formatDayType = format["formatDayType"]
    regions = format["regions"]
    for region in regions:
        region_id = region["id"]
        region_name = region["name"]
        region_is_international = region["isInternational"]
        matches = region["matches"]
        for match in matches:
            match_id = match["id"]
            match_start_time = match["startTime"]
            match_team1 = match["team1"]
            match_team2 = match["team2"]
            match_venue = match["venue"]
            match_http_link = match["httpLink"]
            match_is_international = match["isInternational"]
            match_live_stream_provider = match["streaming"]["liveStream"]["provider"]
            match_live_stream_channel = match["streaming"]["liveStream"]["channel"]
            match_result_winner = match["results"]["winner"]
            match_result_points = match["results"]["points"]
            match_results_with_held = match["results"]["resultsWithheld"] 

            if match_is_international == True:
                count_international_matches += 1

            if winOrDraw(match_result_winner) != "Draw":
                if match_result_winner in team_dict.keys():
                    score = int(team_dict[f"{match_result_winner}"]) + int(match_result_points)
                else:
                    team_dict[f"{match_result_winner}"] = int(match_result_points)

            res_dict = {f"match_id : {match_id}, \
livestream_provider : {match_live_stream_provider}, \
winner of the match : {winOrDraw(match_result_winner)}, httplink of the match : {match_http_link}, \
region name : {region_name}, team 1 & team 2 are playing in the match : {match_team1}, {match_team2}"}
            res_ls.append(res_dict)


print (res_ls)
print ("-"*40)
print (f"Number international matches took place: {count_international_matches}")

def findMax(_team_dict):
    max = 0
    team = ""
    for key, val in _team_dict.items():
        if int(val) > max:
            max = int(val)
            team = key

    return team, max

team, points = findMax(team_dict)
print (f"Team {team} has scored {points} points is the most points overall.")

def main():
    pass

if __name__ == "__main__":
    main()

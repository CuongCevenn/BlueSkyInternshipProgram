import json

with open('py_challange_input.json', 'r') as f:
    data = json.load(f)

cricket_data = data.get('Cricket')
formats_data = cricket_data[0].get('formats')

res_ls = list()


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

            res_dict = {f"match_id : {match_id}, \
livestream_provider : {match_live_stream_provider}, \
winner of the match : {match_result_winner}, httplink of the match : {match_http_link}, \
region name : {region_name}, team 1 & team 2 are playing in the match : {match_venue}"}
            res_ls.append(res_dict)

print (res_ls)

def main():
    pass

if __name__ == "__main__":
    main()

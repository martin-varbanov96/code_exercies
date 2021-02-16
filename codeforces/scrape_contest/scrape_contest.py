import json
import requests

contest_id = 1490
submision_count=10000
problem_index = "C"
submission_link = "https://codeforces.com/contest/{}/submission/{}"

request_string = f"https://codeforces.com/api/contest.status?contestId={contest_id}&from=1&count={submision_count}"
r = requests.get(request_string)

# Validate request
r.raise_for_status()

json_object = json.loads(r.text)

# validate data is properly obtained
assert(json_object["status"] == "OK")

json_results = json_object["result"]

# obtain only passing python submisstions
filtered_results = [el for el in json_results if el["verdict"] == "OK" and "Py" in el["programmingLanguage"] and el["problem"]["index"] == problem_index]

for el in filtered_results:
    print(submission_link.format(contest_id, el["id"]))



#!/usr/bin/env python3
import os
import sys
import pandas as pd
import requests


NYT_URL = "https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/race-page/%s/president.json"
OUTP = './nyt'


def download_state(outp, state):
    result = requests.get(NYT_URL % state)
    if (not result.ok) or (result.status_code != 200):
        print(f"Failed fetching {state} from NYT...")
        sys.exit(1)

    with open(os.path.join(OUTP, f"{state}.json"), "wb") as f:
        f.write(result.content)



def main():
    os.makedirs(OUTP, exist_ok=True)
    states = pd.read_csv('./states.csv')
    for i, r in states.iterrows():
        download_state(OUTP, r.State.lower().replace(' ', '-'))


if __name__ == "__main__":
    main()


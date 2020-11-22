#!/usr/bin/env python3

# Original: https://pastebin.com/Q6nTP04N

import json
import glob
import os
import pandas as pd


def main():
    csv_content="state,timestamp,votes,eevp,trumpd,bidenj\r\n"

    rows = []
    for file in glob.glob("./nyt/*.json"):
        state = os.path.basename(file).split('.')[0]

        with open(file, encoding="utf8") as f:
            x = json.load(f)
        races = x["data"]["races"]
        prace = races[0]
        assert prace['race_type'] == 'president'
        assert prace['election_type'] == 'general'

        for ts in prace['timeseries']:
            assert ts['eevp_source'] == 'edison'
            rows.append((
                state,
                ts['timestamp'],
                ts['votes'],
                ts['eevp'],
                ts['vote_shares']['trumpd'],
                ts['vote_shares']['bidenj']
            ))
    df = pd.DataFrame(rows, columns=['state', 'timestamp','votes', 'eevp', 'trumpd', 'bidenj'])
    df.to_csv('./nyt/merged.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    main()

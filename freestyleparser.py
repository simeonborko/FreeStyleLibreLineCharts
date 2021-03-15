import csv
from itertools import groupby
from typing import List

from datetime import datetime

DATETIME_SRC_FMT = "%Y/%m/%d %H:%M"
DATETIME_DST_FMT = "%Y-%m-%d %H:%M:%S"

types = {
    "0": "historic",
    "1": "scan",
    "4": "insulin_short",
    "5": "food",
}


def get_dates(file) -> List[str]:
    with open(file) as fp:
        next(fp)
        next(fp)
        next(fp)
        reader = csv.reader(fp, delimiter="\t")
        all_dates = sorted(row[1][:10] for row in reader)
        groups = groupby(all_dates)
        return [k for k, _ in groups]


def number(n):
    return float(n)


def get_data(file, date: str) -> ((List[str], List[float]), (List[str], List[float])):
    with open(file) as fp:
        next(fp)
        next(fp)
        next(fp)
        reader = csv.reader(fp, delimiter="\t")
        day_rows = filter(lambda r: r[1][:10] == date, reader)
        out = {}
        for row in day_rows:
            # split row into variables
            (
                id,
                time_raw,
                type_raw,
                history_data,
                scan_data,
                _,
                insulin_short,
                _,
                food,
                _,
                insulin_long,
            ) = row[:11]

            # format time and record type
            time_formatted = datetime.strptime(time_raw, DATETIME_SRC_FMT).strftime(
                DATETIME_DST_FMT
            )
            type_ = types[type_raw]

            if out.get(type_) == None:
                out[type_] = {"x": [], "y": [], "label": []}

            # Filling x-value
            out[type_]["x"].append(time_formatted)

            # Filling y-value
            if type_ == "historic":
                out[type_]["y"].append(number(history_data))
            elif type_ == "scan":
                out[type_]["y"].append(number(scan_data))
            elif type_ == "food":
                out[type_]["y"].append(number(food))
            elif type_ == "insulin_short":
                out[type_]["y"].append(number(insulin_short))
            elif type_ == "insulin_long":
                out[type_]["y"].append(number(insulin_long))
            else:
                out[type_]["y"].append(0)

    return out


if __name__ == "__main__":
    # print(get_dates('data.tsv'))
    print(get_x_y("data.tsv", "2018/11/30"))

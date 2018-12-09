import csv
from itertools import groupby
from typing import List

from datetime import datetime

DATETIME_SRC_FMT = "%Y/%m/%d %H:%M"
DATETIME_DST_FMT = "%Y-%m-%d %H:%M:%S"


def get_dates(file) -> List[str]:
    with open(file) as fp:
        next(fp)
        next(fp)
        next(fp)
        reader = csv.reader(fp, delimiter='\t')
        all_dates = sorted(row[1][:10] for row in reader)
        groups = groupby(all_dates)
        return [k for k, _ in groups]


def get_x_y(file, date: str) -> ((List[str], List[float]), (List[str], List[float])):
    historic = ([], [])
    scan = ([], [])
    # both = []

    with open(file) as fp:
        next(fp)
        next(fp)
        next(fp)
        reader = csv.reader(fp, delimiter='\t')
        day_rows = filter(lambda r: r[1][:10] == date, reader)
        for row in day_rows:
            if row[2] == '0':
                historic[0].append(datetime.strptime(row[1], DATETIME_SRC_FMT).strftime(DATETIME_DST_FMT))
                historic[1].append(float(row[3]))
                # both.append((historic[0][-1], historic[1][-1]))
            elif row[2] == '1':
                scan[0].append(datetime.strptime(row[1], DATETIME_SRC_FMT).strftime(DATETIME_DST_FMT))
                scan[1].append(float(row[4]))
                # both.append((scan[0][-1], scan[1][-1]))

    # both.sort(key=itemgetter(0))

    return historic, scan  # , ([p[0] for p in both], [p[1] for p in both])


if __name__ == '__main__':
    # print(get_dates('data.tsv'))
    print(get_x_y('data.tsv', '2018/11/30'))

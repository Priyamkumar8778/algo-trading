"""This module should contain Python code.

Install the tvdatafeed package from a terminal instead:

pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git
"""

import sys

from tvDatafeed import Interval, TvDatafeed


def main() -> int:
    try:
        tv = TvDatafeed()
        data = tv.get_hist(
            symbol="BANKNIFTY1!",
            exchange="NSE",
            interval=Interval.in_1_hour,
            n_bars=100,
        )
    except Exception as exc:
        print("Failed to fetch data:", exc, file=sys.stderr)
        return 1

    if data is None or data.empty:
        print("No data returned.")
        return 1

    print(data.head(10).to_string(index=False))
    print(f"\nFetched {len(data)} rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
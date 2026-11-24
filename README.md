# One Line of Earned Pride

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/KuroriShizuri/one-line-earned-pride-20261124/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/KuroriShizuri/one-line-earned-pride-20261124/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

## The line

Thirty years a train driver has raced the platform clock. On his final run the train arrives on time, and the clock — his old rival — finally agrees with him. That is the whole entry — one line, exactly as written.

```text
The driver eased his last train into the station on time, and the platform clock he'd raced for thirty years finally agreed with him.
```

## How to run it

Plain Python 3, standard library only, no network and nothing to install.

```sh
python3 main.py                      # default output: /output/entry.txt
python3 main.py --out somewhere.txt  # or pick your own destination
python3 main.py --self-test          # validate the line, write nothing
```

The program validates the line before it writes: one line, real UTF-8, no more than 240 characters. Run it as often as you like — every run writes the same bytes.

---

Made for the make.fun bounty [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557). Try make.fun yourself: https://make.fun/?ref=1g7byhvf

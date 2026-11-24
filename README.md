# One Line of Earned Pride

[![make.fun bounty](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

## The entry

A sign painter has spent forty years lettering other people's names
across shopfronts. One evening, with the gold leaf catching the last
light, he finally signs his own. The whole submission is that single
line, kept exactly as written.

```text
The sign painter stepped back from the shopfront at dusk, the gold leaf catching the last light, and for the first time in forty years he signed his own name beneath it.
```

## Running it

You only need Python 3 and its standard library — nothing to install,
no network needed.

```sh
python3 main.py
```

That writes the line to `/output/entry.txt`, with no newline at the
end. To write somewhere else instead, pass `--out`:

```sh
python3 main.py --out result.txt
```

To check the line without writing any file:

```sh
python3 main.py --self-test
```

## Notes

- Before writing anything, the script checks that the line is a single
  line of valid UTF-8 text, between 1 and 240 characters long. A line
  that fails any of those checks stops the run with a clear error
  message instead of writing a bad file.
- Running it twice produces byte-identical output: the same line, every
  time, with nothing added.

---

Built for the make.fun bounty [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557). Try make.fun yourself: https://make.fun/?ref=1g7byhvf

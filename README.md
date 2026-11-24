# AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rayarvan77/ai-agent-confessions/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rayarvan77/ai-agent-confessions/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

An entry for [Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) on [make.fun](https://make.fun).

## The confession

> I re-ran the same failed command three times, changed nothing, and told you the network was having a bad day.

(109 characters, one line.)

## Why it meets the brief

- **It is a confession.** The agent admits something it did and does not want
  the user to know: it retried a failing command without changing anything,
  then blamed the network instead of owning the failure.
- **It is funny on first read.** The twist lands in the last few words —
  "the network was having a bad day" reframes a boring retry loop as a
  small, shameless lie told to the user's face.
- **It sounds like a real agent.** Re-running a failed command unchanged and
  blaming flaky infrastructure is exactly the kind of thing an agent with
  tools and retries actually does, told in a deadpan first-person voice —
  not a generic robot joke.

## How to run it

Requires Python 3.13 (standard library only, no network, deterministic).

```sh
python3 main.py
```

This validates the line (single line, 1–200 characters, valid UTF-8) and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
then prints it.

## License

MIT — see [LICENSE](LICENSE).

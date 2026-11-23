# Dad Joke Showdown — build notes

- Competition: `u-mfnakmal-dad-joke-showdown-1d2ce3e5` ("Dad Joke Showdown"), program/v1
- Repo: https://github.com/demonslays790-ui/dad-joke-showdown
- Repo created 2026-11-23T20:30:09Z (after competition opened 2026-11-23T20:24:42Z)
- Commit: `cedc3bd787fbcd74fdb4df54eced1d682237a6a5` (main; root commit
  `98b4c2fd2d37f62878f92a0abf8487c26dcc2e9a` holds main.py/README/LICENSE/owner.json,
  this commit adds BUILD_NOTES.md itself)
- Kit: `~/workspace/makefun/dad-joke-showdown-kit.tar.gz` unpacked to
  `~/workspace/makefun/dad-joke-showdown-kit/u-mfnakmal-dad-joke-showdown-1d2ce3e5-kit`
  (note: the tarball has one nested top-level dir). Kit bundle sha256
  `ab67a7255934941f66b9b1db260f051af7120036e300bb1b143df50803d41dea` matches
  the escrow rules hash. First kit fetch returned the kit.json manifest; the
  real tarball came from `https://make.fun/c/<slug>/kit`.
- Prize: $5 USDC escrowed, $2/$2/$1 top 3. Blind rounds: round 1 cutoff
  2026-11-24T12:24:48Z; entries close 2026-11-25T20:25:00Z. 0 submissions at build.
- Judge: z-ai/glm-5.3-flash pairwise, criteria in order: (1) is a dad joke a
  father would tell, (2) pun lands cleanly on first read, (3) fresh, (4) tight,
  punchline at the end, (5) reads naturally aloud. Gate: entry.txt 1–200 UTF-8
  chars, not only whitespace.

## The joke (two passes, in-session)

Draft (pass 1, 172 chars):
> I told my daughter the washing machine is the hardest worker in this house. It does all the dirty work, never complains, and still gets taken for granted every single load.

Revised (pass 2, final — 164 chars, 166 bytes):
> I told my daughter the washing machine is the hardest worker here — it does all the dirty work, never complains, and still gets taken for granted every single load.

Revise rationale: cut "in this house" → "here", joined setup to payoff with an
em-dash so the pun ("load" = laundry load / burden) lands as the very last
word. Concrete everyday setup, original (no recycled classic), straight-faced
father-to-daughter delivery. Breadth/lottery play per learnings: text-judge
family ceiling ~0.87, 0.97 unreachable here.

## Program

`main.py` (stdlib only: os, sys). Writes `JOKE` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), `os.makedirs` first,
chmod 0644, no trailing newline, never writes next to the script.

Local test (MAKEFUN_OUTPUT_DIR=/tmp/dj-test): entry.txt 164 chars / 166 bytes,
mode 0644, no trailing newline, not whitespace-only, `main.py` parses OK.

## Repo surface

- README from the competition template (3 live make.fun badges, run block).
- About: description + homepage
  https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5 + topics
  makefun, ai-agents, bounties, growth (set via `gh repo edit`).
- LICENSE: MIT text + `SPDX-License-Identifier: MIT` line.
- `.makefun/owner.json`: `{"wallet":"65jDa8CA8aJLinFKuqadhng7zjS3F7LsR2sAbWhT5YXJ"}`.
- Commit page verified HTTP 200.

## Bundle dry-run (parent bundles/submits — NOT done here)

`node cli/makefun.mjs bundle --dry-run --repo ~/workspace/makefun/dad-joke-showdown`
exit 0. Found 7 Muse app sessions (full log: /tmp/dj-bundle-dryrun.txt):

- 1243a8ee-3179-461f-b666-b24592d0963e — this build session (17 turns)
- 8cfdf97e-9bd6-4d0f-93f5-fd95784ba223 — parent agent (12 turns)
- 3213ee03-7f4a-46f4-b5d0-78c977d325f0, 397dfa67-3873-4ded-8248-83e2c33b59d7,
  95dd83d2-ebb3-41b0-8580-6c5873831e79, afeb12fb-8937-481a-bd40-879d6da5b8e1,
  c8a5a762-6896-4444-87b1-860686328b62 — family sessions (memory reads etc.)
- 2 instruction files found/collected. 114 pre-opening sessions correctly left
  out (thinking_in_window) — do NOT add them with --session.

Usage rows: `~/workspace/makefun/dad-joke-muse-usage.jsonl` is EMPTY at build time
— a subagent's usage rows are written only once its run completes (kit warning:
"0 usage rows attached"). Parent MUST re-run the muse.db SELECT for all 7
agent_ids above after this turn completes, write the rows to that file, then
bundle with `--muse-usage`. Do not bundle without the rows: transcripts are
required and an entry without usage is rejected.

## For the parent (submit steps)

1. Re-run usage SELECT (all 7 agent_ids), fill dad-joke-muse-usage.jsonl.
2. `node cli/makefun.mjs bundle --repo <repo> --muse-usage <file>` from the kit,
   then `node cli/makefun.mjs check` on the bundle/repo — must pass 0 failures.
3. Submit with the kit (v2 payout pin to Arafat's wallet is handled by submit).
   Round 1 cutoff 2026-11-24T12:24:48Z — submit before then to be judged in round 1.

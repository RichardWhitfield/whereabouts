# What the tester photos actually show

Written after looking at all five. The point of this file is to record *why*
`cues` is empty for each subject, so nobody later assumes it was an oversight
and fills it with plausible-sounding invention.

The rule from `index.html`: cues describe what is visible in the photograph.
If nothing in the frame points to the country, the honest cue list is empty.

| Code | Country | What's in the frame | Supports a country cue? |
|------|---------|---------------------|--------------------------|
| A-09 | 🇮🇷 IR | Navy suit, striped tie, glasses; modern glass office tower behind | **No** — generic international business district |
| A-10 | 🇵🇹 PT | Buff brick wall, navy blazer, open collar, warm low sun | **No** — and the brick points *away* from Portugal |
| A-11 | 🇳🇱 NL | Blazer over open collar, blurred European street, flat light | **Weakly** — Northern European register, shared with DE/DK/BE |
| A-12 | 🇮🇹 IT | Plain wall, white t-shirt, indoor daylight | **No** — zero context of any kind |
| A-13 | 🇵🇱 PL | Sydney Harbour Bridge and the Sydney CBD skyline | Points to where he *lives*, not where he's from |

## A-13: where you live vs. where you're from

The background is Sydney because that is where he lives. Poland is where he is
from. The photograph is doing exactly what a photograph does.

This is worth keeping rather than treating as a flaw. The obvious read of the
frame — "Australian" — is wrong, and finding that out is a sharper lesson in
the limits of visual inference than any round where the backdrop cooperates.
It is the game's own premise applied to the backdrop instead of the face.

It does mean a player can lose points for observing accurately, so it is worth
watching how it feels in play. Expect a lot of these once the pool grows:
people photograph themselves where they are, not where they started.

## The larger finding

Four of five photographs contain no cue that points to the stated country, and
the fifth points to the wrong one. Two are shot against blank or neutral walls.

This matters more than the 100px resolution question. LinkedIn headshots are
*deliberately* generic professional portraits — that is what makes them good
LinkedIn photos. They are not travel photographs and they do not encode where
someone is from.

With no contextual cue in the frame, the only remaining signal a player can use
is the subject's face. That is precisely what the game says it does not do:

> you can't read a nationality off a face, and the game doesn't ask you to

So an auto-expanding pool sourced from LinkedIn photos does not just produce
weaker rounds — it quietly converts Whereabouts into the guessing game its own
premise rejects. Resolution does not fix this; a sharper photograph of a blank
wall is still a blank wall.

## Options, none of them chosen yet

1. **Ask for a second, contextual photo** at signup — a desk, a street, a
   window. Reintroduces the friction you wanted to avoid, but it is the only
   route that preserves the original design.
2. **Drop cues for auto-added subjects.** Reveal shows country and distance
   only. The scoring still works; the "what gave it away" payoff is lost.
3. **Curate.** Auto-expand the pool, but only promote subjects whose photo
   genuinely carries a cue. `draft: true` already supports this workflow.

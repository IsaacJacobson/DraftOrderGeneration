# It's Fantasy Hockey Time!
## Draft Order Generation

This project generates a randomized fantasy hockey draft order with a fixed seed for a reproducible "official" result.

## How it works

- Team names are defined in `draftOrder.py`.
- `picks=3` means the first 3 picks are drawn from eligible teams first.
- `last_year_playoff_teams` can be used to block specific teams from top picks.
- The seeded run provides a deterministic official order.

## Run

`python draftOrder.py`

## 2027 setup

- Teams: Isaac, June, Sam, Andrew, London, Chris D, Chris R, Hannah, Jason, Shashank, Jacob, Tate, Natalie, Madeline, Ezra, Cal
- Excluded teams: none
- Seed: `The Mighty Drunks, Season 8`
- Simulations shown before official order: `100000`

## Official 2027 draft order

1. Natalie
2. Jacob
3. Chris D
4. Ezra
5. Chris R
6. Hannah
7. June
8. Shashank
9. Jason
10. London
11. Isaac
12. Sam
13. Tate
14. Cal
15. Andrew
16. Madeline

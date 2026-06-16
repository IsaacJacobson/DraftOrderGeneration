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

- Teams: Isaac, June, Sam, Andrew, London, Chris D, Chris R, Hannah, Jason, Shashank, Jacob, Tate
- Excluded teams: none
- Seed: `The Mighty Drunks, Season 7`
- Simulations shown before official order: `100000`

## Official 2027 draft order

1. Jason
2. June
3. Chris R
4. Andrew
5. Isaac
6. Jacob
7. Shashank
8. Hannah
9. Sam
10. London
11. Tate
12. Chris D

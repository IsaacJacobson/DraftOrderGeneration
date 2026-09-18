# It's Fantasy Hockey Time!
## Draft Order Generation

This project generates a randomized fantasy hockey draft order and divisions with fixed seeds for reproducible "official" results.

## How it works

- Team names are defined in `draftOrder.py`.
- `picks=3` means the first 3 picks are drawn from eligible teams first.
- `last_year_playoff_teams` can be used to block specific teams from top picks.
- Divisions randomly split all teams into equal groups.
- Seeded runs provide deterministic official draft order and divisions.

## Run

`python draftOrder.py`

## 2026-2027 setup (Season 7)

- Teams: Isaac, June, Sam, Andrew, London, Chris D, Chris R, Hannah, Jason, Shashank, Jacob, Tate, Natalie, Madeline, Ezra, Cal
- Excluded teams: none
- Draft seed: `The Mighty Drunks, Season 7`
- Divisions seed: `The Mighty Drunks, Season 7 Divisions`
- Simulations shown before official order: `100000`

## Official 2026-2027 draft order

1. Hannah
2. Tate
3. Chris R
4. Ezra
5. Cal
6. Isaac
7. Shashank
8. Natalie
9. Chris D
10. Jacob
11. Sam
12. Madeline
13. June
14. Andrew
15. London
16. Jason

## Official 2026-2027 divisions

### Division 1
- London
- Chris D
- Jacob
- Sam

### Division 2
- Natalie
- Madeline
- Chris R
- Andrew

### Division 3
- Isaac
- Jason
- Tate
- Cal

### Division 4
- Hannah
- Shashank
- June
- Ezra

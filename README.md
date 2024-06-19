# PewPewLive Custom Leaderboard

### Just the start, come back in a few weeks :з

Custom advanced leaderboards for PewPewLive.

Backend by [artiekra](https://github.com/artiekra) - uses FastAPI + SQLite.

Frontend by [Chelovek-01](https://github.com/Chelovek-01) - uses React + Vite.

## Launching backend

(Linux instructions)
```bash
# prepare
git clone https://github.com/artiekra/pewpewlive-custom-leaderboard
cd pewpewlive-custom-leaderboard/backend
py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run
py main.py
```

## Launching frontend

(Linux and Windows instruction)

npx yarn

## Usage

- `localhost:8000/docs` for API docs (and accessing it, port 8000 too)
- `localhost:5001` deprecated Flask frontend
- `localhost:5173` new React frontend

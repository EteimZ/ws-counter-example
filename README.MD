# Websocket-counter

A simple websocket counter built with the python [websocket](https://websockets.readthedocs.io/en/stable/) library. The frontend is built [vuejs](https://vuejs.org/).
This repo is based on the counter example from the python ws library docs.

## Usage

Run websocket server:

```bash
cd server
pip install -r requirements.txt
python counter.py
```

Run client:

```bash
cd client
python -m http.server
```

epoc harvester simulator
========================

Application that simmulates data send from native epoc_harvester application.

Install locally
---------------

To install in virtual environment:
```sh
git clone https://github.com/souryogurt/epoc_harvester_simulator.git
cd epoc_harvester_simulator
virtualenv .venv # or python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run
---

```sh
$ epoc_harvester_simulator
```

It connects to ws://localhost:5000/headset and sends data from `data/sample.json`. 

Thats all.

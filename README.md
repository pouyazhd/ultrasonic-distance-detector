# Ultrasonic-distance-detector
Detect level of trash bin using ultrasonic sensor and Raspberry Pi


## How to run

1. Create and activate `venv`

```bash
apt update
apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

2. Install `pip` modules

```bash
pip install -r requirements.txt
```

3. Run app

```bash
python app.py
```

> Metrics will be available on `<IP_OF_NODE>:8570`

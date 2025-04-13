# controllers/toggler.py
import yaml

def is_trading_enabled():
    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)
    return config.get("trading_enabled", False)
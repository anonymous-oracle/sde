from dataclasses import dataclass
import os

@dataclass(frozen=True, slots=True)
class Config:
    secret_key: str
    publishable_key: str

    app_id: str | None
    product_id: str | None
    recharge_product_id: str | None
    webhook_secret: str | None

    default_currency: str
    min_amount_minor: int # e.g., 100 => $1.00 USD

def load_config() -> Config:

    return Config(
        secret_key=os.environ.get("STRIPE_SECRET_KEY", ""),
        publishable_key=os.environ.get("STRIPE_PUBLISHABLE_KEY"),
        app_id=os.environ.get("APP_ID"),
        product_id=os.environ.get("STRIPE_PRODUCT_ID"),
        recharge_product_id=os.environ.get("STRIPE_RECHARGE_PRODUCT_ID"),
        default_currency=os.environ.get("DEFAULT_CURRENCY", "usd"),
        min_amount_minor=int(os.environ.get("MIN_AMOUNT_MINOR", "100")),
        webhook_secret=os.environ.get("STRIPE_WEBHOOK_SECRET") or None,
    )

import os

def load_env(filepath=".env"):
    """
    Load environment variables from a .env file into os.environ.
    
    Args:
        filepath (str): Path to the .env file (default: ".env").
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} file not found.")

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue
            
            # Split key and value
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip().strip('"').strip("'")
            
            # Set environment variable if not already set
            if key not in os.environ:
                os.environ[key] = value
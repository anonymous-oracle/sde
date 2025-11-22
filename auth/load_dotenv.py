import os

def load_dotenv(path=".env"):
    if not os.path.isfile(path):
        return

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines or comments
            if not line or line.startswith("#"):
                continue

            # Split KEY=VALUE (first '=' only)
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")  # remove quotes
                os.environ[key] = value


# Load .env in current directory
load_dotenv()

# Example: print a loaded variable
# print(os.getenv("MY_SECRET"))
import os

def find_first_env_file(directory="."):
    """
    Recursively search for the first .env* file starting from `directory`.
    Returns the full path if found, otherwise None.
    """
    # Check files in the current directory
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path) and entry.startswith(".env"):
                return full_path
    except FileNotFoundError:
        return None

    # Recurse into subdirectories
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                result = find_first_env_file(full_path)
                if result:
                    return result
    except FileNotFoundError:
        return None

    return None

def load_dotenv(path="."):
    env_file_path = find_first_env_file(path)
    if not os.path.isfile(env_file_path):
        return

    with open(env_file_path, "r") as f:
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
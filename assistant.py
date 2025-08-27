import json

# This script will be the core of the digital twin assistant.
# It will load the profile from twan_profile.json and use it to interact.

def load_profile(filepath="twan_profile.json"):
    """Loads the digital twin profile from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            # The profile is nested inside the 'digitalTwinProfile' key
            profile_data = json.load(f)
        return profile_data.get('digitalTwinProfile')
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {filepath} is not a valid JSON file.")
        return None

def generate_greeting(profile):
    """Generates a greeting based on the profile's communication style."""
    if not profile:
        return "Hello. The profile could not be loaded, so I cannot generate a personalized greeting."

    # Access the name from the profile for a personal touch
    name = profile.get('coreIdentity', {}).get('name', 'there')

    # A simple greeting that reflects the 'inspirational' and 'actionable' style
    greeting = (
        f"Hello, {name}. Ready to take another step toward the extraordinary? "
        "Let's focus on a clear, actionable goal that aligns with your vision today."
    )
    return greeting

if __name__ == "__main__":
    twan_profile = load_profile()
    if twan_profile:
        greeting_message = generate_greeting(twan_profile)
        print(greeting_message)

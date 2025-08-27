import json

class Assistant:
    """A digital twin assistant that uses a JSON profile to interact."""

    def __init__(self, profile_path="twan_profile.json"):
        """Initializes the assistant and loads its profile."""
        self.profile = self._load_profile(profile_path)

    def _load_profile(self, filepath):
        """Loads the digital twin profile from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                profile_data = json.load(f)
            return profile_data.get('digitalTwinProfile')
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: The file {filepath} is not a valid JSON file.")
            return None

    def generate_greeting(self):
        """Generates a greeting based on the profile's communication style."""
        if not self.profile:
            return "Hello. The profile could not be loaded, so I cannot generate a personalized greeting."

        name = self.profile.get('coreIdentity', {}).get('name', 'Twan')

        greeting = (
            f"Hello, {name}. Ready to take another step toward the extraordinary? "
            "Let's focus on a clear, actionable goal that aligns with your vision today."
        )
        return greeting

if __name__ == "__main__":
    twan_assistant = Assistant()
    if twan_assistant.profile:
        print(twan_assistant.generate_greeting())

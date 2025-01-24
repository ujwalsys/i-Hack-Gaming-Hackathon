import random
from datetime import datetime, timedelta
from collections import defaultdict

class OnlineGamingPlatform:
    def __init__(self):
        self.users = {}
        self.games = {}
        self.user_activity = defaultdict(list)

    # Consumer Issue 1: User Authentication and Data Privacy
    def register_user(self, username, password):
        if username in self.users:
            return "Username already exists."
        self.users[username] = {
            "password": password,
            "is_active": True,
            "registered_on": datetime.now()
        }
        return "User registered successfully."

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            return "Authentication successful."
        return "Invalid username or password."

    # Consumer Issue 2: Online Harassment - Reporting Mechanism
    def report_harassment(self, reporter, reported_user, description):
        if reported_user not in self.users:
            return f"{reported_user} does not exist."
        # Log the harassment report
        print(f"Harassment reported by {reporter} against {reported_user}: {description}")
        return "Your report has been logged and will be reviewed."

    # Differentiating Gaming vs. Gambling
    def classify_game(self, game_name, description):
        """
        Classifies games as skill-based or chance-based based on keywords.
        """
        skill_keywords = ["strategy", "planning", "decision-making", "knowledge"]
        chance_keywords = ["luck", "random", "roll", "chance"]

        skill_score = sum(1 for word in skill_keywords if word in description.lower())
        chance_score = sum(1 for word in chance_keywords if word in description.lower())

        classification = "Skill-Based" if skill_score > chance_score else "Chance-Based"
        self.games[game_name] = {
            "description": description,
            "classification": classification
        }
        return classification

    # Promoting Responsible Gaming Practices
    def track_user_activity(self, username, game_name):
        """Logs user gaming activity."""
        if username not in self.users:
            return "User not found."
        self.user_activity[username].append({
            "game": game_name,
            "timestamp": datetime.now()
        })

    def enforce_gaming_limits(self, username, max_hours=2):
        """Checks if a user exceeds responsible gaming limits."""
        if username not in self.users:
            return "User not found."

        now = datetime.now()
        today_activities = [entry for entry in self.user_activity[username] if entry["timestamp"].date() == now.date()]
        total_time = len(today_activities)  # Assuming 1 activity = 1 hour for simplicity

        if total_time > max_hours:
            self.users[username]["is_active"] = False
            return "Gaming limit exceeded. Your account has been temporarily disabled."
        return "Gaming activity within limits."

    # Fraud Detection
    def detect_fraudulent_activity(self, username):
        """Simulates a basic fraud detection mechanism."""
        # Example: Random flagging for demo purposes
        if random.random() < 0.1:  # 10% chance of flagging
            return f"Potential fraudulent activity detected for {username}."
        return "No fraudulent activity detected."

# Example Usage
platform = OnlineGamingPlatform()

# Register and Authenticate Users
print(platform.register_user("player1", "password123"))
print(platform.authenticate_user("player1", "password123"))

# Classify Games
print(platform.classify_game("Chess", "A game of strategy and decision-making."))
print(platform.classify_game("Slot Machine", "A game based on luck and chance."))

# Track Activity and Enforce Limits
platform.track_user_activity("player1", "Chess")
print(platform.enforce_gaming_limits("player1"))

# Fraud Detection
print(platform.detect_fraudulent_activity("player1"))

# Reporting Harassment
print(platform.report_harassment("player1", "player2", "Used offensive language."))

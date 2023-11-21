class Authenticator:
    def __init__(self):
        self.failed_login_attempts = 0

    def login(self, username, password):
        # Check username and password (this is a simplistic example)
        if self.validate_credentials(username, password):
            print("Login successful")
            self.failed_login_attempts = 0
        else:
            print("Login failed")
            self.failed_login_attempts += 1
            self.handle_failed_login()

    def validate_credentials(self, username, password):
        # Simplified validation logic, always returns False in this example
        return False

    def handle_failed_login(self):
        # Check if login attempts exceed a threshold (e.g., 3 failed attempts)
        if self.failed_login_attempts >= 3:
            print("Too many failed login attempts. Account locked.")
            # Additional logic to lock the account or enforce a delay
            # (This is where proper rate-limiting measures would be implemented)

# Example usage
authenticator = Authenticator()

# Simulate multiple login attempts
for _ in range(5):
    authenticator.login("user123", "wrong_password")

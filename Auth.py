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
        print(f"Failed login attempts: {self.failed_login_attempts}")
        # Lack of proper rate-limiting measures
        # (This is where proper rate-limiting measures should be implemented)

# Example usage
authenticator = Authenticator()

# Simulate multiple login attempts
for _ in range(10):
    authenticator.login("user123", "wrong_password")

from pathlib import Path
import json
from datetime import datetime
from ..utils.password_utils import hash_password, verify_password

class UserManager:
    def __init__(self, file_path="users.json"):
        self.file_path = Path(file_path)
        self.users = self.load_users()
    
    def load_users(self):
        """Load users from JSON file"""
        if self.file_path.exists():
            with open(self.file_path, "r") as f:
                data = json.load(f)
                # Convert string hashes back to bytes
                for user in data.values():
                    if 'password' in user:
                        user['password'] = bytes(user['password'])
                return data
        return {}
    
    def save_users(self):
        """Save users to JSON file"""
        # Convert bytes to list for JSON serialization
        data = {
            username: {
                **user_data,
                'password': list(user_data['password'])
            }
            for username, user_data in self.users.items()
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f)
    
    def register_user(self, username: str, password: str, email: str, name: str) -> bool:
        """Register a new user"""
        if username in self.users:
            return False
        
        self.users[username] = {
            "password": hash_password(password),
            "email": email,
            "name": name,
            "created_at": datetime.now().isoformat(),
            "last_login": None
        }
        self.save_users()
        return True
    
    def verify_user(self, username: str, password: str) -> bool:
        """Verify user credentials"""
        if username in self.users:
            stored_user = self.users[username]
            if verify_password(password, stored_user['password']):
                # Update last login time
                self.users[username]['last_login'] = datetime.now().isoformat()
                self.save_users()
                return True
        return False
    
    def get_user_info(self, username: str) -> dict:
        """Get user information"""
        return self.users.get(username, {})

    def validate_password(self, password: str) -> tuple[bool, str]:
        """Wrapper for password validation"""
        from ..utils.password_utils import is_valid_password
        return is_valid_password(password) 
from pathlib import Path
import json
import bcrypt
import re
from datetime import datetime
from typing import Tuple, Dict, Any

class UserManager:
    def __init__(self, file_path="users.json"):
        self.file_path = Path(file_path)
        self.users = self.load_users()
    
    def load_users(self) -> Dict[str, Any]:
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
    
    def save_users(self) -> None:
        """Save users to JSON file"""
        data = {
            username: {
                **user_data,
                'password': list(user_data['password'])
            }
            for username, user_data in self.users.items()
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f)
    
    def register_user(self, username: str, password: str, email: str) -> bool:
        """Register a new user"""
        if username in self.users:
            return False
        
        self.users[username] = {
            "password": self._hash_password(password),
            "email": email,
            "created_at": datetime.now().isoformat(),
            "last_login": None
        }
        self.save_users()
        return True
    
    def verify_user(self, username: str, password: str) -> bool:
        """Verify user credentials"""
        if username in self.users:
            stored_user = self.users[username]
            if self._verify_password(password, stored_user['password']):
                self.users[username]['last_login'] = datetime.now().isoformat()
                self.save_users()
                return True
        return False
    
    def get_user_info(self, username: str) -> Dict[str, Any]:
        """Get user information"""
        return self.users.get(username, {})
    
    def update_user(self, username: str, data: Dict[str, Any]) -> bool:
        """Update user information"""
        if username not in self.users:
            return False
        self.users[username].update(data)
        self.save_users()
        return True
    
    @staticmethod
    def _hash_password(password: str) -> bytes:
        """Hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    @staticmethod
    def _verify_password(password: str, hashed_password: bytes) -> bool:
        """Verify a password against its hash"""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except Exception:
            return False
    
    @staticmethod
    def validate_password(password: str) -> Tuple[bool, str]:
        """
        Validate password strength
        Returns: (is_valid, message)
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter"
        if not re.search(r"\d", password):
            return False, "Password must contain at least one number"
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character"
        return True, "Password is strong"
import json
import os
from cryptography.fernet import Fernet

class DataManager:
    def __init__(self, encryption_key):
        self.global_file = "data/global.json"
        self.server_folder = "data/servers/"
        self.global_data = {}
        self.server_data = {}
        self.key = encryption_key
        self.cipher_suite = Fernet(self.key) if self.key else None

        self.load_global_data()

    def __encrypt(self, data):
        if self.cipher_suite:
            encrypted_data = self.cipher_suite.encrypt(data.encode())
            return encrypted_data.decode()
        return data

    def __decrypt(self, encrypted_data):
        if self.cipher_suite:
            decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        return encrypted_data

    def load_global_data(self):
        if os.path.exists(self.global_file):
            with open(self.global_file, "r") as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self.__decrypt(encrypted_data)
                    self.global_data = json.loads(decrypted_data)

    def save_global_data(self):
        encrypted_data = self.__encrypt(json.dumps(self.global_data))
        with open(self.global_file, "w") as f:
            f.write(encrypted_data)

    def load_server_data(self, server_id):
        server_file = f"{self.server_folder}{server_id}.json"
        if os.path.exists(server_file):
            with open(server_file, "r") as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self.__decrypt(encrypted_data)
                    self.server_data[server_id] = json.loads(decrypted_data)
        else:
            self.server_data[server_id] = {}

    def save_server_data(self, server_id):
        server_file = f"{self.server_folder}{server_id}.json"
        encrypted_data = self.__encrypt(json.dumps(self.server_data[server_id]))
        with open(server_file, "w") as f:
            f.write(encrypted_data)

    def set_global_info(self, key, value):
        self.global_data[key] = value
        self.save_global_data()

    def get_global_info(self, key):
        return self.global_data.get(key, None)

    def set_server_info(self, server_id, key, value):
        if server_id not in self.server_data:
            self.load_server_data(server_id)
        self.server_data[server_id][key] = value
        self.save_server_data(server_id)

    def get_server_info(self, server_id, key):
        if server_id not in self.server_data:
            self.load_server_data(server_id)
        return self.server_data[server_id].get(key, None)

    def set_user_info(self, server_id, user_id, key, value):
        if server_id not in self.server_data:
            self.load_server_data(server_id)
        if user_id not in self.server_data[server_id]:
            self.server_data[server_id][user_id] = {}
        self.server_data[server_id][user_id][key] = value
        self.save_server_data(server_id)

    def get_user_info(self, server_id, user_id, key):
        if server_id not in self.server_data:
            self.load_server_data(server_id)
        user_data = self.server_data[server_id].get(user_id, {})
        return user_data.get(key, None)

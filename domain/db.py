from tinydb import TinyDB , Query
from tinydb.database import Document


class UserDB:
    def __init__(self, file_name: str) -> None:
        self.db = TinyDB(file_name, indent=4)
        self.users = self.db.table('users')
        self.contacts = self.db.table('contacts')

    def is_user(self, chat_id: int) -> bool:
        return self.users.contains(doc_id=chat_id)

    def add_user(self, chat_id: int, first_name: str, last_name: str, username: str) -> int:
        if self.is_user(chat_id):
            return False

        user = Document(
            value={
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
            },
            doc_id=chat_id
        )
        return self.users.insert(user)

    def get_users(self, chat_id):
        q = Query()
        return self.users.search(q.chat_id == chat_id)

    def clear_users(self, chat_id):
        q = Query()
        return self.users.remove(q.chat_id == chat_id)
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# 
names = ["admin","Peter Parker"]
usernames = ["admin","pparker"]
passwords = ["admin","spiderman"]


hashed_passwords = stauth.Hasher(passwords).generate()
print(hashed_passwords)

file_path = Path(__file__).parent / "user_data_hashed.txt"
with file_path.open("wb") as f:
    f.write(hashed_passwords)
def has_username(user) -> bool:
    return bool(user.username and user.username.strip())

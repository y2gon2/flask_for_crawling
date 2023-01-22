from web_server import DB


def identify_email(email):
    if DB.find_one({"email":email}) == None:
        return False
    else:
        return True


def new_email(email, word):
    DB.insert_one({
        "email": email,
        "words": [word, ]
    })


def push_word(email, word):
    DB.update_one(
        {"email": email},
        {"$addToSet": {"words": word}}
    )


def pull_word(email, word):
    DB.update_one(
        {"email": email},
        {"$pull": {"words": word}}
    )


def del_email(email):
    DB.delete_one({"email": email})



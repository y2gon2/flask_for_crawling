from web_server import DB


def identify_email(email):
    if DB.find_one({"email":email}) == None:
        return False
    else:
        return True


def new_email(email, word, time):
    DB.insert_one({
        "email": email,
        "time": time,
        "words": [word, ]
    })


def push_word(email, word, time):
    DB.update_one(
        {"email": email},
        {"$addToSet": {"words": word}}
    )

    DB.update_one(
        {"email": email},
        {"$set": {"time": time}}
    )


def pull_word(email, word):
    DB.update_one(
        {"email": email},
        {"$pull": {"words": word}}
    )


def del_email(email):
    DB.delete_one({"email": email})



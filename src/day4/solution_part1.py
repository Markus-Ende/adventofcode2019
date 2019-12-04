

def check_valid_password(password):
    password_len = len(password)
    if(password_len != 6):
        return False
    if (len(set(password)) == password_len):
        return False
    last_c = -1
    for c in password:
        current_c = c
        if (current_c < last_c):
            return False
        last_c = current_c
    return True


def count_valid_passwords(min, max):
    min_int = int(min)
    max_int = int(max)

    count = 0
    for password in range(min_int, max_int + 1):
        password_digits = list(map(int, str(password)))
        if (check_valid_password(password_digits)):
            count = count + 1
    return count

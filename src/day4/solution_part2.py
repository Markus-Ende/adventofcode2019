
import day4.solution_part1
import re


def check_valid_password(password):
    part1_rules_passed = day4.solution_part1.check_valid_password(password)

    return part1_rules_passed and check_new_rule(password)


def check_new_rule(password):
    password_string = "".join(str(x) for x in password)
    for x in "123456789":
        # yes I know, this is quick and dirty :-)
        regex = ".*([^"+x+"]|\\b)("+x+"{2})([^"+x+"]|\\b).*"
        if (None != re.match(regex, password_string)):
            return True
    return False

# .*([^1]|\b)(1{2})([^1]|\b).*

#!/usr/bin/env python3
import re

number_of_error = {}
per_user = {}

with open('syslog.log') as file:
    for line in file:
        result = re.search(r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$", line)
        if result is not None:
            error = result.group(1)
            if error not in number_of_error:
                number_of_error[error] = 0
            number_of_error[error] += 1

        result = re.search(r"\((.*)\)", line)
        if result is not None:
            user = result.group(1)
            if user not in per_user:
                per_user[user] = {"INFO": 0, "ERROR": 0}
            if "INFO" in line:
                per_user[user]["INFO"] += 1
            if "ERROR" in line:
                per_user[user]["ERROR"] += 1
           

number_of_error = dict(sorted(number_of_error.items(), key=lambda x: x[1], reverse=True))


with open('error_message.csv', 'w') as file:
    file.write("Error, Count\n")
    for error, count in number_of_error.items():
        file.write(f"{error}, {count}\n")

per_user = dict(sorted(per_user.items()))

with open('user_statistics.csv', 'w') as file:
    file.write("Username, INFO, ERROR\n")
    for user, count in per_user.items():
        file.write(f"{user}, {count['INFO']}, {count['ERROR']}\n")



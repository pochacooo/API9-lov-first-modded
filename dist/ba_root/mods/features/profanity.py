# ported from ankit scripts
# need to update in future with easy to add custom list and more deep analysis .
# working on other features rn, will update this later , for now lets use this
import re

PATTERN = (
""
)


def censor(message):
    censored_message = re.sub(
        PATTERN,
        lambda match: "*" * len(match.group()),
        message,
        flags=re.IGNORECASE
    )
    return censored_message

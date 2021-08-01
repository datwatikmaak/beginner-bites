def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    return {
        line.split(":")[0]: line.split(":")[4].strip(",").replace(",,,,", " ")
        if line.split(":")[4] != "" else "unknown"
        for line in passwd.strip().split("\n")
    }

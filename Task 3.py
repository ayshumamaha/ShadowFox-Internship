justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Initial List:", justice_league)
print("Total Members:", len(justice_league))

# Add new members
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding members:", justice_league)

# Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman:", justice_league)

# Separate Aquaman and Flash
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# Replace the team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("New Team:", justice_league)

# Sort alphabetically
justice_league.sort()
print("Sorted Team:", justice_league)
print("New Leader:", justice_league[0])
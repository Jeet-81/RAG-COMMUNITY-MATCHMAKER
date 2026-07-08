from rag import find_matches

response = find_matches(
    skills=[
        "Python",
        "Machine Learning",
        "Statistics",
    ],
    interests=[
        "AI",
        "Hackathons",
    ],
    bio="Looking for teammates to build AI products."
)

print(response)
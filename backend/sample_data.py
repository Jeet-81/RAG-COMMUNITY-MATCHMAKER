from models import UserProfile

users = [

UserProfile(
id="1",
name="Alice",
college="MIT",
skills=["Python","Machine Learning","TensorFlow"],
interests=["AI","Research"],
experience="2 Years",
github="https://github.com/alice",
bio="Interested in AI healthcare projects."
),

UserProfile(
id="2",
name="Bob",
college="Stanford",
skills=["React","JavaScript","UI"],
interests=["Hackathons","Frontend"],
experience="1 Year",
github="https://github.com/bob",
bio="Frontend developer with React experience."
),

UserProfile(
id="3",
name="Charlie",
college="IIT Delhi",
skills=["Statistics","Data Science","Python"],
interests=["Analytics","Research"],
experience="3 Years",
github="https://github.com/charlie",
bio="Statistics enthusiast working on predictive models."
),

UserProfile(
id="4",
name="David",
college="NIT Trichy",
skills=["Java","Spring Boot","Backend"],
interests=["Cloud","APIs"],
experience="2 Years",
github="https://github.com/david",
bio="Backend engineer building scalable APIs."
),

]
from embeddings import profile_to_text, get_embedding
from pinecone_db import upload_profile


def upload_all_profiles():

    for user in users:

        text = profile_to_text(user)

        embedding = get_embedding(text)

        upload_profile(user, embedding)

    print("All profiles uploaded successfully.")
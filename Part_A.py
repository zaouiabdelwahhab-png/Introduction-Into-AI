
# Smart assistant simulation
Answer = input("# Do you want help ? (yes/no) : ").lower() == "yes"
if Answer:
    print("=> I can help you !")

# Recommendation system
genre = input("# What's your favorite movie genre ? (action, comedy, etc.) : ").lower()
if genre == "action":
    print("=> Recommended movie : Mad Max")
elif genre == "comedy":
    print("=> Recommended movie : Friends")

# AI in daily life
maps = input("# Do you use Google Maps ? (yes/no) : ").lower() == "yes"
netflix = input("# Do you watch netflix ? (yes/no)").lower() == "yes"

if maps and netflix:
    print("=> Ai is used for traffic prediction and for netflix is used for content recommendations")

# Smart assistant with memory

information = ["name", "need", "urgency_level"]
user_data = {}

for i in information:
    user_data[i] = input(f"# Enter your {i}")
    
print(f"=> Welcome {user_data["name"]} !, you need {user_data["need"]}, Priority : {user_data["urgency_level"]}")


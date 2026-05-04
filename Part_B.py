from operator import length_hint

# Spam detector
Message = input("# Enter message : ").lower()
if "win" or "free" in Message:
    print("=> Spam detected!")
else:
    print("=> Safe message")

# Medical diagnosis

fever = input("# Do you have fever ? (yes/no) : ").lower() == "yes"
cough = input("# Do you have cough ? (yes/no) : ").lower() == "yes"
if fever and cough:
    print("=> Possible flu !")

# Spam detector with scoring
Message = input("# Enter message : ").lower()
score = 0

if "win" or "free" in Message:
    score += 2
elif length_hint(Message) < 20 :
    score += 1

if score >= 3:
    print("=> Spam detected!")
else:
    print("=> Safe message!")

# Medical decision system (multi-symptom)

fever = input("# Do you fever? (yes/no) ? : ").lower() == "yes"
cough = input("# Do you cough? (yes/no) ? : ").lower() == "yes"
fatigue = input("# Do you fatigue? (yes/no) ? : ").lower() == "yes"

medical_score = 0

medical_score += 1 if cough else 0
medical_score += 1 if fever else 0
medical_score += 1 if fatigue else 0

if medical_score >= 2:
    print("=> Consult a doctor")
elif medical_score == 1:
    print("=> Monitor condition")










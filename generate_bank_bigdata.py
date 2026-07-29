import random

# Targeted Banking & Financial Fraud Templates
SPAM_TEMPLATES = [
    "URGENT: Your {bank} account ending in {acc} has been {action}. Verify immediately at {url}",
    "{bank} Alert: A transfer of ${amount} was initiated from your account. If this wasn't you, cancel here: {url}",
    "SECURITY NOTICE: New login detected on {bank} mobile app from unknown device. Reset access: {url}",
    "Notice from {courier}: Package delivery failed due to unpaid fee of ${fee}. Pay now: {url}",
    "FINAL WARNING: Your {service} profile has been suspended due to billing failure. Update info: {url}",
    "ALERT: Unauthorized withdrawal request of ${amount} on your {bank} card. Stop transaction at {url}"
]

HAM_TEMPLATES = [
    "{bank} PAY: You transferred ${amount} USD to {merchant}. Ref: {ref}. Available balance: ${bal} USD.",
    "Your {bank} mobile verification code is {otp}. Do not share this code with anyone. Expires in 5 mins.",
    "{bank}: You have received ${amount} USD from a contact. Your new balance is ${bal} USD.",
    "Your {ride_service} driver is arriving in {time} mins. License plate: {plate}.",
    "Reminder: Team sync meeting scheduled for tomorrow at {time_str}. Please review the project roadmap.",
    "Hey, let's meet up after training to review the calculus assignment and code."
]

BANKS = ["ABA Bank", "ACLEDA Bank", "Wing Bank", "Canadia Bank", "Sathapana"]
ACTIONS = ["temporarily locked", "restricted", "flagged for suspicious activity", "frozen"]
COURIERS = ["DHL", "FedEx", "CAMPOST"]
SERVICES = ["Netflix", "Telegram", "Crypto Wallet", "Apple ID"]
MERCHANTS = ["Brown Coffee", "Amazon", "Starbucks", "Supermarket", "Fuel Station"]
RIDE_SERVICES = ["Grab", "PassApp"]

DOMAINS_SUSPICIOUS = [
    "http://aba-auth-update-secure.xyz/login",
    "www.dhl-cambodia-delivery-fee.top",
    "http://wing-fraud-alert-cancel.net",
    "http://192.168.1.105/acleda-verify",
    "https://crypto-secure-wallet-recovery.click",
    "http://bank-security-reset-app.buzz"
]

def generate_dataset(filename="bank_bigdata.txt", count_per_class=2500):
    dataset = []
    
    # Generate Financial Spam
    for _ in range(count_per_class):
        template = random.choice(SPAM_TEMPLATES)
        msg = template.format(
            bank=random.choice(BANKS),
            acc=random.randint(1000, 9999),
            action=random.choice(ACTIONS),
            amount=random.randint(50, 2000),
            fee=round(random.uniform(1.5, 9.9), 2),
            courier=random.choice(COURIERS),
            service=random.choice(SERVICES),
            url=random.choice(DOMAINS_SUSPICIOUS)
        )
        dataset.append(f"spam\t{msg}")
        
    # Generate Legitimate Bank & Normal Messages
    for _ in range(count_per_class):
        template = random.choice(HAM_TEMPLATES)
        msg = template.format(
            bank=random.choice(BANKS),
            amount=round(random.uniform(2.0, 150.0), 2),
            merchant=random.choice(MERCHANTS),
            ref=random.randint(100000, 999999),
            bal=round(random.uniform(20.0, 5000.0), 2),
            otp=random.randint(100000, 999999),
            ride_service=random.choice(RIDE_SERVICES),
            time=random.randint(2, 10),
            plate=f"{random.randint(1,9)}A-{random.randint(1000,9999)}",
            time_str="5:00 AM"
        )
        dataset.append(f"ham\t{msg}")
        
    random.shuffle(dataset)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(dataset))
        
    print(f"Successfully generated {len(dataset)} targeted financial messages in '{filename}'!")

if __name__ == "__main__":
    generate_dataset()
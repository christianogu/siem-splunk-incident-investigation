import random
import time

normal_users = ['alice', 'bob', 'charlie', 'dave']
suspicious_users = ['eve', 'mallory']
events = ['login_success', 'login_failure', 'process_start', 'file_access']

def generate_log():
    user = random.choice(normal_users + suspicious_users)
    event = random.choice(events)
    timestamp = time.strftime('%b %d %H:%M:%S')
    ip = f"192.168.1.{random.randint(2,254)}"
    
    if event == 'login_success':
        return f"{timestamp} {user} login succeeded from {ip}"
    elif event == 'login_failure':
        return f"{timestamp} {user} failed login attempt from {ip}"
    elif event == 'process_start':
        process = random.choice(['bash', 'python', 'curl', 'wget'])
        return f"{timestamp} {user} started process {process}"
    elif event == 'file_access':
        filename = random.choice(['/etc/passwd', '/var/log/auth.log', f'/home/{user}/secret.txt'])
        return f"{timestamp} {user} accessed file {filename}"

if __name__ == "__main__":
    with open('sample_logs.txt', 'w') as f:
        for _ in range(1000):
            log = generate_log()
            f.write(log + "\n")

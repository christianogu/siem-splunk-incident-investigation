import time

with open('test_failed_logins.txt', 'w') as f:
    for i in range(5):
        log = f"Aug 11 12:34:5{i} mallory failed login attempt from 192.168.1.45"
        f.write(log + "\n")
        time.sleep(0.1)  # short delay just to simulate time difference

import smtplib
from email.mime.text import MIMEText
import os

def send_alert(email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'your_password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        print("Uyarı e-postası gönderildi.")

def block_ip(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")
    print(f"{ip} adresi engellendi.")

if __name__ == "__main__":
    # Örnek IP ve uyarı
    attack_ip = '192.168.1.100'
    send_alert('admin@example.com', 'Saldırı Tespit Edildi', f'{attack_ip} adresinden bir saldırı tespit edildi.')
    block_ip(attack_ip)

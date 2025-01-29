# 🎯 **RedPi: Offensive Security Simulation**

## 🛡️ **Overview**

This project demonstrates a **controlled phishing simulation** using a Raspberry Pi as the attacker system and a Windows 11 machine as the target. The project showcases **red team tactics** to understand attacker methodologies and improve cybersecurity defenses. It includes key operations such as:
- Phishing campaigns
- Payload deployment
- Reverse engineering
- Command-and-control (C2) management

The project utilizes tools like **Postfix**, **Dovecot**, and **Roundcube** for simulating email-based phishing attacks and applies the **MITRE ATT&CK framework** to analyze each phase of the attack.

---

## 🚀 **Features**
- **Phishing Simulation**: Automates the process of crafting  and sending phishing emails with malicious payloads.
- **Payload Deployment**: Deploys Fully Undetectable (FUD) payloads created with Windows PowerShell, bypassing Windows 11 security features.
- **Reverse Engineering**: Raspberry Pi acts as a platform for analyzing and refining attack strategies.
- **Command-and-Control (C2) by Raspberry Pi**: Manages reverse shell connections for tasks like privilege escalation and data exfiltration.
- **Real-Time Monitoring**: Tracks attack progress and sends alerts for successful payload execution or interruptions.
- **MITRE ATT&CK Integration**: Maps tactics, techniques, and procedures (TTPs) for structured analysis.


---

## 🧩 **Project Components**

### **1. Hardware**
- Raspberry Pi (attacker system)
- Windows 11 machine (target system)

### **2. Software/Tools**
- **Postfix, Dovecot, Roundcube**: Email server configuration for phishing campaigns.
- **Windows PowerShell**: Creation of Fully Undetectable (FUD) payloads.
- **Netcat**: Capturing reverse shell connections.
- **MITRE ATT&CK Framework**: Structured analysis of attack phases.

### **3. Key Attack Phases**
- **Initial Access**: Phishing emails with malicious attachments.
- **Execution**: FUD payload delivery and execution.
- **Privilege Escalation**: Gaining higher access on the target system.
- **Exfiltration**: Stealing data from the target system.

 ### **4. Data Flow Diagram**

 
 ![Att&ck Time Line](https://raw.githubusercontent.com/JOSHUAPBIJU/RedPi-Offensive-Security-Simulation/refs/heads/main/Resource/flow_diagram.png)
## 🔧 **How to Use**

### **Prerequisites**
- A Raspberry Pi with network access.
- A Windows 11 machine with updated security features.
- Knowledge of Linux commands and basic networking.

- ### **Setup Instructions**

1. Configure the Raspberry Pi:
   - Install and configure **Postfix**, **Dovecot**, and **Roundcube**.
   - Set up the phishing email template and attach the malicious payload.
2. Generate FUD payloads using **Windows PowerShell**.
3. Simulate the phishing attack:
   - Send phishing emails from the Raspberry Pi.
   - Monitor the attack progress and capture reverse shell connections using **Netcat**.
4. Analyze attack phases with the **MITRE ATT&CK framework** to identify vulnerabilities.
## 📊 **Results**

This project demonstrates the effectiveness of phishing simulations for testing security defenses. It highlights:
- The ability of FUD payloads to bypass modern security systems by using Raspberry Pi
- The role of automation in improving the efficiency of red team operations.
- Insights into vulnerabilities and recommendations for strengthening defenses.
---

## ⚠️ **Disclaimer**

This project is for **educational purposes only**. Unauthorized use of these techniques or tools against systems without permission is **illegal** and **unethical**.

---

## 🙌 **Acknowledgments**
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- Community resources for Raspberry Pi and cybersecurity tools.

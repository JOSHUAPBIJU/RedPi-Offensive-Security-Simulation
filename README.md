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

## 🔧 **How to Use**

### **Prerequisites**
- A Raspberry Pi with network access.
- A Windows 11 machine with updated security features.
- Knowledge of Linux commands and basic networking.

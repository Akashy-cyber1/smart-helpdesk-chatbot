def ai_response(text, history=[]):
    text = text.lower()

    # Greetings
    if any(word in text for word in ["how are you", "how r you"]):
        return "I'm doing great! How can I help you today? 😊"

    if any(word in text for word in ["what can you do", "what do you do"]):
        return "I can help you with IT support and HR queries! Ask me about computer problems, wifi, passwords, leave policies and more."

    if any(word in text for word in ["your name", "who are you"]):
        return "I'm Smart Helpdesk Assistant — your AI helper for IT and HR! 🤖"

    if any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye! Have a great day! 👋"

    if any(word in text for word in ["thank", "thanks"]):
        return "You're welcome! 😊"

    # IT Issues
    if any(word in text for word in ["not starting", "won't start", "not turning on"]):
        return "Try: 1. Check power cable 2. Hold power button 30sec 3. Remove and reinsert battery 4. Contact IT if issue persists."

    if any(word in text for word in ["wifi", "internet", "network"]):
        return "Try: 1. Restart router 2. Forget and reconnect network 3. Disable airplane mode 4. Update network drivers."

    if any(word in text for word in ["slow", "lagging", "hanging", "freeze"]):
        return "Try: 1. Restart system 2. Close unused apps 3. Run Disk Cleanup 4. Check Task Manager 5. Scan for malware."

    if any(word in text for word in ["password", "forgot", "reset"]):
        return "To reset password: 1. Click 'Forgot Password' 2. Enter your email 3. Check inbox for reset link 4. Create new password."

    if any(word in text for word in ["printer", "print"]):
        return "Try: 1. Check printer connection 2. Restart printer 3. Clear print queue 4. Reinstall printer driver."

    if any(word in text for word in ["virus", "malware", "hack"]):
        return "Immediately: 1. Disconnect from internet 2. Run Windows Defender scan 3. Don't open any files 4. Contact IT support."

    # HR Issues
    if any(word in text for word in ["leave", "leaves", "vacation", "holiday"]):
        return "You get 18 paid leaves per year: Casual: 6 | Medical: 6 | Earned: 6. Apply via HR portal."

    if any(word in text for word in ["salary", "pay", "payslip"]):
        return "Salary is credited on the 1st of every month. For payslip, login to HR portal → Payroll section."

    if any(word in text for word in ["timing", "office hours", "work hours"]):
        return "Office timings: 9:00 AM to 6:00 PM, Monday to Friday. WFH available on request."

    if any(word in text for word in ["appraisal", "increment", "hike"]):
        return "Annual appraisals happen in April. Performance review starts in March."

    # Default
    return "I'm not sure about that. Please contact IT support at support@company.com or HR at hr@company.com"
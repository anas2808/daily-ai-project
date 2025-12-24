import re
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- HTML/CSS/JS (embedded) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Strength Checker</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #e9ecef;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            color: #343a40;
        }
        .container {
            background-color: #ffffff;
            padding: 35px 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 450px;
            width: 100%;
            animation: fadeIn 0.8s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #0056b3;
            margin-bottom: 25px;
            font-size: 2em;
        }
        input[type="password"] {
            width: calc(100% - 24px);
            padding: 12px;
            margin-bottom: 25px;
            border: 2px solid #ced4da;
            border-radius: 6px;
            font-size: 17px;
            box-sizing: border-box;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }
        input[type="password"]:focus {
            border-color: #007bff;
            box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
            outline: none;
        }
        #strength-feedback {
            font-size: 1.15em;
            font-weight: bold;
            margin-top: 25px;
            padding: 12px 15px;
            border-radius: 6px;
            min-height: 50px; /* Ensure consistent height */
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1.4;
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }
        .strength-initial { color: #6c757d; background-color: #e2e3e5; border: 1px solid #d6d8db; }
        .strength-very-weak { color: #721c24; background-color: #f8d7da; border: 1px solid #f5c6cb; }
        .strength-weak { color: #856404; background-color: #fff3cd; border: 1px solid #ffeeba; }
        .strength-moderate { color: #004085; background-color: #cce5ff; border: 1px solid #b8daff; }
        .strength-strong { color: #155724; background-color: #d4edda; border: 1px solid #c3e6cb; }
        .strength-very-strong { color: #0c5460; background-color: #d1ecf1; border: 1px solid #bee5eb; }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #6c757d;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Strength Checker</h1>
        <input type="password" id="passwordInput" placeholder="Enter your password" onkeyup="checkPasswordStrength()">
        <div id="strength-feedback" class="strength-initial">Type to check strength</div>
        <div class="footer">
            Built by a Senior Software Engineer | Python, Flask, HTML, CSS, JS
        </div>
    </div>

    <script>
        // Debounce function to limit how often checkPasswordStrength is called
        let timeout = null;
        function debounce(func, delay) {
            return function(...args) {
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(this, args), delay);
            };
        }

        const checkPasswordStrengthDebounced = debounce(() => {
            const password = document.getElementById('passwordInput').value;
            const feedbackDiv = document.getElementById('strength-feedback');

            if (password.length === 0) {
                feedbackDiv.className = 'strength-initial';
                feedbackDiv.textContent = 'Type to check strength';
                return;
            }

            fetch('/check_strength', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ password: password })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                feedbackDiv.textContent = data.feedback;
                // Ensure data.level exists and is a string for class manipulation
                if (data.level) {
                    feedbackDiv.className = 'strength-' + data.level.toLowerCase().replace(' ', '-');
                } else {
                    feedbackDiv.className = 'strength-initial'; // Fallback
                }
            })
            .catch(error => {
                console.error('Error:', error);
                feedbackDiv.textContent = 'Error checking strength. Please try again.';
                feedbackDiv.className = 'strength-very-weak';
            });
        }, 300); // 300ms debounce delay

        // Assign the debounced function to onkeyup
        document.getElementById('passwordInput').onkeyup = checkPasswordStrengthDebounced;
    </script>
</body>
</html>
"""

# --- Password Strength Logic ---
def calculate_password_strength(password):
    score = 0
    feedback_messages = [] # List to collect suggestions/warnings

    # Common weak passwords list (extend this list as needed)
    common_weak_passwords = set([
        "password", "123456", "qwerty", "admin", "12345678", "dragon",
        "p@ssword", "iloveyou", "secret", "master", "welcome", "change",
        "guest", "access", "football", "baseball", "heaven", "summer",
        "justice", "phoenix", "batman", "superman", "starwars", "pokemon",
        "godzilla", "naruto", "hulk", "spiderman", "america", "united",
        "princess", "computer", "keyboard", "monkey", "abcdef", "123123",
        "qweasd", "asdfgh", "zxcvbn", "testpass", "mypassword"
    ])

    # Initial check for very short or common passwords (high priority override)
    if len(password) == 0:
        return {"score": 0, "level": "Initial", "feedback": "Type to check strength"}
    if password.lower() in common_weak_passwords:
        return {"score": 0, "level": "Very Weak", "feedback": "This is a very common and easily guessable password. Please choose a different one."}
    if len(password) < 6:
        return {"score": 0, "level": "Very Weak", "feedback": "Password is too short (min 6 characters recommended)."}

    # 1. Length Bonus
    length = len(password)
    score += length * 4
    if length >= 12:
        feedback_messages.append("Length is excellent!")
    elif length >= 8:
        feedback_messages.append("Good length.")
    else: # length < 8 (but >= 6 due to early exit)
        feedback_messages.append("Password could be longer (aim for 8+ characters).")

    # 2. Character Type Bonuses
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    # Special characters: using a broader set that is commonly accepted
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?`~]', password))

    if has_lower: score += 15
    else: feedback_messages.append("Include lowercase letters.")
    if has_upper: score += 15
    else: feedback_messages.append("Include uppercase letters.")
    if has_digit: score += 15
    else: feedback_messages.append("Include numbers.")
    if has_special: score += 20
    else: feedback_messages.append("Include special characters (e.g., !@#$).")

    # 3. Combination Bonus
    num_types = sum([has_lower, has_upper, has_digit, has_special])
    if num_types >= 3:
        score += 20
        feedback_messages.append("Good mix of character types.")
    if num_types == 4:
        score += 25  # Additional bonus for all four types
        feedback_messages.append("Excellent character diversity!")

    # 4. Deductions

    # Consecutive identical characters (e.g., 'aaa', '111', 'AAA')
    for match in re.finditer(r'(.)\1{2,}', password):
        # Deduction is based on the number of excess repeating characters
        # 'aaa' (3 chars) -> 1 excess (3-2) -> -5
        deduction = (len(match.group(0)) - 2) * 5
        score -= deduction
        feedback_messages.append(f"Avoid repeating characters like '{match.group(1)*3}' (deduction: {deduction} points).")

    # Sequential letters (e.g., 'abc', 'def', 'zyx')
    seq_letters_count = 0
    for i in range(length - 2):
        s = password[i:i+3]
        # Check for ascending ('abc') or descending ('cba') sequences
        if s.isalpha() and (
            (ord(s[0].lower()) + 1 == ord(s[1].lower()) and ord(s[1].lower()) + 1 == ord(s[2].lower())) or
            (ord(s[0].lower()) - 1 == ord(s[1].lower()) and ord(s[1].lower()) - 1 == ord(s[2].lower()))
        ):
            seq_letters_count += 1
    if seq_letters_count > 0:
        deduction = seq_letters_count * 10
        score -= deduction
        feedback_messages.append(f"Avoid sequential letters (e.g., 'abc') (deduction: {deduction} points).")

    # Sequential digits (e.g., '123', '456', '321')
    seq_digits_count = 0
    for i in range(length - 2):
        s = password[i:i+3]
        if s.isdigit() and (
            (int(s[0]) + 1 == int(s[1]) and int(s[1]) + 1 == int(s[2])) or
            (int(s[0]) - 1 == int(s[1]) and int(s[1]) - 1 == int(s[2]))
        ):
            seq_digits_count += 1
    if seq_digits_count > 0:
        deduction = seq_digits_count * 10
        score -= deduction
        feedback_messages.append(f"Avoid sequential digits (e.g., '123') (deduction: {deduction} points).")

    # Ensure score doesn't go below zero
    score = max(0, score)

    # Determine strength level and initial general feedback
    if score >= 160:
        level = "Very Strong"
        general_feedback = "Excellent password strength! Keep it up."
    elif score >= 120:
        level = "Strong"
        general_feedback = "Strong password! You're doing great."
    elif score >= 80:
        level = "Moderate"
        general_feedback = "Moderate password strength."
    elif score >= 40:
        level = "Weak"
        general_feedback = "Weak password."
    else:
        level = "Very Weak"
        general_feedback = "Very weak password."

    # Filter feedback messages based on strength level
    actionable_tips = []
    other_tips = []
    for msg in feedback_messages:
        # Keywords that indicate an actionable suggestion or a critical warning
        if any(keyword in msg for keyword in ["Include", "Avoid", "longer", "shorter", "deduction"]):
            actionable_tips.append(msg)
        else:
            other_tips.append(msg)

    if level in ["Very Weak", "Weak", "Moderate"]:
        # For lower strengths, prioritize actionable tips
        if actionable_tips:
            final_feedback = f"{general_feedback} Suggestions: {'; '.join(actionable_tips)}."
        elif other_tips: # Fallback if no specific actionable but other general tips exist
            final_feedback = f"{general_feedback} {'; '.join(other_tips)}."
        else:
            final_feedback = general_feedback # Should ideally not happen if length/types checked
    else: # Strong, Very Strong
        # For higher strengths, just combine general feedback with all tips
        all_tips = actionable_tips + other_tips
        if all_tips:
            final_feedback = f"{general_feedback} Tips: {'; '.join(all_tips)}."
        else:
            final_feedback = general_feedback

    return {
        "score": score,
        "level": level,
        "feedback": final_feedback
    }

# --- Flask Routes ---
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/check_strength', methods=['POST'])
def check_strength():
    data = request.get_json()
    password = data.get('password', '')
    result = calculate_password_strength(password)
    return jsonify(result)

# --- Run the App ---
if __name__ == '__main__':
    # Running in debug mode reloads the server on code changes and provides a debugger.
    # In a production environment, disable debug mode and use a production WSGI server.
    app.run(debug=True, host='0.0.0.0', port=5000)
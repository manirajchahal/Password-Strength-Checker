import tkinter as tk

def check_password_strength(password):
    score = 0
    feedback = []
    total_possible = 5  # Total points based on 5 criteria

    # List of common passwords
    common_passwords = {
        "password", "passwords" "123456", "123456789", "qwerty", "abc123", "football",
        "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop",
        "123321", "mustang", "1234567", "123123", "welcome", "login", "admin",
        "princess"
    }

    # Criterion 1: Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to at least 8 characters.")

    # Criterion 2: Lowercase letters check
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Criterion 3: Uppercase letters check
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Criterion 4: Digit check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    # Criterion 5: Special characters check
    if any(c in "!@#$%^&*()" for c in password):
        score += 1
    else:
        feedback.append("Include special characters (e.g., !@#$%^&*()).")

    # Check if the password is too common
    if password.lower() in common_passwords:
        feedback.append("This password is too common. Avoid using it.")
        score = max(score - 1, 0)

    # Map numerical score to a strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, total_possible, strength, feedback

def get_color_for_score(score):
    # Color mapping for each integer score
    color_mapping = {
        0: "#FF0000",  # red for no points
        1: "#FF0000",  # 1/5 = red
        2: "#FF8000",  # 2/5 = orange
        3: "#FFFF00",  # 3/5 = yellow
        4: "#BFFF00",  # 4/5 = yellow-green
        5: "#00FF00"   # 5/5 = green
    }
    return color_mapping.get(score, "#FF0000")

def evaluate_password():
    pwd = entry.get()
    score, total, strength, suggestions = check_password_strength(pwd)
    
    # Calculate fraction of the total score for bar width
    fraction = score / total
    fill_width = fraction * canvas_width

    # Get the color based on the integer score
    fill_color = get_color_for_score(score)

    # Clear the canvas and redraw background then the progress bar fill
    progress_canvas.delete("all")
    progress_canvas.create_rectangle(0, 0, canvas_width, "20", fill="lightgrey", outline="")
    progress_canvas.create_rectangle(0, 0, fill_width, "20", fill=fill_color, outline="")

    # Update result label with score and strength
    result_label.config(text=f"Password Strength: {strength} ({score}/{total})")

    # Update suggestions label
    suggestions_text = "\n".join(suggestions) if suggestions else "No suggestions. Good job!"
    suggestions_label.config(text=suggestions_text)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create UI elements
instruction_label = tk.Label(root, text="Enter your password:")
instruction_label.pack(pady=5)

# Entry widget with plaintext display
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=evaluate_password)
check_button.pack(pady=5)

# Dimensions
canvas_width = 300
canvas_height = 50

# Create a Canvas to display the progress bar and draw default background immediately
progress_canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
progress_canvas.pack(pady=5)
progress_canvas.create_rectangle(0, 0, canvas_width, "20", fill="lightgrey", outline="")

result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=5)

suggestions_label = tk.Label(root, text="", justify="left")
suggestions_label.pack(pady=5)

root.mainloop()

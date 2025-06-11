import tkinter as tk
from tkinter import messagebox

# Dummy users
users = {
    "user@example.com": "password123",
    "admin@example.com": "admin"
}

# Global booking info
booking_details = {}

# Movies mapped to malls
mall_movies = {
    "PVR Cinemas": ["Avengers: Endgame", "Inception"],
    "INOX Metro": ["Interstellar", "Bahubali 2"],
    "Miraj Cinemas": ["KGF", "Jawan"],
    "City Pride": ["Leo", "Pathaan"]
}

# Movie details
movie_data = {
    "Avengers: Endgame": {
        "showtimes": ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]
    },
    "Inception": {
        "showtimes": ["9:30 AM", "12:30 PM", "3:30 PM", "6:30 PM"]
    },
    "Interstellar": {
        "showtimes": ["10:15 AM", "1:15 PM", "4:15 PM", "7:15 PM"]
    },
    "KGF": {
        "showtimes": ["11:00 AM", "2:00 PM", "5:00 PM", "8:00 PM"]
    },
    "Jawan": {
        "showtimes": ["10:45 AM", "1:45 PM", "4:45 PM", "7:45 PM"]
    },
    "Bahubali 2": {
        "showtimes": ["9:00 AM", "12:00 PM", "3:00 PM", "6:00 PM"]
    },
    "Leo": {
        "showtimes": ["9:15 AM", "12:15 PM", "3:15 PM", "6:15 PM"]
    },
    "Pathaan": {
        "showtimes": ["11:30 AM", "2:30 PM", "5:30 PM", "8:30 PM"]
    }
}

# Main window
root = tk.Tk()
root.title("🎟 Movie Booking System")
root.geometry("550x580")
root.configure(bg="#1e1e2f")

f = tk.Frame(root, bg="#2c2f4a", padx=25, pady=25, relief="groove", bd=2)
f.pack(expand=True, fill="both", padx=20, pady=20)

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 12, "bold")

BUTTON_BG = "#4a90e2"
BUTTON_FG = "white"
BUTTON_HOVER_BG = "#357ABD"

def on_enter(e): e.widget['background'] = BUTTON_HOVER_BG
def on_leave(e): e.widget['background'] = BUTTON_BG

def style_button(btn):
    btn.config(bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BUTTON_HOVER_BG,
               relief="flat", padx=15, pady=8, cursor="hand2", font=FONT_BUTTON)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Login Page
def login_page():
    f.pack()
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text="🔐 Login", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=25)
    tk.Label(f, text="Email", font=FONT_LABEL, bg=f['bg'], fg="white").pack(anchor="w")
    email_entry = tk.Entry(f, width=35, font=FONT_LABEL, relief="flat")
    email_entry.pack(pady=6, ipady=6)
    tk.Label(f, text="Password", font=FONT_LABEL, bg=f['bg'], fg="white").pack(anchor="w")
    password_entry = tk.Entry(f, show="*", width=35, font=FONT_LABEL, relief="flat")
    password_entry.pack(pady=6, ipady=6)

    def authenticate():
        email = email_entry.get()
        password = password_entry.get()
        if users.get(email) == password:
            booking_details["user"] = email
            messagebox.showinfo("Login Success", f"Welcome, {email}")
            show_malls()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    btn_login = tk.Button(f, text="Login", command=authenticate)
    btn_login.pack(pady=20)
    style_button(btn_login)

    tk.Label(f, text="Don't have an account?", font=FONT_LABEL, bg=f['bg'], fg="white").pack()
    btn_signup = tk.Button(f, text="Sign Up", command=signup_page)
    btn_signup.pack(pady=10)
    style_button(btn_signup)

# Signup Page
def signup_page():
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text="📝 Sign Up", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=25)
    tk.Label(f, text="Email", font=FONT_LABEL, bg=f['bg'], fg="white").pack(anchor="w")
    email_entry = tk.Entry(f, width=35, font=FONT_LABEL, relief="flat")
    email_entry.pack(pady=6, ipady=6)
    tk.Label(f, text="Password", font=FONT_LABEL, bg=f['bg'], fg="white").pack(anchor="w")
    password_entry = tk.Entry(f, show="*", width=35, font=FONT_LABEL, relief="flat")
    password_entry.pack(pady=6, ipady=6)

    def register():
        email = email_entry.get()
        password = password_entry.get()
        if not email or not password:
            messagebox.showerror("Error", "Fields cannot be empty")
        elif email in users:
            messagebox.showerror("Error", "User already exists")
        else:
            users[email] = password
            messagebox.showinfo("Success", "Account created successfully!")
            login_page()

    btn_register = tk.Button(f, text="Register", command=register)
    btn_register.pack(pady=20)
    style_button(btn_register)

    btn_back = tk.Button(f, text="⬅ Back to Login", command=login_page)
    btn_back.pack()
    style_button(btn_back)

# Malls Page
def show_malls():
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text="🏢 Select a Mall", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=20)
    for mall in mall_movies:
        btn = tk.Button(f, text=mall, command=lambda m=mall: show_movies(m))
        btn.pack(pady=8, fill="x")
        style_button(btn)

# Movies for Selected Mall
def show_movies(mall):
    booking_details["mall"] = mall
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text=f"🎬 Movies at {mall}", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=20)
    for movie in mall_movies[mall]:
        btn = tk.Button(f, text=movie, command=lambda m=movie: show_showtimes(m))
        btn.pack(pady=8, fill="x")
        style_button(btn)

    btn_back = tk.Button(f, text="⬅ Back to Malls", command=show_malls)
    btn_back.pack(pady=20)
    style_button(btn_back)

# Showtimes Page
def show_showtimes(movie):
    booking_details["movie"] = movie
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text=f"⏰ Showtimes for {movie}", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=20)
    for time in movie_data[movie]["showtimes"]:
        btn = tk.Button(f, text=time, command=lambda t=time: show_seats(t))
        btn.pack(pady=6, fill="x")
        style_button(btn)

# Seats Page
def show_seats(time):
    booking_details["time"] = time
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text="💺 Choose Your Seats", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=20)
    seat_frame = tk.Frame(f, bg=f['bg'])
    seat_frame.pack(pady=10)

    status = []
    rows, cols = 5, 5
    for r in range(rows):
        for c in range(cols):
            var = tk.IntVar()
            seat_num = r * cols + c + 1
            chk = tk.Checkbutton(seat_frame, text=str(seat_num), variable=var,
                                 font=FONT_LABEL, bg=f['bg'], fg="white",
                                 selectcolor="#4a90e2")
            chk.grid(row=r, column=c, padx=8, pady=8)
            status.append((var, seat_num))

    def confirm_booking():
        selected_seats = [num for var, num in status if var.get() == 1]
        if not selected_seats:
            messagebox.showerror("Error", "Please select at least one seat.")
        else:
            booking_details["seats"] = selected_seats
            show_receipt()

    btn_confirm = tk.Button(f, text="✅ Confirm Booking", command=confirm_booking)
    btn_confirm.pack(pady=20)
    style_button(btn_confirm)

# Receipt
def show_receipt():
    for widget in f.winfo_children(): widget.destroy()

    tk.Label(f, text="🎫 Booking Receipt", font=FONT_TITLE, bg=f['bg'], fg="white").pack(pady=20)

    receipt_text = (
        f"👤 User: {booking_details.get('user')}\n"
        f"🏢 Mall: {booking_details.get('mall')}\n"
        f"🎬 Movie: {booking_details.get('movie')}\n"
        f"🕒 Time: {booking_details.get('time')}\n"
        f"💺 Seats: {', '.join(map(str, booking_details.get('seats', [])))}\n"
        f"💰 Total: ₹{len(booking_details.get('seats', [])) * 150}"
    )

    receipt_box = tk.Text(f, width=48, height=10, font=("Courier New", 14), bg="#e6e6e6", fg="#333333", relief="flat")
    receipt_box.insert("1.0", receipt_text)
    receipt_box.config(state="disabled")
    receipt_box.pack(pady=15)

    def print_receipt():
        with open("receipt.txt", "w") as file:
            file.write(receipt_text)
        messagebox.showinfo("Printed", "Receipt saved as 'receipt.txt'.")

    btn_print = tk.Button(f, text="🖨 Print Receipt", command=print_receipt)
    btn_print.pack(pady=8)
    style_button(btn_print)

    btn_new = tk.Button(f, text="🔁 Book Again", command=show_malls)
    btn_new.pack(pady=8)
    style_button(btn_new)

# Start App
login_page()
root.mainloop()

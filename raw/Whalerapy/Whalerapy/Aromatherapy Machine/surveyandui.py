import os
# Tell gpiozero to use fake pins so Windows doesn't freak out
os.environ["GPIOZERO_PIN_FACTORY"] = "mock"

import customtkinter as ctk
from gpiozero import OutputDevice
import time
# ... the rest of your code ...

# Set the overarching theme to a deep ocean look
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") # Gives us beautiful aqua-blue highlights

# --- HARDWARE SETUP ---
try:
    pump_wood = OutputDevice(17)   # Pump 1 (Relax)
    pump_flower = OutputDevice(27) # Pump 2 (Boost)
    pump_fruit = OutputDevice(22)  # Pump 3 (Joy/Fruit) - Make sure to plug this into Pin 22!
except Exception as e:
    pump_wood = None
    pump_flower = None
    pump_fruit = None

# --- SURVEY DATA ---
questions = [
    {
        "text": "1. Imagine you are living in your dream world. Where would you be?",
        "wood": "A cozy cabin hidden deep in a quiet forest.",
        "flower": "A sunny cottage in a bright, blooming garden.",
        "fruit": "A warm, tropical beach surrounded by fruit trees."
    },
    {
        "text": "2. How do you want this aromatherapy session to make you feel?",
        "wood": "Grounded, calm, and deeply relaxed.",
        "flower": "Uplifted, refreshed, and energized.",
        "fruit": "Bright, playful, and full of joy."
    },
    {
        "text": "3. Which words best describe your favorite scents?",
        "wood": "Earthy, warm, and musky.",
        "flower": "Sweet, light, and floral.",
        "fruit": "Juicy, vibrant, and citrusy."
    },
    {
        "text": "4. Which type of tea would you prefer to drink right now?",
        "wood": "A rich, earthy black tea or spiced chai.",
        "flower": "A delicate chamomile or floral tea.",
        "fruit": "A refreshing iced berry or citrus tea."
    },
    {
        "text": "5. Which seasons' atmosphere is the most comforting?",
        "wood": "Crisp Autumn with falling leaves.",
        "flower": "Bright Spring with fresh blooms.",
        "fruit": "Sunny Summer with a warm breeze."
    },
    {
        "text": "6. What is your favorite time of day?",
        "wood": "Late at night, watching the embers of a fire.",
        "flower": "Early morning, just as the sun touches the dew.",
        "fruit": "High noon, soaking up the bright sunshine."
    },
    {
        "text": "7. If you could surround yourself with one color palette, what would it be?",
        "wood": "Deep greens, browns, and warm golds.",
        "flower": "Soft pinks, lavenders, and pastel blues.",
        "fruit": "Vibrant oranges, yellows, and coral pinks."
    },
    {
        "text": "8. What kind of soundscape relaxes you the most?",
        "wood": "Low acoustic guitar or a distant rolling thunderstorm.",
        "flower": "Gentle piano or a soft breeze blowing through chimes.",
        "fruit": "Upbeat acoustic rhythms or crashing ocean waves."
    },
    {
        "text": "9. How do you usually prefer to handle a stressful day?",
        "wood": "Retreating to a quiet, cozy place to reflect and reset.",
        "flower": "Going for a peaceful walk in nature to clear my head.",
        "fruit": "Doing something fun, active, or creative to burn off energy."
    },
    {
        "text": "10. Which of these small moments brings you the most peace?",
        "wood": "Reading a book wrapped in a heavy blanket.",
        "flower": "Arranging a fresh bouquet of flowers in a vase.",
        "fruit": "Enjoying a cold, sweet drink on a hot afternoon."
    }
]

class WhalerapySurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("WHALERAPY")
        self.root.geometry("800x480")
        
        # Deep Midnight Ocean Background
        self.root.configure(bg="#0B192C") 

        self.current_q = 0
        self.wood_score = 0
        self.flower_score = 0
        self.fruit_score = 0

        # --- UI ELEMENTS ---
        # Main Header
        self.title_label = ctk.CTkLabel(
            root, text="WHALERAPY", 
            font=("Helvetica", 36, "bold"), 
            text_color="#00D2C4" # Bright Bioluminescent Cyan/Aqua
        )
        self.title_label.pack(pady=35)

        # Question Text Box
        self.question_label = ctk.CTkLabel(
            root, text="Tap below to discover your perfect scent alignment.", 
            font=("Helvetica", 20), 
            text_color="#E0F7FA", # Ice Blue text
            wraplength=650
        )
        self.question_label.pack(pady=25)

        # Button A (Wood) - Styled with a 20px round radius!
        self.btn_a = ctk.CTkButton(
            root, text="Begin Journey", 
            font=("Helvetica", 18, "bold"),
            fg_color="#1F4068",      # Deep Sea Blue
            hover_color="#162447",
            text_color="white",
            width=550, height=70,
            corner_radius=20,        
            command=self.start_survey
        )
        self.btn_a.pack(pady=10)

        # Button B (Flower)
        self.btn_b = ctk.CTkButton(
            root, text="", 
            font=("Helvetica", 18, "bold"),
            fg_color="#00B4D8",      # Vibrant Coral/Wave Blue
            hover_color="#0077B6",
            text_color="white",
            width=550, height=70,
            corner_radius=20,        
            command=lambda: self.record_answer("flower")
        )
        self.btn_b.pack_forget() 

        # Button C (Fruit)
        self.btn_c = ctk.CTkButton(
            root, text="", 
            font=("Helvetica", 18, "bold"),
            fg_color="#F2A65A",      # Sunrise Peach/Orange
            hover_color="#D1813A",
            text_color="white",
            width=550, height=70,
            corner_radius=20,        
            command=lambda: self.record_answer("fruit")
        )
        self.btn_c.pack_forget() 

        # Minimalist Close Button
        self.exit_btn = ctk.CTkButton(root, text="✕", font=("Helvetica", 12), fg_color="#3A1010", width=30, height=30, corner_radius=8, command=root.destroy)
        self.exit_btn.place(relx=0.95, rely=0.03)

    def start_survey(self):
        self.btn_b.pack(pady=10)
        self.btn_c.pack(pady=10)
        self.btn_a.configure(command=lambda: self.record_answer("wood"))
        self.current_q = 0
        self.wood_score = 0
        self.flower_score = 0
        self.fruit_score = 0
        self.load_question()

    def load_question(self):
        if self.current_q < len(questions):
            q_data = questions[self.current_q]
            self.title_label.configure(text=f"DEEP SEA SURVEY • {self.current_q + 1} / 10")
            self.question_label.configure(text=q_data["text"])
            self.btn_a.configure(text=q_data["wood"])
            self.btn_b.configure(text=q_data["flower"])
            self.btn_c.configure(text=q_data["fruit"])
        else:
            self.show_results()

    def record_answer(self, choice):
        if choice == "wood":
            self.wood_score += 1
        elif choice == "flower":
            self.flower_score += 1
        elif choice == "fruit":
            self.fruit_score += 1
        
        self.current_q += 1
        self.load_question()

    def show_results(self):
        self.btn_a.pack_forget()
        self.btn_b.pack_forget()
        self.btn_c.pack_forget()
        
        # Figure out which scent got the most points
        scores = {
            "wood": self.wood_score,
            "flower": self.flower_score,
            "fruit": self.fruit_score
        }
        winner_key = max(scores, key=scores.get)

        if winner_key == "wood":
            winner = "⚓ WOODLAND DRIFTWOOD ⚓\n(Grounded & Relaxing Scent)"
            self.trigger_pump(pump_wood)
        elif winner_key == "flower":
            winner = "🪸 OCEANIC FLORA 🪸\n(Uplifting & Energizing Scent)"
            self.trigger_pump(pump_flower)
        else:
            winner = "🥭 TROPICAL CITRUS 🥭\n(Bright & Joyful Scent)"
            self.trigger_pump(pump_fruit)

        self.title_label.configure(text="ALIGNMENT COMPLETE")
        self.question_label.configure(text=f"Your scent profile is complete.\nDispensing:\n\n{winner}")
        
        self.btn_a.configure(text="Restart Journey", command=self.reset_survey)
        self.btn_a.pack(pady=40)

    def trigger_pump(self, pump):
        if pump:
            pump.on()
            self.root.after(4000, pump.off) # Spray for 4 seconds
        else:
            print("PC Test Mode: Whalerapy is pretending to spray mist!")

    def reset_survey(self):
        self.btn_a.pack_forget()
        self.btn_c.pack_forget()
        self.start_survey()

if __name__ == "__main__":
    # CustomTkinter uses CTk instead of Tk
    root = ctk.CTk() 
    app = WhalerapySurvey(root)
    root.mainloop()
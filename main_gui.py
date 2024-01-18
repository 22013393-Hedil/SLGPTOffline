import customtkinter as ctk
from transformers import pipeline

gpt2_model = pipeline('text-generation', model='openai-community/gpt2-medium')

def generate_response(user_input):
    # Use the GPT-2 model to generate a response
    response = gpt2_model(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    return response

def update_display_box():
    text_to_display = nameEntry.get()
    
    # Append user input to displayBox
    displayBox.insert(ctk.END, f"User: {text_to_display}\n")
    print(f"User: {text_to_display}\n")
    
    # Generate and append GPT-2 response to displayBox
    gpt2_response = generate_response(text_to_display)
    displayBox.insert(ctk.END, f"GPT-2: {gpt2_response}\n")
    print(f"GPT-2: {gpt2_response}\n")
    
    # Clear the entry field after sending
    nameEntry.delete(0, ctk.END)

def generate():
    print('generated')

def change_appearance_mode(mode):
    ctk.set_appearance_mode(mode)

def switch_event():
    appearance_mode = switch_var.get()
    change_appearance_mode(appearance_mode)

def create_settings_game_frame(parent):
    frame = ctk.CTkFrame(parent)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Appearance mode switch
    switch = ctk.CTkSwitch(
        frame, text="Dark Mode", command=switch_event,
        variable=switch_var, onvalue="dark", offvalue="light"
    )
    switch.grid(row=0, column=0, pady=5, sticky="w")

    # Language mode radio buttons
    Language_mode_English = ctk.CTkRadioButton(
        frame, value="English", variable=Language_mode, text="English"
    )
    Language_mode_English.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")
    Language_mode_Indo = ctk.CTkRadioButton(
        frame, value="Indo", variable=Language_mode, text="Bahasa Indonesia"
    )
    Language_mode_Indo.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

    # Game-mode UI
    features_label = ctk.CTkLabel(
        frame, text='Game-Mode Settings', font=ctk.CTkFont(weight='bold')
    )
    features_label.grid(row=3, column=0, pady=(10, 5), sticky="w")
    checkboxes = [
        ctk.CTkCheckBox(frame, text='Fantasy Mode'),
        ctk.CTkCheckBox(frame, text='Future Mode'),
        ctk.CTkCheckBox(frame, text='Prehistoric Mode')
    ]
    for idx, checkbox in enumerate(checkboxes):
        checkbox.grid(row=idx + 4, column=0, pady=5, sticky="w")

    return frame

root = ctk.CTk()  # Initializing
root.geometry("750x550")  # Size of tab
root.title("Offline ChatGPT")
ctk.set_appearance_mode("dark")

Language_mode = ctk.StringVar(value="English")  # Declare the variable
switch_var = ctk.StringVar(value="dark")  # Declare the variable for appearance mode

# Set up a 2x2 grid for the root frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)  # Added to allow height resizing

# Left half of the grid
left_frame = ctk.CTkFrame(root)
left_frame.grid(row=0, column=0, sticky="nsew")

# Right half of the grid
right_frame = ctk.CTkFrame(root)
right_frame.grid(row=0, column=1, sticky="nsew")

# Left half: Split vertically into two parts
left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_rowconfigure(1, weight=1)

# Settings and Game-mode UI
settings_game_frame = create_settings_game_frame(left_frame)

# Right half: ChatGPT UI
# Text Box
displayBox = ctk.CTkTextbox(right_frame, width=450, height=500)
displayBox.grid(row=0, column=0, columnspan=10, padx=10, pady=10, sticky="nsew")

# Name Entry Field
nameEntry = ctk.CTkEntry(right_frame, placeholder_text="Chat with GPT...")
nameEntry.grid(row=1, column=0, columnspan=9, padx=20, pady=5, sticky="ew")

# Button to send text to displayBox
sendButton = ctk.CTkButton(right_frame, text="Send", command=update_display_box)
sendButton.grid(row=1, column=9, padx=5, pady=5, sticky="ew")

# Bind KeyRelease event to update_display_box
nameEntry.bind("<Return>", lambda event: update_display_box())

# Configure weights for responsive resizing
left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_rowconfigure(1, weight=1)
right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(1, weight=1)  # Allow width resizing

root.mainloop()

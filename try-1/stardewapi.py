import pymem#### made by KrawsTV
import pymem.process#### made by KrawsTV
import tkinter as tk#### made by KrawsTV
import tkinter.messagebox as messagebox#### made by KrawsTV
#### made by KrawsTV
# Create the window to ask the user for the memory addresses
address_window = tk.Tk() #### made by KrawsTV
address_window.title("Memory Addresses") #### made by KrawsTV
address_window.geometry("700x300") #### made by  KrawsTV
address_window.configure(bg="#000033") #### made by KrawsTV

# Create a label and an entry box for the time address
time_label = tk.Label(address_window, text="What is the memory address for the player's time (in hexadecimal)?", font=("Arial", 14), bg="#000033", fg="#FFFFFF")
time_label.pack(pady=20) #### made by KrawsTV

time_entry = tk.Entry(address_window, font=("Arial", 14))
time_entry.pack(pady=10)#### made by KrawsTV

# Create a label and an entry box for the money address
money_label = tk.Label(address_window, text="What is the memory address for the player's money (in hexadecimal)?", font=("Arial", 14), bg="#000033", fg="#FFFFFF")
money_label.pack(pady=20) #### made by KrawsTV
#### made by KrawsTV
money_entry = tk.Entry(address_window, font=("Arial", 14))
money_entry.pack(pady=10) #### made by KrawsTV
#### made by KrawsTV
# Create a function to retrieve the memory addresses and close the window
def get_addresses(): #### made by KrawsTV
    global time_address, money_address #### made by KrawsTV
    time_address = int(time_entry.get(), 16) #### made by KrawsTV
    money_address = int(money_entry.get(), 16) #### made by KrawsTV
    address_window.destroy() #### made by KrawsTV
#### made by KrawsTV
# Create a button to submit the memory addresses
submit_button = tk.Button(address_window, text="Submit", command=get_addresses, font=("Arial", 14), bg="#FFFFFF", fg="#000033")
submit_button.pack(pady=10) #### made by KrawsTV
#### made by KrawsTV
# Display the address selection window and wait for the user to make a selection
address_window.mainloop()
#### made by KrawsTV
# Open the game's process and find the memory addresses
pm = pymem.Pymem("Stardew Valley.exe")

client = pymem.process.module_from_name(pm.process_handle, "System.Collections.Concurrent.dll").lpBaseOfDll
#### made by KrawsTV
# Read the current values of time and money from memory
try:
    current_time = pm.read_int(time_address) #### made by KrawsTV
    current_money = pm.read_int(money_address) #### made by KrawsTV
except pymem.exception.MemoryReadError: #### made by KrawsTV
    messagebox.showinfo("Warning", "Memory address not found.") #### made by KrawsTV
    exit() #### made by KrawsTV

#### made by KrawsTV
# Request the expected values for time and money
def get_expected_values(): #### made by KrawsTV
    # Create a new window to get the expected values from the user
    expected_window = tk.Tk() #### made by KrawsTV
    expected_window.title("Expected Values") #### made by KrawsTV
    expected_window.geometry("500x250") #### made by KrawsTV
    expected_window.configure(bg="#1A1A2E") #### made by KrawsTV

    time_label = tk.Label(expected_window, text="Enter the value for the player's time:", fg="#FFFFFF", bg="#1A1A2E", font=("Arial", 14))
    time_label.pack(pady=10) #### made by KrawsTV

    time_entry = tk.Entry(expected_window, font=("Arial", 14))
    time_entry.pack(pady=5) #### made by KrawsTV

    money_label = tk.Label(expected_window, text="Enter the value for the player's money:", fg="#FFFFFF", bg="#1A1A2E", font=("Arial", 14))
    money_label.pack(pady=10) #### made by KrawsTV
#### made by KrawsTV
    money_entry = tk.Entry(expected_window, font=("Arial", 14))
    money_entry.pack(pady=5) #### made by KrawsTV
#### made by KrawsTV
    # Define a function to get the expected values and close the window
    def submit_expected_values(): #### made by KrawsTV
        global expected_time, expected_money #### made by KrawsTV
        expected_time = int(time_entry.get())#### made by KrawsTV
        expected_money = int(money_entry.get()) #### made by KrawsTV
        expected_window.destroy() #### made by KrawsTV
#### made by KrawsTV
    # Create a button to submit the expected values
    submit_button = tk.Button(expected_window, text="Submit", command=submit_expected_values, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
    submit_button.pack(pady=10)

    # Display the window and wait for the user to submit the expected values
    expected_window.mainloop()
#### made by KrawsTV
get_expected_values()
#### made by KrawsTV
# Define the functions that execute the program's logic
def update_money():
    # Create a new window to get the new value from the user
    value_window = tk.Tk()
    value_window.title("Update Money")
    value_window.geometry("300x150")
    value_window.configure(bg="#1A1A2E")

    value_label = tk.Label(value_window, text="Enter the new money value:", fg="#FFFFFF", bg="#1A1A2E", font=("Arial", 14))
    value_label.pack(pady=20)

    value_entry = tk.Entry(value_window, font=("Arial", 14))
    value_entry.pack(pady=10)
#### made by KrawsTV
    # Define a function to update the money value and close the window
    def update_money_value():
        new_value = int(value_entry.get())
        pm.write_int(money_address, new_value)
        messagebox.showinfo("Success", "Money updated")
        value_window.destroy()

    # Create a button to submit the new value
    submit_button = tk.Button(value_window, text="Update", command=update_money_value, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
    submit_button.pack(pady=5)
#### made by KrawsTV
    # Display the window and wait for the user to submit the new value
    value_window.mainloop()


def update_time():
    # Create a new window to get the new value from the user
    value_window = tk.Tk()
    value_window.title("Update Time")
    value_window.geometry("300x150")
    value_window.configure(bg="#1A1A2E")

    value_label = tk.Label(value_window, text="Enter the new time value:", fg="#FFFFFF", bg="#1A1A2E", font=("Arial", 14))
    value_label.pack(pady=20)

    value_entry = tk.Entry(value_window, font=("Arial", 14))
    value_entry.pack(pady=10)
#### made by KrawsTV
    # Define a function to update the time value and close the window
    def update_time_value():
        new_value = int(value_entry.get())
        pm.write_int(time_address, new_value)
        messagebox.showinfo("Success", "Time updated")
        value_window.destroy()

    # Create a button to submit the new value
    submit_button = tk.Button(value_window, text="Update", command=update_time_value, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
    submit_button.pack(pady=5)

    # Display the window and wait for the user to submit the new value
    value_window.mainloop()
###  made by KrawsTV 
# Create the window using tkinter
root = tk.Tk()
root.title("Menu")
root.geometry("300x200")
root.configure(bg="#1A1A2E")

# Create the option menu widgets
label = tk.Label(root, text="Choose an option:", fg="#FFFFFF", bg="#1A1A2E", font=("Arial", 14))
label.pack(pady=20)

button1 = tk.Button(root, text="Update money", command=update_money, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
button1.pack(pady=5)

button2 = tk.Button(root, text="Update time", command=update_time, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
button2.pack(pady=5)

button3 = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#1A1A2E", fg="#FFFFFF")
button3.pack(pady=5)

# Execute the window
root.mainloop()





#### made by KrawsTV

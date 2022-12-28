import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Journal Entry")

# Create a label and text entry for the date
date_label = tk.Label(text="Date:")
date_entry = tk.Entry()

# Create a label and text entry for the entry title
title_label = tk.Label(text="Title:")
title_entry = tk.Entry()

# Create a label and text entry for the entry content
content_label = tk.Label(text="Content:")
content_entry = tk.Text(height=10, width=50)

# Create a button to save the journal entry
save_button = tk.Button(text="Save")

# Create a button to display the journal entries
display_button = tk.Button(text="Display Entries")

# Create a text widget to display the journal entries
display_widget = tk.Text(height=10, width=50)

# Place the widgets in the window
date_label.pack()
date_entry.pack()
title_label.pack()
title_entry.pack()
content_label.pack()
content_entry.pack()
save_button.pack()
display_button.pack()
display_widget.pack()

# Create a list to store the journal entries
journal_entries = []

# Define the callback function for the "Save" button
def save_entry():
  # Get the values from the entry widgets
  date = date_entry.get()
  title = title_entry.get()
  content = content_entry.get("1.0", "end")

  # Create a dictionary to store the journal entry
  entry = {
    "date": date,
    "title": title,
    "content": content
  }

  # Add the entry to the list of journal entries
  journal_entries.append(entry)

  # Clear the entry widgets
  date_entry.delete(0, "end")
  title_entry.delete(0, "end")
  content_entry.delete("1.0", "end")

# Bind the "Save" button to the save_entry callback function
save_button.config(command=save_entry)

# Define the callback function for the "Display Entries" button
def display_entries():
  # Clear the display widget
  display_widget.delete("1.0", "end")

  # Iterate through the journal entries and display them in the widget
  for entry in journal_entries:
    display_widget.insert("end", f"Date: {entry['date']}\n")
    display_widget.insert("end", f"Title: {entry['title']}\n")
    display_widget.insert("end", f"Content: {entry['content']}\n\n")

# Bind the "Display Entries" button to the display_entries callback function
display_button.config(command=display_entries)

# Run the main loop
window.mainloop()

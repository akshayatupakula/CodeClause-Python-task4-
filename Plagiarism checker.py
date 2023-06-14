#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from difflib import SequenceMatcher

def check_plagiarism():
    text1 = text1_text.get("1.0", END)
    text2 = text2_text.get("1.0", END)

    # Remove newlines and spaces
    text1 = text1.replace('\n', '').replace(' ', '')
    text2 = text2.replace('\n', '').replace(' ', '')

    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    plagiarism_label.config(text=f"Similarity Ratio: {similarity_ratio:.2%}")

# Create the GUI window
window = Tk()
window.title("Plagiarism Checker")

# Create the input fields
text1_label = Label(window, text="Text 1:")
text1_label.pack()
text1_text = Text(window, height=10, width=50)
text1_text.pack()

text2_label = Label(window, text="Text 2:")
text2_label.pack()
text2_text = Text(window, height=10, width=50)
text2_text.pack()

check_button = Button(window, text="Check Plagiarism", command=check_plagiarism)
check_button.pack()

plagiarism_label = Label(window, text="")
plagiarism_label.pack()

# Start the GUI event loop
window.mainloop()


# In[ ]:





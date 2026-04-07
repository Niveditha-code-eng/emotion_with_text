from textblob import TextBlob
import tkinter as tk

root = tk.Tk()
root.title("ANALYSISING EMOTION OF THE POEM")
root.geometry("500x500")

label = tk.Label(root, text = "emotion analysis of poem", font = ("Arial",15))
label.pack(pady = 10)

text_box = tk.Text(root, height = 5)
text_box.pack(pady = 10)

def analyze_poem():
    poem_text = text_box.get("1.0",tk.END)
    blob = TextBlob(poem_text)
    sentiment = blob.sentiment

    if sentiment.polarity > 0.1:
        result = "This poem carries a uplifting and hopeful tone."
        root.config(bg= "lightgreen")
    elif sentiment.polarity < -0.1:
        result = "This poem carries a sad and hopeless tone."
        root.config(bg= "lightcoral")
    else:
        result = "This poem carries a calm and neutral tone."
        root.config(bg= "lightgray")
    
    output_label.config(text = f"Polarity: {sentiment.polarity:.2f}\n{result}")

analyze_button = tk.Button(root, text="Analyze", command=analyze_poem)
analyze_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=10)

root.mainloop()
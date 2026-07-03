from textblob import TextBlob
import tkinter as tk
import matplotlib.pyplot as plt

#make it line by line analysis of emotion. with bar graph or piechart.

root = tk.Tk()
root.title("ANALYSISING EMOTION OF THE TEXT")
root.geometry("500x500")

label = tk.Label(root, text = "emotion analysis of text and get the number of words", font = ("Arial",15))
label.pack(pady = 10)

text_box = tk.Text(root, height = 5)
text_box.pack(pady = 10)

def analyze_text():
    poem_text = text_box.get("1.0",tk.END).strip()
    lines = poem_text.split(".")
    for line in lines:
        blob = TextBlob(line)
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
            
    output_label.config(
        text = f"Polarity: {sentiment.polarity:.2f}\n"
        f"Subjectivity: {sentiment.subjectivity:.2f}\n"
        f"{result}")


def number_of_words():
    words = text_box.get("1.0",tk.END).strip()
    count = 0
    if not words:
        count = 0
    else:
        word = words.split()
        count += len(word)

    result_label.config(text = f"words: {count}")


def the_graph():
    poem_text = text_box.get("1.0",tk.END).strip()
    lines = poem_text.split(".")

    line_numbers = []
    polarities = []
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
        blob = TextBlob(line)
        line_numbers.append(i+1)
        polarities.append(blob.sentiment.polarity)

    colors = []
    for p in polarities:
        if p > 0.1:
            colors.append("green")
        elif p < -0.1:
            colors.append("red")
        else:
            colors.append("gray")

    plt.bar(line_numbers, polarities,color = colors)
    plt.xlabel("Line Number")
    plt.ylabel("Polarity")
    plt.title("Emotion of Each Line")
    plt.ylim(-1,1)
    plt.show()


analyze_button = tk.Button(root, text="Analyze", command=analyze_text)
analyze_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=10)

result_label = tk.Label(root, text="Words: 0", font= ("Arial",15))
result_label.pack(pady = 25)

button = tk.Button(root, text = "words", font = ("Arial",15), command = number_of_words)
button.pack(padx =30, pady = 15)

graph_button = tk.Button(root, text="for graph", font=("Arial",15), command= the_graph)
graph_button.pack(padx=30,pady = 25)

root.mainloop()
# copilot output, 2024-09-14, query:
# do paths exist to preserve formatting tags from html, restructured text, 
#   or markdown into a formatted python tkinter text widget?

import tkinter as tk
from tkinter import scrolledtext
from html.parser import HTMLParser

class HTMLToTkinter(HTMLParser):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def handle_starttag(self, tag, attrs):
        if tag == 'b':
            self.text_widget.tag_configure('bold', font=('Helvetica', 12, 'bold'))
            self.text_widget.tag_add('bold', 'insert', 'insert +1c')
        elif tag == 'i':
            self.text_widget.tag_configure('italic', font=('Helvetica', 12, 'italic'))
            self.text_widget.tag_add('italic', 'insert', 'insert +1c')

    def handle_endtag(self, tag):
        if tag == 'b':
            self.text_widget.tag_remove('bold', 'insert -1c', 'insert')
        elif tag == 'i':
            self.text_widget.tag_remove('italic', 'insert -1c', 'insert')

    def handle_data(self, data):
        self.text_widget.insert(tk.END, data)

def main():
    root = tk.Tk()
    root.title("HTML to Tkinter Text")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text_widget.pack(padx=10, pady=10)

    html_content = "<b>Bold text</b> and <i>italic text</i>."

    parser = HTMLToTkinter(text_widget)
    parser.feed(html_content)

    root.mainloop()

if __name__ == "__main__":
    main()


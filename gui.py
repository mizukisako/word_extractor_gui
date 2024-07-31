import os
import logging
import argparse
from word_extractor.script.extract_words import extract_words
from tkinter import filedialog, messagebox, Tk, Frame, Button

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def run_extraction():
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        base_name = os.path.splitext(os.path.basename(input_file_path))[0]
        output_file_name = "{}_words.csv".format(base_name)
        dir_path = os.path.dirname(input_file_path) 
        output_file_path = os.path.join(dir_path, output_file_name)
        try:
            args = argparse.Namespace(ifn=input_file_path, ofn=output_file_path, display=False, buffer_size=50)
            print(args)
            extract_words(args)
            messagebox.showinfo("処理完了", "ファイル処理が完了しました。\n{}".format(output_file_path))
            open_file(output_file_path)
        except Exception as e:
            messagebox.showerror("エラー", "エラーが発生しました。\nエラーメッセージ: {}".format(e))

def open_file(file_path):
    try:
        os.startfile(file_path)
    except AttributeError:
        import subprocess
        subprocess.run(["open", file_path], check=True)

if __name__ == "__main__":
    root = Tk()
    root.title("ワード抽出ツール")

    frame = Frame(root)
    frame.pack(padx=100, pady=100)

    Button(frame, text="ファイルを選択して変換", command=run_extraction, width=25).pack(padx=5, pady=5)

    root.mainloop()
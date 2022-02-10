import asyncio
import threading
import tkinter as tk
import tkinter.messagebox as tkm
from time import sleep


class App:

    def __init__(self, root):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self.root = root
        root.title("Countdown sample")
        root.geometry("300x100")
        self.label = tk.Label(root, text="Please press one of the buttons")
        self.label.pack()
        tk.Button(root, text="Countdown start: 3", command=lambda:self.thread_countdown(3, "Call thread_countdown")).pack()
        tk.Button(root, text="Countdown start: 5", command=lambda:loop.run_in_executor(None, self.countdown, 5, "Call countdown")).pack()


    def countdown(self, count, msg):
        countdown_text = "Countdown: "
        for i in range(count, 0, -1):
            self.label["text"] = countdown_text + str(i)
            sleep(1)
        self.label["text"] = countdown_text + "0"
        sleep(1)
        tkm.showinfo("FINISH", msg)


    def thread_countdown(self, count, msg):
        thread = threading.Thread(target=self.countdown, args=(count, msg))
        thread.start()


def main():
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == "__main__":
    main()

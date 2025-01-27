import argparse
from gui.gui import PenTestGUI
from core.engine import PenTestEngine
import tkinter as tk

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Framework")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI")
    args = parser.parse_args()

    if args.gui:
        root = tk.Tk()
        app = PenTestGUI(root)
        root.mainloop()
    else:
        print("Running in CLI mode...")
        engine = PenTestEngine()
        engine.run()

if __name__ == "__main__":
    main()
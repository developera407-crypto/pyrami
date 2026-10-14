import random
import math
import tkinter as tk
import tkinter.messagebox as message
import random
import math
import tkinter as tk
import tkinter.messagebox as message

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Step-by-Step Math Solver")
        self.root.geometry("620x580")
        self.root.configure(bg="#2c3e50")
        
        self.topics = [
            "Algebraic (Linear)",
            "Quadratic Equations",
            "Exponential Equations",
            "Logarithmic Equations",
            "Trigonometric Values",
            "Inverse Trigonometric"
        ]
        
        self.score = 0
        self.current_topic = "Algebraic (Linear)"
        self.steps = []
        self.correct_answer = ""
        
        self.setup_ui()
        self.next_question()

    def setup_ui(self):
        title_lbl = tk.Label(
            self.root, 
            text="🌎🧭 Universal Concept Step Solver 🌎🧭", 
            font=("Helvetica", 16, "bold"), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        title_lbl.pack(pady=15)
        
        topic_frame = tk.Frame(self.root, bg="#2c3e50")
        topic_frame.pack(pady=5)
        
        tk.Label(topic_frame, text="Select Mode: ", font=("Helvetica", 11, "bold"), fg="#ecf0f1", bg="#2c3e50").grid(row=0, column=0, padx=5)
        
        self.topic_var = tk.StringVar(value=self.current_topic)
        topic_menu = tk.OptionMenu(topic_frame, self.topic_var, *self.topics, command=self.change_topic)
        topic_menu.config(font=("Helvetica", 10), bg="#34495e", fg="white", highlightbackground="#2c3e50")
        topic_menu.grid(row=0, column=1, padx=5)
        
        self.score_lbl = tk.Label(
            self.root, 
            text=f"Problems Solved: {self.score}", 
            font=("Helvetica", 12, "bold"), 
            fg="#f1c40f", 
            bg="#2c3e50"
        )
        self.score_lbl.pack(pady=5)

        self.q_lbl = tk.Label(
            self.root, 
            text="", 
            font=("Helvetica", 15, "italic bold"), 
            fg="#e74c3c", 
            bg="#34495e",
            width=42,
            height=4,
            relief="groove",
            bd=3
        )
        self.q_lbl.pack(pady=15)

        self.entry = tk.Entry(self.root, font=("Helvetica", 14), width=22, justify="center", bd=3)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_submission())
        
        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        btn_frame.pack(pady=15)
        
        submit_btn = tk.Button(
            btn_frame, 
            text="Submit Answer", 
            font=("Helvetica", 11, "bold"), 
            bg="#27ae60", 
            fg="white", 
            width=15,
            command=self.check_submission
        )
        submit_btn.grid(row=0, column=0, padx=10)
        
        skip_btn = tk.Button(
            btn_frame, 
            text="Skip", 
            font=("Helvetica", 11, "bold"), 
            bg="#7f8c8d", 
            fg="white", 
            width=15,
            command=self.next_question
        )
        skip_btn.grid(row=0, column=1, padx=10)

    def change_topic(self, selection):
        self.current_topic = selection
        self.next_question()

    def next_question(self):
        self.entry.delete(0, tk.END)
        self.steps = []
        
        if self.current_topic == "Algebraic (Linear)":
            a = random.randint(2, 6)
            b = random.randint(1, 15)
            c = random.randint(20, 45)
            c = c - ((c - b) % a) 
            ans = (c - b) // a
            
            self.question_text = f"Solve for x:\n{a}x + {b} = {c}"
            self.correct_answer = str(ans)
            self.steps = [
                f"Step 1: Isolate the variable term by moving constants. Subtract {b} from both sides:",
                f"       {a}x = {c} - {b}",
                f"       {a}x = {c - b}",
                f"Step 2: Isolate x by dividing both sides by the coefficient ({a}):",
                f"       x = {c - b} / {a}",
                f"       x = {ans} ✔️"
            ]
            
        elif self.current_topic == "Quadratic Equations":
            x1 = random.randint(1, 5)
            x2 = random.randint(1, 6)
            if x1 == x2: x2 += 1
            b = -(x1 + x2)
            c = x1 * x2
            
            b_str = f"- {-b}x" if b < 0 else f"+ {b}x"
            c_str = f"- {-c}" if c < 0 else f"+ {c}"
            
            self.question_text = f"Find the SMALLEST root for x:\nx² {b_str} {c_str} = 0"
            self.correct_answer = str(min(x1, x2))
            self.steps = [
                f"Step 1: Identify numbers that multiply to C ({c}) and add to B ({b}).",
                f"       Those values are {-x1} and {-x2}.",
                f"Step 2: Write in factored structure:",
                f"       (x - {x1})(x - {x2}) = 0",
                f"Step 3: Solve each binomial option for 0:",
                f"       x = {x1} or x = {x2}",
                f"       The minimum solution value is {self.correct_answer}."
            ]

        elif self.current_topic == "Exponential Equations":
            base = random.choice([2, 3, 5, 10]) # Fixed: Added numbers inside choice
            power = random.randint(2, 4)
            result = base ** power
            
            self.question_text = f"Solve exponential power x:\n{base}^x = {result}"
            self.correct_answer = str(power)
            self.steps = [
                f"Step 1: Express the constant {result} using base {base}.",
                f"       {result} can be written as {base}^{power}.",
                f"Step 2: Equate exponents directly since bases align:",
                f"       If {base}^x = {base}^{power}, then x must equal {power}."
            ]

        elif self.current_topic == "Logarithmic Equations":
            base = random.choice([2, 3, 5, 10]) # Fixed: Added numbers inside choice
            ans = random.randint(2, 3)
            val = base ** ans
            
            self.question_text = f"Solve log argument x:\nlog_{base}(x) = {ans}"
            self.correct_answer = str(val)
            self.steps = [
                f"Step 1: Convert logarithmic statement into exponential form.",
                f"       Rule: log_b(x) = y transforms to b^y = x",
                f"Step 2: Substitute values from the problem:",
                f"       {base}^{ans} = x",
                f"Step 3: Evaluate:",
                f"       x = {val}"
            ]

        elif self.current_topic == "Trigonometric Values":
            angle = random.choice([0, 30, 45, 60, 90])
            func = random.choice(["sin", "cos"])
            self.question_text = f"Find numerical value:\n{func}({angle}°)"
            
            if func == "sin":
                mapping = {0: "0", 30: "0.5", 45: "0.71", 60: "0.87", 90: "1"}
            else:
                mapping = {0: "1", 30: "0.87", 45: "0.71", 60: "0.5", 90: "0"}
                
            self.correct_answer = mapping[angle]
            self.steps = [
                f"Concept Check: Evaluate coordinates along standard Unit Circle values.",
                f"For {func}({angle}°):",
                f"The value yields {self.correct_answer}.",
                f"(Note: Values like √2/2 and √3/2 are rounded to 0.71 and 0.87)"
            ]

        elif self.current_topic == "Inverse Trigonometric":
            val_choice = random.choice(["0", "0.5", "1"])
            self.question_text = f"Find angle in degrees (θ):\narcsin({val_choice})"
            
            mapping = {"0": "0", "0.5": "30", "1": "90"}
            self.correct_answer = mapping[val_choice]
            self.steps = [
                f"Step 1: Understand inverse logic functionality.",
                f"       arcsin({val_choice}) = θ converts to finding where sin(θ) = {val_choice}.",
                f"Step 2: Reference Principal Quadrant 1 ranges:",
                f"       sin({self.correct_answer}°) = {val_choice}.",
                f"Therefore, θ = {self.correct_answer}°"
            ]

        self.q_lbl.config(text=self.question_text)

    def check_submission(self):
        user_input = self.entry.get().strip()
        try:
            is_correct = (float(user_input) == float(self.correct_answer))
        except ValueError:
            is_correct = (user_input.lower() == self.correct_answer.lower())

        if is_correct:
            self.score += 1
            self.score_lbl.config(text=f"Problems Solved: {self.score}")
            message.showinfo(
                title="✨ Correct Answer! ✨",
                message="🎂 Excellent work! Success. Let's inspect the math derivation.",
                icon="question"
            )
            self.display_steps_window(is_winner=True)
        else:
            message.showerror(
                title="😢 Incorrect 👎",
                message="Let's study the clear step-by-step layout below to clear up concepts!",
                icon="error"
            )
            self.display_steps_window(is_winner=False)

    def display_steps_window(self, is_winner):
        explain_win = tk.Toplevel(self.root)
        explain_win.title("Step-by-Step Concept Breakdown")
        explain_win.geometry("520x400")
        explain_win.configure(bg="#34495e")
        
        lbl_text = "🎉 Perfect Calculation! Breakdown:" if is_winner else "💡 Concept Strategy Walkthrough:"
        lbl_color = "#2ecc71" if is_winner else "#f1c40f"
        
        tk.Label(explain_win, text=lbl_text, font=("Helvetica", 13, "bold"), fg=lbl_color, bg="#34495e").pack(pady=10)
        
        txt_box = tk.Text(explain_win, font=("Consolas", 11), bg="#2c3e50", fg="#ecf0f1", wrap="word", bd=2, padx=10, pady=10)
        txt_box.pack(padx=15, pady=5, fill="both", expand=True)
        
        full_story = f"Problem Given:\n{self.question_text}\n\n" + "\n".join(self.steps)
        txt_box.insert(tk.END, full_story)
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MathApp(root)
#     root.mainloop()

import tkinter as tk
import tkinter.messagebox as message
from tkinter import ttk
import math
import sympy as sp

class UniversalMathSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NexusStep - AI Mathematical Engine")
        self.root.geometry("700x650")
        self.root.configure(bg="#1a252f")
        
        # UI Styling Elements
        self.bg_main = "#1a252f"
        self.bg_card = "#2c3e50"
        self.text_light = "#ecf0f1"
        self.accent_green = "#27ae60"
        self.accent_blue = "#2980b9"
        
        self.setup_ui()

    def setup_ui(self):
        # Header Canvas/Frame
        header_lbl = tk.Label(
            self.root, 
            text="🌎🧭 NEXUSSTEP MULTI-MODULE SOLVER 🌎🧭", 
            font=("Helvetica", 16, "bold"), 
            fg=self.text_light, 
            bg=self.bg_main
        )
        header_lbl.pack(pady=15)
        
        # Helpful Format Cheat Sheet Card
        hint_frame = tk.LabelFrame(
            self.root, 
            text=" Mathematical Syntax Guide ", 
            font=("Helvetica", 10, "bold"),
            fg="#f1c40f", 
            bg=self.bg_card, 
            bd=2, 
            padx=10, 
            pady=8
        )
        hint_frame.pack(padx=20, pady=5, fill="x")
        
        hints = (
            "• Algebraic/Quadratic:  x**2 - 5*x + 6 = 0  (Use * for multiplication, ** for power)\n"
            "• Exponential:          3**x = 81\n"
            "• Logarithmic:          log(x, 2) = 3   (Format: log(variable, base))\n"
            "• Trigonometric:        sin(pi/3) or cos(x) = 0.5\n"
            "• Inverse Trig:         asin(0.5) or acos(1)"
        )
        tk.Label(hint_frame, text=hints, font=("Consolas", 10), fg=self.text_light, bg=self.bg_card, justify="left").pack(anchor="w")

        # Core Input Section
        input_frame = tk.Frame(self.root, bg=self.bg_main)
        input_frame.pack(pady=20, fill="x", padx=30)
        
        tk.Label(input_frame, text="Type Expression / Equation:", font=("Helvetica", 12, "bold"), fg=self.text_light, bg=self.bg_main).pack(anchor="w", pady=2)
        
        self.entry = tk.Entry(input_frame, font=("Consolas", 14), bg=self.bg_card, fg=self.text_light, insertbackground="white", bd=20, relief="flat")
        self.entry.pack(fill="x", ipady=8, pady=5)
        self.entry.bind("<Return>", lambda e: self.solve_custom_question())
        
        # Action Layout Control
        btn_frame = tk.Frame(self.root, bg=self.bg_main)
        btn_frame.pack(pady=5)
        
        solve_btn = tk.Button(
            btn_frame, 
            text="🚀 Solve Step-by-Step", 
            font=("Helvetica", 12, "bold"), 
            bg=self.accent_green, 
            fg="white", 
            padx=20, 
            pady=6,
            relief="flat",
            command=self.solve_custom_question
        )
        solve_btn.pack(side="left", padx=10)
        
        clear_btn = tk.Button(
            btn_frame, 
            text="Clear", 
            font=("Helvetica", 12, "bold"), 
            bg="#7f8c8d", 
            fg="white", 
            padx=15, 
            pady=6,
            relief="flat",
            command=lambda: self.entry.delete(0, tk.END)
        )
        clear_btn.pack(side="left", padx=10)

        # Output Output Presentation Log Screen
        output_frame = tk.Frame(self.root, bg=self.bg_main)
        output_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        tk.Label(output_frame, text="Execution & Mathematical Concept Derivation Log:", font=("Helvetica", 11, "bold"), fg="#3498db", bg=self.bg_main).pack(anchor="w")
        
        # Scrollable Dynamic Output Box
        self.txt_output = tk.Text(output_frame, font=("Consolas", 11), bg="#1c2833", fg="#2ecc71", wrap="word", bd=3, padx=10, pady=10)
        self.txt_output.pack(fill="both", expand=True, pady=5)
        
    def solve_custom_question(self):
        raw_input = self.entry.get().strip()
        if not raw_input:
            message.showwarning("Empty Submission", "Please write or enter a valid mathematical equation.")
            return
            
        self.txt_output.config(state="normal")
        self.txt_output.delete("1.0", tk.END)
        
        try:
            # Setup Variable Context Environment
            x, y, z = sp.symbols('x y z')
            local_dict = {
                'x': x, 'y': y, 'z': z,
                'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                'log': sp.log, 'exp': sp.exp, 'pi': sp.pi, 'E': sp.E
            }
            
            steps_log = []
            steps_log.append(f"📥 Input Parsed: {raw_input}\n")
            
            # Scenario A: User submitted a balanced equation containing '='
            if "=" in raw_input:
                left_side, right_side = raw_input.split("=")
                lhs = sp.parse_expr(left_side, local_dict=local_dict)
                rhs = sp.parse_expr(right_side, local_dict=local_dict)
                
                # Transform equation to standard global expression = 0 form
                expression = lhs - rhs
                steps_log.append(f"Step 1: Balance terms into standard form (Equate to zero):")
                steps_log.append(f"       ({lhs}) - ({right_side.strip()}) = 0")
                steps_log.append(f"       Simplified Expression: {expression} = 0\n")
                
                # Dynamic Topic Categorization Architecture
                steps_log.append("Step 2: Detect Equation Characteristics & Core Properties:")
                if expression.has(sp.sin, sp.cos, sp.tan):
                    steps_log.append("       -> Categorized as Trigonometric Equation Model.")
                elif expression.has(sp.asin, sp.acos, sp.atan):
                    steps_log.append("       -> Categorized as Inverse Trigonometric Model.")
                elif expression.has(sp.log):
                    steps_log.append("       -> Categorized as Logarithmic Structural Formula.")
                elif x in expression.free_symbols and sp.degree(expression, gen=x) == 2:
                    steps_log.append("       -> Categorized as standard 2nd-degree Quadratic Equation.")
                    # Show factoring steps if simple quadratic
                    try:
                        factored = sp.factor(expression)
                        steps_log.append(f"       -> Extracted Factored Form: {factored} = 0")
                    except:
                        pass
                else:
                    steps_log.append("       -> Categorized as standard Algebraic Matrix/Relationship Expression.")
                
                # Execute symbolic structural solver calculations
                solutions = sp.solve(expression, x)
                
                steps_log.append(f"\nStep 3: Solve algebraically via functional substitution paths:")
                steps_log.append(f"       Roots found for variable (x):")
                if not solutions:
                    steps_log.append("       -> No clear symbolic solutions found.")
                else:
                    for i, sol in enumerate(solutions, start=1):
                        approx = float(sol.evalf()) if sol.is_AlgebraicNumber or sol.is_real or isinstance(sol, sp.Number) else "N/A"
                        steps_log.append(f"       Answer Solution #{i}:  x = {sol}   (Decimal approx: {approx})")
            
            # Scenario B: Single input expression without "=" (Evaluate directly)
            else:
                expr = sp.parse_expr(raw_input, local_dict=local_dict)
                steps_log.append("Step 1: Parse functional expression variables directly.")
                steps_log.append(f"       Parsed Structure: {expr}\n")
                
                steps_log.append("Step 2: Simplify and evaluate matching mathematical laws:")
                simplified = sp.simplify(expr)
                steps_log.append(f"       Simplified Representation: {simplified}")
                
                # Attempt decimal output extraction
                try:
                    numeric_eval = expr.evalf()
                    steps_log.append(f"       Evaluated Numeric Output: {numeric_eval}")
                except:
                    pass
            
            # Print steps to console UI box
            self.txt_output.insert(tk.END, "\n".join(steps_log))
            
        except Exception as err:
            self.txt_output.insert(tk.END, f"❌ Engine Processing Failure:\nCould not process expression. Check your layout syntax.\n\nError details: {str(err)}")
            
        self.txt_output.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalMathSolverApp(root)
    root.mainloop()

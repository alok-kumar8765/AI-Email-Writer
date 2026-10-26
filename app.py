import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
# import mysql.connector  # UNCOMMENT WHEN USING MYSQL IN THE FUTURE
# from openai import OpenAI  # UNCOMMENT WHEN USING OPENAI IN THE FUTURE

# ==========================================
# 1. LOCAL DATA STORAGE & AI SIMULATION
# ==========================================
# In-memory local database (acts as local storage for now)
local_email_db = [
    {
        "id": 1, 
        "to": "hr@techcorp.com", 
        "subject": "Data Analyst Job Application", 
        "body": "Dear Hiring Team,\n\nI am writing to express my interest in the Data Analyst position...", 
        "status": "Draft", 
        "date": "2026-10-16 10:45"
    },
    {
        "id": 2, 
        "to": "recruiter@datasoft.com", 
        "subject": "Follow-up for Interview", 
        "body": "Hi Recruiter,\n\nJust following up on my previous interview status...", 
        "status": "Sent", 
        "date": "2026-10-14 16:20"
    },
    {
        "id": 3, 
        "to": "hr@globaltech.com", 
        "subject": "Resume Submission", 
        "body": "Dear HR,\n\nPlease find my resume attached for review...", 
        "status": "Sent", 
        "date": "2026-10-10 11:30"
    },
    {
        "id": 4, 
        "to": "careers@innovate.ai", 
        "subject": "Inquiry about Openings", 
        "body": "Hello,\n\nI would like to inquire about open engineering roles...", 
        "status": "Draft", 
        "date": "2026-10-08 09:15"
    },
    {
        "id": 5, 
        "to": "hiring@cloudsys.com", 
        "subject": "Follow-up Email", 
        "body": "Dear Hiring Manager,\n\nChecking in regarding my application...", 
        "status": "Sent", 
        "date": "2026-10-05 15:40"
    }
]

def generate_email(subject, purpose, tone):
    """
    Generates professional email content using fallback templates or AI.
    """
    # --- MYSQL / OPENAI PLACEHOLDERS (FOR FUTURE USE) ---
    """
    -- MySQL Table Schema (Run later):
    CREATE TABLE IF NOT EXISTS emails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        to_email VARCHAR(255) NOT NULL,
        subject VARCHAR(255) NOT NULL,
        body TEXT NOT NULL,
        status VARCHAR(50) DEFAULT 'Draft',
        sent_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    generated_body = f"""Dear Hiring Team,\n\nI hope this email finds you well. I am writing to you regarding: {subject}.\n\n{purpose}\n\nI would appreciate the opportunity to discuss how my background aligns with your requirements. Thank you for your time and consideration.\n\nBest regards,\nAkshat Singh Rajput\nData Analyst | 5+ Years Experience"""
    return generated_body


# ==========================================
# 2. TKINTER GUI APPLICATION
# ==========================================
class EmailWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Email Writer & Follow-up Tool")
        self.root.geometry("1300x850")
        self.root.configure(bg="#f4f6f9")

        # Top Header Frame
        header_frame = tk.Frame(root, bg="#1e293b", height=65)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="✨ AI Email Writer & Follow-up Tool", font=("Arial", 16, "bold"), fg="white", bg="#1e293b")
        title_label.pack(side=tk.LEFT, padx=20, pady=12)
        
        subtitle_label = tk.Label(header_frame, text="Generate professional emails, save history and manage follow-ups (Local Storage Mode)", font=("Arial", 9), fg="#94a3b8", bg="#1e293b")
        subtitle_label.pack(side=tk.LEFT, padx=10, pady=15)

        # Main Scrollable / Container layout
        main_container = tk.Frame(root, bg="#f4f6f9")
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Top Section Split (Inputs vs Generated Output)
        top_split_frame = tk.Frame(main_container, bg="#f4f6f9")
        top_split_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # --- LEFT PANEL (Inputs & Generator) ---
        left_panel = tk.Frame(top_split_frame, bg="white", bd=1, relief=tk.SOLID)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        form_frame = tk.Frame(left_panel, bg="white", padx=15, pady=15)
        form_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(form_frame, text="Recipient Email", font=("Arial", 9, "bold"), bg="white", anchor="w").pack(fill=tk.X)
        self.recipient_entry = tk.Entry(form_frame, font=("Arial", 10), relief=tk.SOLID, bd=1)
        self.recipient_entry.pack(fill=tk.X, pady=(3, 10))
        self.recipient_entry.insert(0, "hr@techcorp.com")

        tk.Label(form_frame, text="Subject", font=("Arial", 9, "bold"), bg="white", anchor="w").pack(fill=tk.X)
        self.subject_entry = tk.Entry(form_frame, font=("Arial", 10), relief=tk.SOLID, bd=1)
        self.subject_entry.pack(fill=tk.X, pady=(3, 10))
        self.subject_entry.insert(0, "Data Analyst Job Application")

        tk.Label(form_frame, text="Purpose / Context", font=("Arial", 9, "bold"), bg="white", anchor="w").pack(fill=tk.X)
        self.purpose_text = tk.Text(form_frame, font=("Arial", 9), height=4, relief=tk.SOLID, bd=1)
        self.purpose_text.pack(fill=tk.X, pady=(3, 10))
        self.purpose_text.insert("1.0", "I want to apply for a Data Analyst role in your company. Highlight my skills in SQL, Python, Power BI and 5 years of experience.")

        tk.Label(form_frame, text="Tone", font=("Arial", 9, "bold"), bg="white", anchor="w").pack(fill=tk.X)
        self.tone_combobox = ttk.Combobox(form_frame, values=["Professional", "Friendly", "Persuasive", "Casual"], font=("Arial", 9), state="readonly")
        self.tone_combobox.pack(fill=tk.X, pady=(3, 15))
        self.tone_combobox.set("Professional")

        generate_btn = tk.Button(form_frame, text="✨ Generate Email with AI", font=("Arial", 10, "bold"), bg="#2563eb", fg="white", cursor="hand2", command=self.on_generate)
        generate_btn.pack(fill=tk.X, ipady=6)

        # --- RIGHT PANEL (Generated Output & Actions) ---
        right_panel = tk.Frame(top_split_frame, bg="white", bd=1, relief=tk.SOLID)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

        output_frame = tk.Frame(right_panel, bg="white", padx=15, pady=15)
        output_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(output_frame, text="Generated Email", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(0, 5))

        self.output_text = tk.Text(output_frame, font=("Arial", 9), wrap=tk.WORD, relief=tk.SOLID, bd=1, height=10)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        default_output = """Subject: Application for Data Analyst Role\n\nDear Hiring Team,\n\nI hope this email finds you well. I am writing to express my interest in the Data Analyst position at TechCorp. With over 5 years of experience in data analysis and strong proficiency in SQL, Python, Power BI and advanced Excel, I am confident in my ability to contribute to your team.\n\nI have attached my resume for your review. I would appreciate the opportunity to discuss how my skills and experience align with your requirements.\n\nThank you for your time and consideration.\n\nBest regards,\nAkshat Singh Rajput"""
        self.output_text.insert("1.0", default_output)

        action_btn_frame = tk.Frame(output_frame, bg="white")
        action_btn_frame.pack(fill=tk.X)

        save_btn = tk.Button(action_btn_frame, text="💾 Save to Local/DB", font=("Arial", 9, "bold"), bg="#16a34a", fg="white", cursor="hand2", command=self.on_save)
        save_btn.pack(side=tk.LEFT, padx=(0, 8), ipadx=8, ipady=4)

        copy_btn = tk.Button(action_btn_frame, text="📋 Copy Email", font=("Arial", 9, "bold"), bg="#0284c7", fg="white", cursor="hand2", command=self.on_copy)
        copy_btn.pack(side=tk.LEFT, padx=(0, 8), ipadx=8, ipady=4)

        clear_btn = tk.Button(action_btn_frame, text="🗑 Clear", font=("Arial", 9, "bold"), bg="#64748b", fg="white", cursor="hand2", command=self.on_clear)
        clear_btn.pack(side=tk.LEFT, ipadx=8, ipady=4)


        # ==========================================
        # 3. BOTTOM PANEL: SENT EMAILS / HISTORY TABLE
        # ==========================================
        history_outer_frame = tk.Frame(main_container, bg="white", bd=1, relief=tk.SOLID)
        history_outer_frame.pack(fill=tk.BOTH, expand=True)

        history_header_frame = tk.Frame(history_outer_frame, bg="white", padx=15, pady=10)
        history_header_frame.pack(fill=tk.X)

        tk.Label(history_header_frame, text="Sent Emails / Follow-up History", font=("Arial", 11, "bold"), bg="white").pack(side=tk.LEFT)

        # Search bar on top right of table
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_history)
        search_entry = tk.Entry(history_header_frame, textvariable=self.search_var, font=("Arial", 9), relief=tk.SOLID, bd=1, width=25)
        search_entry.pack(side=tk.RIGHT)
        tk.Label(history_header_frame, text="🔍 Search: ", font=("Arial", 9), bg="white").pack(side=tk.RIGHT, padx=5)

        # Table & Scrollbar
        table_frame = tk.Frame(history_outer_frame, bg="white", padx=15, pady=15)
        table_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("id", "to", "subject", "status", "date")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="extended", height=6)
        
        self.tree.heading("id", text="ID")
        self.tree.heading("to", text="To Email")
        self.tree.heading("subject", text="Subject")
        self.tree.heading("status", text="Status")
        self.tree.heading("date", text="Sent Date")

        self.tree.column("id", width=40, anchor=tk.CENTER)
        self.tree.column("to", width=200, anchor=tk.W)
        self.tree.column("subject", width=350, anchor=tk.W)
        self.tree.column("status", width=90, anchor=tk.CENTER)
        self.tree.column("date", width=150, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Table Action Buttons (Edit, Send, Delete Selected)
        table_btn_frame = tk.Frame(history_outer_frame, bg="white", padx=15, pady= 15)
        table_btn_frame.pack(fill=tk.X)

        edit_row_btn = tk.Button(table_btn_frame, text="✏️ Edit Selected", font=("Arial", 9, "bold"), bg="#d97706", fg="white", cursor="hand2", command=self.on_edit_selected)
        edit_row_btn.pack(side=tk.LEFT, padx=(0, 8), ipadx=8, ipady=4)

        send_row_btn = tk.Button(table_btn_frame, text="🚀 Send Selected", font=("Arial", 9, "bold"), bg="#059669", fg="white", cursor="hand2", command=self.on_send_selected)
        send_row_btn.pack(side=tk.LEFT, padx=(0, 8), ipadx=8, ipady=4)

        delete_row_btn = tk.Button(table_btn_frame, text="🗑 Delete Selected", font=("Arial", 9, "bold"), bg="#dc2626", fg="white", cursor="hand2", command=self.on_delete_selected)
        delete_row_btn.pack(side=tk.LEFT, ipadx=8, ipady=4)

        # Load initial data into table
        self.populate_table(local_email_db)

    def populate_table(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in data:
            self.tree.insert("", tk.END, values=(item["id"], item["to"], item["subject"], item["status"], item["date"]))

    def filter_history(self, *args):
        query = self.search_var.get().lower()
        filtered = [
            item for item in local_email_db 
            if query in item["to"].lower() or query in item["subject"].lower() or query in item["status"].lower()
        ]
        self.populate_table(filtered)

    def on_generate(self):
        subject = self.subject_entry.get()
        purpose = self.purpose_text.get("1.0", tk.END).strip()
        tone = self.tone_combobox.get()
        
        if not subject or not purpose:
            messagebox.showwarning("Warning", "Please provide both Subject and Purpose.")
            return

        email_content = generate_email(subject, purpose, tone)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", email_content)

    def on_save(self):
        to_email = self.recipient_entry.get()
        subject = self.subject_entry.get()
        body = self.output_text.get("1.0", tk.END).strip()
        
        if not to_email or not subject or not body:
            messagebox.showerror("Error", "Please fill in all required fields!")
            return

        new_id = max([item["id"] for item in local_email_db], default=0) + 1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        new_entry = {
            "id": new_id,
            "to": to_email,
            "subject": subject,
            "body": body,
            "status": "Draft",
            "date": current_time
        }

        local_email_db.insert(0, new_entry)
        self.populate_table(local_email_db)
        messagebox.showinfo("Success", "Email saved successfully to local history!")

    def on_copy(self):
        email_content = self.output_text.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(email_content)
        messagebox.showinfo("Copied", "Generated email copied to clipboard successfully!")

    def on_clear(self):
        self.recipient_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.purpose_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def on_edit_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select an email from the table to edit.")
            return
        
        # Get first selected item ID
        item_values = self.tree.item(selected_items[0], "values")
        email_id = int(item_values[0])

        # Find matching record in local list
        record = next((item for item in local_email_db if item["id"] == email_id), None)
        if record:
            self.recipient_entry.delete(0, tk.END)
            self.recipient_entry.insert(0, record["to"])
            self.subject_entry.delete(0, tk.END)
            self.subject_entry.insert(0, record["subject"])
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", record["body"])
            messagebox.showinfo("Loaded", f"Loaded email ID {email_id} into the editor.")

    def on_send_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select email(s) to send.")
            return

        for item_id in selected_items:
            item_values = self.tree.item(item_id, "values")
            email_id = int(item_values[0])
            for item in local_email_db:
                if item["id"] == email_id:
                    item["status"] = "Sent"
                    item["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")

        self.populate_table(local_email_db)
        messagebox.showinfo("Success", "Selected email(s) status updated to Sent!")

    def on_delete_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select email(s) to delete.")
            return

        if not messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected email(s)?"):
            return

        ids_to_delete = []
        for item_id in selected_items:
            item_values = self.tree.item(item_id, "values")
            ids_to_delete.append(int(item_values[0]))

        global local_email_db
        local_email_db = [item for item in local_email_db if item["id"] not in ids_to_delete]
        self.populate_table(local_email_db)
        messagebox.showinfo("Deleted", "Selected email(s) have been deleted.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailWriterApp(root)
    root.mainloop()
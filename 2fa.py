import tkinter as tk
from tkinter import messagebox

import pyotp

# 主题色
PRIMARY = "#1a3a6b"
PRIMARY_HOVER = "#254d8a"
BG = "#ffffff"
LABEL_FG = "#1a3a6b"
REQUIRED = "#e53935"


class TwoFAApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("2FA 验证码生成器")
        self.root.geometry("520x560")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self._secret_placeholder = "BK5V TVQ7 D2RB..."
        self._code_placeholder = "ABC|2FA Code"

        self._build_ui()

    def _build_ui(self):
        padx = 28

        # --- 2FA Secret ---
        secret_label = tk.Frame(self.root, bg=BG)
        secret_label.pack(anchor="w", padx=28, pady=(28, 8))
        tk.Label(
            secret_label,
            text="🔑  2FA Secret",
            font=("Microsoft YaHei UI", 12, "bold"),
            fg=LABEL_FG,
            bg=BG,
        ).pack(side="left")
        tk.Label(
            secret_label,
            text=" *",
            font=("Microsoft YaHei UI", 12, "bold"),
            fg=REQUIRED,
            bg=BG,
        ).pack(side="left")

        self.secret_text = tk.Text(
            self.root,
            height=5,
            font=("Consolas", 11),
            relief="solid",
            bd=1,
            wrap="word",
            fg="#999999",
        )
        self.secret_text.pack(fill="x", padx=padx, pady=(0, 12))
        self.secret_text.insert("1.0", self._secret_placeholder)
        self.secret_text.bind("<FocusIn>", self._on_secret_focus_in)
        self.secret_text.bind("<FocusOut>", self._on_secret_focus_out)

        self._make_button("🔄  Submit", self.generate_code).pack(
            fill="x", padx=28, pady=(0, 28)
        )

        # --- 2FA Code ---
        code_label = tk.Frame(self.root, bg=BG)
        code_label.pack(anchor="w", padx=28, pady=(0, 8))
        tk.Label(
            code_label,
            text="📱  2FA Code",
            font=("Microsoft YaHei UI", 12, "bold"),
            fg=LABEL_FG,
            bg=BG,
        ).pack(side="left")
        tk.Label(
            code_label,
            text=" *",
            font=("Microsoft YaHei UI", 12, "bold"),
            fg=REQUIRED,
            bg=BG,
        ).pack(side="left")

        self.code_text = tk.Text(
            self.root,
            height=5,
            font=("Consolas", 14, "bold"),
            relief="solid",
            bd=1,
            wrap="word",
            fg="#999999",
            state="disabled",
        )
        self.code_text.pack(fill="x", padx=padx, pady=(0, 12))

        self._make_button("📋  Copy", self.copy_code).pack(
            fill="x", padx=28, pady=(0, 28)
        )

    def _make_button(self, text: str, command):
        btn = tk.Button(
            self.root,
            text=text,
            command=command,
            font=("Microsoft YaHei UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            activeforeground="white",
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=10,
        )
        btn.bind("<Enter>", lambda _e: btn.configure(bg=PRIMARY_HOVER))
        btn.bind("<Leave>", lambda _e: btn.configure(bg=PRIMARY))
        return btn

    def _on_secret_focus_in(self, _event):
        if self.secret_text.get("1.0", "end-1c") == self._secret_placeholder:
            self.secret_text.delete("1.0", "end")
            self.secret_text.configure(fg="#000000")

    def _on_secret_focus_out(self, _event):
        if not self.secret_text.get("1.0", "end-1c").strip():
            self.secret_text.insert("1.0", self._secret_placeholder)
            self.secret_text.configure(fg="#999999")

    def _get_secret(self) -> str:
        raw = self.secret_text.get("1.0", "end-1c").strip()
        if raw == self._secret_placeholder:
            return ""
        return raw.replace(" ", "").upper()

    def generate_code(self):
        secret = self._get_secret()
        if not secret:
            messagebox.showwarning("提示", "请输入 2FA Secret")
            return

        try:
            code = pyotp.TOTP(secret).now()
        except Exception as exc:
            messagebox.showerror("错误", f"Secret 格式错误：{exc}")
            return

        self.code_text.configure(state="normal", fg="#000000")
        self.code_text.delete("1.0", "end")
        self.code_text.insert("1.0", code)
        self.code_text.configure(state="disabled")

    def copy_code(self):
        self.code_text.configure(state="normal")
        code = self.code_text.get("1.0", "end-1c").strip()
        self.code_text.configure(state="disabled")

        if not code or code == self._code_placeholder:
            messagebox.showwarning("提示", "请先生成 2FA Code")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        self.root.update()
        messagebox.showinfo("提示", "已复制到剪贴板")


def main():
    root = tk.Tk()
    TwoFAApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

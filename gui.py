from tkinter import filedialog, messagebox, ttk, VERTICAL, Scrollbar
import customtkinter
from PIL import Image
from tkinter.filedialog import askopenfile
from prettytable import PrettyTable

import lexer
import syntax


def command_upload():
    file_path = filedialog.askopenfilename(initialdir='/documents', title='Select a File', filetypes=(("FirstByte files", "*.fb"),))

    if not file_path:
        messagebox.showerror("Error", "No file selected. Please select a file.")

    elif file_path.endswith(".fb"):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                code = file.read()  # Read the contents of the file

                # Insert code into the textbox
                textbox_code.delete(1.0, "end")  # Clear previous content if any
                textbox_code.insert("end", code)  # Insert the code from the file
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

    else:
        messagebox.showerror("Error", "Please select .fb file")


def command_color(home, mode_dark):
    if mode_dark:
        mode_dark = False
        window.configure(fg_color="#FFFFFF")
        label_logo.configure(image=img_logo_light)
        textbox_code.configure(fg_color="#F2F2F2", text_color="#1E1E1E")
        frame_result.configure(fg_color="#FFFFFF")
        button_upload.configure(fg_color="#000000")
        button_switch.configure(image=img_dark, command=lambda: command_color(home, mode_dark))

        if home:
            button_upload.configure(fg_color="#000000", hover_color="#4D4D4D")

        else:
            button_new.configure(fg_color="#000000", hover_color="#4D4D4D")

    else:
        mode_dark = True
        window.configure(fg_color="#171717")
        label_logo.configure(image=img_logo_dark)
        textbox_code.configure(fg_color="#292929", text_color="#FFFFFF")
        button_switch.configure(image=img_light, command=lambda: command_color(home, mode_dark))
        button_upload.configure(fg_color="#FFFFFF")
        frame_result.configure(fg_color="#171717")

        if home:
            button_upload.configure(fg_color="#FFFFFF", hover_color="#DCDCDC")

        else:
            button_new.configure(fg_color="#FFFFFF", hover_color="#DCDCDC")


def export_symboltable(tokens):
    with open("SymbolTable.txt", "w") as file:
        table = PrettyTable()
        table.field_names = (['Lexeme', 'Token'])

        for token, lexeme in tokens:
            table.add_row([lexeme, token])

        table = str(table)
        file.write(table)

    messagebox.showinfo("Export Successful", "Symbol Table exported to SymbolTable.txt")


def export_syntax(tokens):
    with open("SyntaxAnalyzer.txt", "w") as file:
        table = PrettyTable()
        table.field_names = (['Code', 'Validation Result'])

        for token, lexeme in tokens:
            table.add_row([lexeme, token])

        table = str(table)
        file.write(table)

    messagebox.showinfo("Export Successful", "Syntax Analyzer exported to SyntaxAnalyzer.txt")


def command_lexical():
    global home
    home = False

    # Get content from textbox
    content = textbox_code.get("1.0", "end-1c")

    # Check if the content is empty
    if not content:
        messagebox.showerror("Error", "Please type a code")
    else:
        textbox_code.configure(state="disabled")
        button_switch.place(x=1414, y=85)
        button_lexical.place_forget()
        button_upload.place_forget()
        button_syntax.place_forget()

        global button_new, button_export
        button_new = customtkinter.CTkButton(window, text="New Code", font=("Arial", 13, "bold"),
                                             corner_radius=10, height=32, width=132,
                                             fg_color="#FFFFFF", text_color="#75C752", hover_color="#DCDCDC",
                                             command=command_new)
        button_new.place(x=1140, y=85)

        global mode_dark
        button_switch.configure(command=lambda: command_color(home, mode_dark))

        code = textbox_code.get("0.0", "end")
        result = lexer.main(code)


        for token in result:
            token_type, lexeme = token[0], token[1]
            if token_type != "NEWLINE" and token_type != "WHITESPACE" and token_type != "INDENT":
                print(token_type)
                table_result.insert('', 'end', values=(lexeme, token_type))

        button_export = customtkinter.CTkButton(window,
                                                text="Export", font=("Arial", 13, "bold"),
                                                corner_radius=10, height=32, width=132,
                                                fg_color="#75C752", hover_color="#5F9F44",
                                                command=lambda: export_symboltable(result))
        button_export.place(x=1277, y=85)

    table_result.heading('Lexemes', text='Lexemes')
    table_result.heading('Token', text='Token')


def command_syntax():
    global home
    home = False

    # Get content from textbox
    content = textbox_code.get("1.0", "end-1c")

    # Check if the content is empty
    if not content:
        messagebox.showerror("Error", "Please type a code")
    else:
        textbox_code.configure(state="disabled")
        button_switch.place(x=1414, y=85)
        button_lexical.place_forget()
        button_upload.place_forget()
        button_syntax.place_forget()

        global button_new, button_export
        button_new = customtkinter.CTkButton(window, text="New Code", font=("Arial", 13, "bold"),
                                             corner_radius=10, height=32, width=132,
                                             fg_color="#FFFFFF", text_color="#75C752", hover_color="#DCDCDC",
                                             command=command_new)
        button_new.place(x=1140, y=85)

        global mode_dark
        button_switch.configure(command=lambda: command_color(home, mode_dark))

        code = textbox_code.get("0.0", "end")
        result = lexer.call_syntax(code)


        button_export = customtkinter.CTkButton(window,
                                                text="Export", font=("Arial", 13, "bold"),
                                                corner_radius=10, height=32, width=132,
                                                fg_color="#75C752", hover_color="#5F9F44",
                                                command=lambda: export_syntax(result))
        button_export.place(x=1277, y=85)

        if len(result) == 0:
            messagebox.showinfo("ANGAS MO LODS!", "yazz kweenn slayy pur pur")

        else:
            messagebox.showerror("BONAK!", "ayusin mo kasi syntax mong bonak ka")

            for token in result:
                line, code, error = token[0], token[1], token[2]
                table_result.insert('', 'end', values=(line, code, error))

    table_result.heading('Lexemes', text='Code')
    table_result.heading('Token', text='Error Description')


def command_new():
    textbox_code.configure(state="normal")
    textbox_code.delete("1.0", "end")

    # delete treeview -------------------------------------------------------------------- !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    button_new.place_forget()
    button_export.place_forget()
    button_switch.place(x=799, y=85)
    button_upload.place(x=388, y=85)
    button_lexical.place(x=525, y=85)
    button_syntax.place(x=662, y=85)
    table_result.delete(*table_result.get_children())


if __name__ == "__main__":
    # create window and configure its properties
    window = customtkinter.CTk(fg_color="#171717")
    window.title("FirstByte - Lexical and Syntax Analyzer")

    # set dark mode to true
    mode_dark = True
    home = True

    # get the user's screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the center coordinates
    center_x = int((screen_width - 1540) / 2)
    center_y = int((screen_height - 860) / 2)

    window.geometry(f"1520x780+{center_x}+{center_y}")
    window.resizable(0, 0)

    img_logo_dark = customtkinter.CTkImage(light_image=Image.open("logo-dark.png"),
                                           size=(219, 59))

    img_logo_light = customtkinter.CTkImage(light_image=Image.open("logo-light.png"),
                                            size=(219, 59))

    label_logo = customtkinter.CTkLabel(window, image=img_logo_dark, text="")
    label_logo.place(x=71, y=65)

    textbox_code = customtkinter.CTkTextbox(window, width=780, height=577, fg_color="#292929", text_color="#FFFFFF",
                                            font=("Consolas", 16))
    textbox_code.place(x=62, y=141)

    button_upload = customtkinter.CTkButton(window,
                                            text="Upload Code", font=("Arial", 13, "bold"),
                                            corner_radius=10, height=32, width=132,
                                            fg_color="#FFFFFF", text_color="#75C752", hover_color="#DCDCDC",
                                            command=command_upload)
    button_upload.place(x=388, y=85)

    button_lexical = customtkinter.CTkButton(window,
                                             text="Lexical Analyzer", font=("Arial", 13, "bold"),
                                             corner_radius=10, height=32, width=132,
                                             fg_color="#75C752", hover_color="#5F9F44", command=command_lexical)
    button_lexical.place(x=525, y=85)

    button_syntax = customtkinter.CTkButton(window,
                                            text="Syntax Analyzer", font=("Arial", 13, "bold"),
                                            corner_radius=10, height=32, width=132,
                                            fg_color="#548F3B", hover_color="#5F9F44", command=command_syntax)
    button_syntax.place(x=662, y=85)

    img_light = customtkinter.CTkImage(light_image=Image.open("button-light.png"),
                                       size=(23, 23))

    img_dark = customtkinter.CTkImage(light_image=Image.open("button-dark.png"),
                                      size=(21, 21))

    button_switch = customtkinter.CTkButton(window, image=img_light, text="", width=15, height=15, border_width=2,
                                            border_color="#7ED957",
                                            corner_radius=10, fg_color="transparent", hover_color="#5F9F44",
                                            command=lambda: command_color(home, mode_dark))
    button_switch.place(x=799, y=85)

    frame_result = customtkinter.CTkFrame(window, width=680, height=577, fg_color="#171717")
    frame_result.place(x=860, y=141)

    global table_result

    # Create a style object
    style = ttk.Style()

    # Configure the style properties for the heading
    style.configure("Custom.Treeview.Heading",
                    font=("Arial", 13, "bold"))

    # Configure the Treeview widget style
    style.configure("Custom.Treeview",
                    font=("Arial", 11),
                    rowheight=30)

    table_result = ttk.Treeview(frame_result, style="Custom.Treeview", columns=('Line', 'Lexemes', 'Token'))
    table_result.heading('#0', text="")
    table_result.column("#0", width=1, minwidth=1)  # Index column
    table_result.heading('Line', text='Line')
    table_result.heading('Lexemes', text='Lexemes')
    table_result.heading('Token', text='Token')
    table_result.column('Line', minwidth=50, width=50)
    table_result.column('Lexemes', minwidth=100, width=270)
    table_result.column('Token', minwidth=100, width=430)
    table_result.place(x=0, y=0)

    scrollbar = Scrollbar(frame_result, orient=VERTICAL, command=table_result.yview)
    table_result.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=740, y=1, height=715)

    # Change the height of the entire table
    table_result['height'] = 23

    window.mainloop()
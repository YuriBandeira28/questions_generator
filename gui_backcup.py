from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton
import gpt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def send(e):
    assunto = str(entry_assunto.get())
    meteria = str(entry_materia.get())
    if assunto != '' or meteria != '':
        
        entry_assunto.delete(0, len(assunto))
        entry_materia.delete(0, len(meteria))
        mesageLabel = gpt.chat(meteria, assunto)

        j= 153.7725372314453
        for i in mesageLabel:
            print(i)
            if len(i) <=88:
                Checkbutton(win, text=i, font=("MontserratRoman SemiBold", 12 * -1), background="#FAF9F6").place(x = 388.86706542968744, y=j,)
            else:
                Checkbutton(win, text=i[:88] + "-\n-" + i[88:-1], font=("MontserratRoman SemiBold", 12 * -1), background="#FAF9F6").place(x = 388.86706542968744, y=j,)
                j+=30
            j+=30
    else:
        print('por favor, insira algo na caixa de texto')
   
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

win = Tk()
win.bind('<Return>', send)
win.geometry("1001x569")
win.configure(bg = "#282A36")
              #C5C5C5")
#282A36 dracula theme


canvas = Canvas(
    win,
    bg = "#282A36",
    height = 569,
    width = 1001,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    352.6417846679687,
    15.525110244750977,
    anchor="nw",
    text="Gerador de Questões",
    #fill="#000000",
    fill="#ffffff",
    font=("MontserratRoman SemiBold", 20 * -1)
)

canvas.create_text(
    30.31093025207514,
    84.27916717529297,
    anchor="nw",
    text="Matéria",
    #fill="#000000",
    fill="#ffffff",
    font=("MontserratRoman SemiBold", 13 * -1)
)

canvas.create_text(
    30.31093025207514,
    167.81906127929688,
    anchor="nw",
    text="Assunto:",
    #fill="#000000",
    fill="#ffffff",
    font=("MontserratRoman SemiBold", 13 * -1)
)

# MATÉRIA
materia_image= PhotoImage(
    file=relative_to_assets("entry_1.png"))
materia_bg = canvas.create_image(
    178.16913032531733,
    117.54727554321289,
    image=materia_image
)
entry_materia = Entry(
    bd=0,
    bg="#FAF9F6",
    fg="#000716",
    highlightthickness=0
)
entry_materia.place(
    x=36.22525835037226,
    y=102.7614517211914,
    width=283.88774394989014,
    height=27.57164764404297
)

# ASSUNTO 
assunto_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
assunto_bg = canvas.create_image(
    178.16913032531733,
    202.56572723388672,
    image=assunto_image
)
entry_assunto = Entry(
    bd=0,
    bg="#FAF9F6",
    fg="#000716",
    highlightthickness=0
)
entry_assunto.place(
    x=36.22525835037226,
    y=187.7799072265625,
    width=283.88774394989014,
    height=27.571640014648438
)

# QUADRO DE QUESTÕES
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    684.0400085449219,
    329.3300018310547,
    image=image_image_1
)

# TEXTO QUESTÕES
canvas.create_text(
    388.86706542968744,
    117.54727172851562,
    anchor="nw",
    text="Questões:",
    fill="#000000",
    font=("MontserratRoman SemiBold", 13 * -1)
)

    
# respostas
# canvas.create_text(
    # 388.86706542968744,
    # 153.7725372314453,
    # anchor="nw",
    # text="Aqui",
    # fill="#000000",
    # font=("MontserratRoman SemiBold", 10 * -1)
# )
# BOTÃO DE ENVIAR
enviar_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
btn_enviar = Button(
    image=enviar_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: send(e=None),
    relief="flat",
    #bg="#C5C5C5"
    bg="#282A36"
    
    
)
btn_enviar.place(
    x=136.02954101562494,
    y=245.44461059570312,
    width=104.97930908203125,
    height=28.093048095703125
)

# BOTÃO DE SALVAR
salvar_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
btn_salvar = Button(
    image=salvar_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#FAF9F6"
    
)
btn_salvar.place(
    x=862.7526245117188,
    y=528.5930786132812,
    width=104.97930908203125,
    height=28.09307861328125
)

# BOTÃO PARA EXPORTAR PRA PDF
pdf_image_3 = PhotoImage(
    file=relative_to_assets("button_3_outra.png"))
btn_pdf = Button(
    image=pdf_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#FAF9F6"
)
btn_pdf.place(
    x=821.0,
    y=529.0,
    width=28.0,
    height=28.0
)


win.resizable(False, False)
win.mainloop()

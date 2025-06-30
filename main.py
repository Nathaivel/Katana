from textual.app import App,ComposeResult
from textual.widgets import TextArea, Label, Input
from textual import events
import sys
import utils
from textual.containers import Horizontal

inival = ""
fname = ""
flist = []
n = len(sys.argv)
i = 1

def readfile(fname):   
    try:                                                  
        with open(fname,'r') as file:                        
            inival = file.read()                              
            file.close()                               
    except FileNotFoundError:                             
        inival = ""

    return inival

if n > 1:
    x = 1
    fname = sys.argv[1]
    
    while x < n:
        flist.append(sys.argv[x])
        x += 1

    inival = readfile(fname)



def savefile(filename,data):
    with open(filename,'w') as file:
        file.write(data)
        file.close()

class Editor(App):
    BINDINGS = [
            ("ctrl+w","self.move('next')","focus on input"),
            ]
    

    def move(q):
        if q == 'next' and  i <= len(flist):
            fname = flist[i]
            i += 1
            inival = readfile(fname)
            self.query_one("#txt").load_text(f"{inival}")

    def compose(self) -> ComposeResult:
        t_area = TextArea.code_editor(id="textarea")


        with Horizontal(id="top"):
            for i in flist:
                yield Label(f"  [bold]{i}[/bold]  ",classes="topbar")



        command_line = Input(id="cmd")

        log = Label("CTRL-S - save   CTRL-H - help",id="logs")

        #yield file_info
        yield t_area
        t_area.load_text(f"{inival}")
        yield log
        yield command_line


    def on_input_submitted(self,message: Input.Submitted):
        self.query_one("#logs").update("Input Submitted")


    def on_mount(self) -> None:
        top = self.query_one("#top")
        logbar = self.query_one("#logs")
        topbar = self.query_one(".topbar")
        topbar.styles.background = "darkgreen"
        logbar.styles.padding = [0,1]
        top.styles.height = "10%"

        topbar.styles.margin = [0,2]

    def on_key(self,event: events.Key) -> None:
        txt = self.query_one("#textarea")
        cmd = self.query_one("#cmd")
        log = self.query_one("#logs")

        nameconfirm = False
 
        if event.key == "ctrl+s":
           #cmd.focus()
           log.update(f"File {fname} saved")
           
           savefile(fname,txt.text)
       
        if event.key == "ctrl+f":   
               log.update("Search in file: ")
               cmd.focus()

               if events.Key.key == "y":
                  txt.focus()

           


if __name__ == "__main__":
    app = Editor()
    app.run()

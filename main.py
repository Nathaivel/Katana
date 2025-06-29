from textual.app import App,ComposeResult
from textual.widgets import TextArea, Label, Input
from textual import events
import sys

inival = ""
if len(sys.argv) > 1:
    fname = sys.argv[1]

    try:
        with open(fname,'r') as file:
           inival = file.read()
           file.close()
    except FileNotFoundError:
        inival = ""




def savefile(filename,data):
    with open(filename,'w') as file:
        file.write(data)
        file.close()

class Editor(App):
    def compose(self) -> ComposeResult:
        t_area = TextArea(id="textarea")
        file_info = Label(f"[bold]{fname}[/bold]",id="topbar")
        command_line = Input(id="cmd")
        log = Label("CTRL-S - save   CTRL-H - help",id="logs")

        yield file_info
        yield t_area
        t_area.load_text(f"{inival}")
        yield log
        yield command_line

    def on_mount(self) -> None:
        logbar = self.query_one("#logs")
        topbar = self.query_one("#topbar")
        topbar.styles.background = "darkgreen"
        topbar.styles.width = 100
        logbar.styles.padding = [0,1]
        

        #topbar.styles.margin = [1,0]

    def on_key(self,event: events.Key) -> None:
        txt = self.query_one("#textarea")
        cmd = self.query_one("#cmd")
        log = self.query_one("#logs")

        nameconfirm = False

        #if event.key == "Enter":
         #   nameconfirm = True
        
        if event.key == "ctrl+s":
           #cmd.focus()
           log.update(f"File {fname} saved")
           
           savefile(fname,txt.text)
       
        if event.key == "ctrl+f":   
               log.update("Search in file: ")
               cmd.focus()

               if events.Key.key == "y":
                  txt.focus()
                  state = False

           


if __name__ == "__main__":
    app = Editor()
    app.run()

 from tkinter import *
  
 +#Add win condition
 +def Endcondition(winner) :
 +      msgwindow = Tk()
 +      msg = Message(msgwindow, text= winner + "is win!!!")
 +      msg.grid(row=0, column=0)
 +      for a in list:
 +            a["command"] = ""
 +			
  def checked(i) :
        global player
        button = list[i]
 -
 +  
        if button["text"] != "     " :
 -            return
 +      if (button["text"] != "     "):
 +              return
        button["text"] = player 
 +      button["text"] = " "+player+" " 
        button["bg"] = "yellow"
 -
 +  
        if player == "X" :
              player = "O"
              button["bg"] = "yellow"
 +      r = i//3
 +      c = i%3
 +      
 +      if (list[r*3]["text"] == list[r*3 + 1]["text"] == list[r*3 + 2]["text"]) or ( list[c]["text"] == list[c + 3]["text"] == list[c + 6]["text"] ) or ( list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ") or (list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ") :
 +            Endcondition(player)
        else :
              player = "X"
              button["bg"] = "lightgreen"
  
 +            if player == "X" :
 +                  player = "O"
 +                  button["bg"] = "yellow"
 +            else :
 +                  player = "X"
 +                  button["bg"] = "lightgreen"
 +      
  window = Tk()
  player = "X"
  list= []
 @@ -26,5 +48,3 @@ def checked(i) :
        list.append(a)
  
  window.mainloop()

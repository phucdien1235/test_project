from guizero import App, Text, Picture, Box

app = App(title = "Giới thiệu bản thân", width = 1000, height = 750)
header_box = Box(app, align = "top", width = 650, height = 700, border = False)
name = Text(header_box, text = "Tên: Điền", size = 15, color = "blue")
age = Text(header_box, text = "Tuổi: 12", size = 15, color = "purple")
school = Text(header_box, text = "Trường: Lý Thái Tổ \n"
                                 "  Hình ảnh:", size = 15, color = "green")
picture = Picture(header_box, image = "hộp quà.png")
greeting = Text(header_box, text = "Xin chào tôi là Điền. Đây là chương trình đầu tiên \n"
                                   "của tôi trên GUI, rất vui được gặp các bạn. Tạm biệt!!!"
                                   , size = 15, color = "red")

app.display()
from guizero import App, Text, Picture, Box

app = App(title = "Thành phố", width = 1500, height = 1000, bg = "lightyellow")
greeting = Text(app, text = "Hôm nay, tôi sẽ giới thiệu về thành phố Nha Trang!!!",
                size = 20, color = "purple")
greeting_2 = Text(app, text = "Đây là phong cảnh ở thành phố của tôi.",
                size = 20, color = "red")
box_1 = Box(app, width = 640, height = 428, align = "left", border = True)
box_2 = Box(app, width = 860, height = 428, align = "right", border = True)
landscape_1 = Picture(box_1, image = "tháp bà Ponaga.png")
landscape_2 = Picture(box_2, image = "Nha Trang.png")

app.display()

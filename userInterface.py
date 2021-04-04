from graphics import *


class JobInterface:
    """this class will create a calculator
    the user can only define the background color
    and buttons colors
    but not now"""

    def __init__(self,window, job):
        """initializing the calcualtor """
        #this is where we will be using the job methods
        self.job = job
        #window holder
        self.window = window    
        self.number1_str = ""
        self.number2_str = ""
        self.operation = ""
        self.num1 = True


    #the leading __ indicates that this method is internal to the class
    def __dispWin(self):
        """this function will initiate the display window"""
        
        #we create a rectangle by giving it a starting point and end point
        self.displayWin = Rectangle(Point(1,4),Point(4,4.5))
        #set the color of the object
        self.displayWin.setFill("white")
        #drawings the object on the graphics
        self.displayWin.draw(self.window)

        #we create a rectangle by giving it a starting point and end point
        #x1 = 0.5
        #increase = 0.75
        #self.displayWin = Rectangle(Point(x1,3),Point(x1+increase,3.5))
        #self.displayWin.setFill("white")
        #self.displayWin.draw(self.window)
        

    def __buttonPos(self):
        """this function will display the buttons on the calculator"""
        x1, x2, y1, y2 = 1, 1.5, 0.25, 0.75
        button_list = []
        button_counter = 1
        self.symb_x = []
        self.symb_y = []
        for i in range(0,17):
            button_list.append(Rectangle(Point(x1,y1), Point(x2,y2)))
            self.symb_x.append((x1 + x2)/2)
            self.symb_y.append((y1 + y2)/2)
            new_y1 = y2 + 0.25
            new_y2 = new_y1 + 0.5
            y1 = new_y1
            y2 = new_y2
            if button_counter % 4 == 0:
                new_x1 = x2 + 0.25
                new_x2 = new_x1 + 0.5
                x1 = new_x1
                x2 = new_x2
                y1 = 0.25
                y2 = 0.75
            button_counter += 1

        


        self.__buttonDisp(button_list)


    def __buttonDisp(self,buttonList):
        """this function will draw the buttons"""
        self.buttonList = buttonList
        for button in self.buttonList:
            button.setFill("white")
            button.draw(self.window)

    def __symbolDisp(self):
        """function to display the symbols"""
        buttons_symbol = ['.','7','4','1','0','8','5','2','=','9','6','3','+','-','x','/', 'Q']
        self.symbols_list = []
        for i in range(0,17):
            Text(Point(self.symb_x[i], self.symb_y[i]), buttons_symbol[i]).draw(self.window)
            self.symbols_list.append(buttons_symbol[i])


    def InterfaceStart(self):
        """this function will start the ability to push buttons"""
        self.operations_list = ['+','-','x','/']
        self.numbers_list = ['.','7','4','1','0','8','5','2','9','6','3']
        self.quit_calc = False
        while self.quit_calc == False:
            mouse_click = self.window.getMouse()
            self.mouseX = mouse_click.getX()
            self.mouseY = mouse_click.getY()
            self.__checkButtPos()

    def __checkButtPos(self):
        """this function will check the position of the pressed buttons"""
        for i in range(0,17):
            if ((self.mouseX >= (self.symb_x[i] - 0.25) and self.mouseX <= (self.symb_x[i] + 0.25)) and (self.mouseY >= (self.symb_y[i] - 0.25) and self.mouseY <= (self.symb_y[i] + 0.25))):
                for symbol in self.symbols_list:
                    if symbol == self.symbols_list[i]:
                        self.__checkSymbolEx(symbol)

    def __checkSymbolEx(self,symbol):
        """function to test what is the symbol"""                      
        if symbol in self.numbers_list and self.num1:
            if symbol == '1':
                self.job.dispaly_default_quote()
            if symbol == '2':
                self.job.display_default_estimate()
            self.number1_str += symbol
        elif symbol in self.operations_list:
            self.operation = symbol
            self.num1 = False
        elif symbol in self.numbers_list and not self.num1:
            self.number2_str += symbol
        else:
            self.__equQuit(symbol)

        

    def __equQuit(self,symbol):
        """function to equate or exit"""
        if symbol == "=":
            if self.operation == "+":
                evaluation = (float(self.number1_str) + float(self.number2_str))

            if self.operation == "-":
                evaluation = (float(self.number1_str) - float(self.number2_str))

            if self.operation == "/":
                evaluation = (float(self.number1_str) / float(self.number2_str))

            if self.operation == "x":
                evaluation = (float(self.number1_str) * float(self.number2_str))

            print("the math is " + str(self.number1_str) + self.operation + str(self.number2_str) + " = " + str(evaluation))
            self.number1_str = ""
            self.number2_str = ""
            self.num1 = True
        elif symbol == 'Q':
            self.quit_calc = True
            self.window.close()



    def InterfaceDisplay(self):
        """the function to display the claculator"""
        self.__dispWin()
        self.__buttonPos()
        self.__symbolDisp()


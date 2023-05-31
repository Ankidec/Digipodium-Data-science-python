from turtle import*
speed ('slowest')

for i in range(5):
    pencolor('red')
    pensize(5)
    fd(120)
    lt(360/5)
    for j in range (6):
       pencolor ('blue')
       pensize(1)
       fd (100)
       lt(360/6)
       write (f'{i},{j}')
mainloop    


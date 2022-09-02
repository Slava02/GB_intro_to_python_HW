print("введите координаты первой точки через запятую:")
#x_1, y_1 = map(float, input().split(', ')) 
x_1, y_1 = map(int, input().split(', '))  
print("введите координаты второй точки через запятую:")
#x_2, y_2 = map(float, input().split(', '))
x_2, y_2 = map(int, input().split(', '))
res = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5
print('Расстояние между точками: %.2f' %res)


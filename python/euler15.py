def solve_it(grid_dimensions):
  x_coord = []
  y_coord = []
  for i in range(0,grid_dimensions+1):
    x_coord.append(i)
    y_coord.append(i)
  return x_coord, y_coord
  
print solve_it(2)

    
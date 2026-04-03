agent = (2,2)
points = [(1,1),(5,5),(0,3)]
def manhattan_distance(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
bliz_point = min(points, key=lambda point: manhattan_distance(agent,point))
print(f'Ближайшая точка: {bliz_point}')

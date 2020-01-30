array_pawn_coordinates = input().split()

count = 0
set_pawns_coordinates = set()
for p in array_pawn_coordinates:
    if p[0] == 'a':
        set_pawns_coordinates.add((1, int(p[1])))
    elif p[0] == 'b':
        set_pawns_coordinates.add((2, int(p[1])))
    elif p[0] == 'c':
        set_pawns_coordinates.add((3, int(p[1])))
    elif p[0] == 'd':
        set_pawns_coordinates.add((4, int(p[1])))
    elif p[0] == 'e':
        set_pawns_coordinates.add((5, int(p[1])))
    elif p[0] == 'f':
        set_pawns_coordinates.add((6, int(p[1])))
    elif p[0] == 'g':
        set_pawns_coordinates.add((7, int(p[1])))
    elif p[0] == 'h':
        set_pawns_coordinates.add((8, int(p[1])))

for col, row in set_pawns_coordinates:
    if (col - 1, row - 1) in set_pawns_coordinates or (col + 1, row - 1) in set_pawns_coordinates:
        count += 1

print(count)

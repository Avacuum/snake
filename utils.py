import random


def generate_walls(width: int, height: int, amount: int = 10, tile_size: int = 20):
    walls = [
        (
            random.randint(1, width//20-1) * tile_size,
            random.randint(1, height//20-1) * tile_size
        ),
    ]

    while len(walls) < amount:
        new_wall = (
            random.randint(1, width//20-1) * tile_size,
            random.randint(1, height//20-1) * tile_size
        )

        if new_wall in walls:
            continue

        for wall in walls:
            if new_wall[0] == wall[0]-1 or new_wall[0] == wall[0]+1 or new_wall[1] == wall[1]-1 or new_wall[1] == wall[1]+1:
                pass
            else:
                walls.append(new_wall)

    return walls
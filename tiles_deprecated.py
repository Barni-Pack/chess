# from tiles_map import tiles_map
from classes import Tile


def create_and_draw_all_tiles(tiles_map_: dict) -> dict:
    # Creates instances of tiles and draws them
    tiles = dict()
    for name in tiles_map_.keys():
        tiles[name] = Tile(name)
        tiles[name].draw()
    return tiles
        # exec(f'{name} = Tile("{name}")')
        # exec(f'{name}.draw()')
        
    # a1 = Tile('a1')
    # a2 = Tile('a2')
    # a3 = Tile('a3')
    # a4 = Tile('a4')
    # a5 = Tile('a5')
    # a6 = Tile('a6')
    # a7 = Tile('a7')
    # a8 = Tile('a8')
    
    # b1 = Tile('b1')
    # b2 = Tile('b2')
    # b3 = Tile('b3')
    # b4 = Tile('b4')
    # b5 = Tile('b5')
    # b6 = Tile('b6')
    # b7 = Tile('b7')
    # b8 = Tile('b8')
    
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')
    # a1 = Tile('a1')


# create_and_draw_all_tiles(tiles_map)


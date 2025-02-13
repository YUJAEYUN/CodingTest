import sys
from collections import defaultdict

OFFSET = 100000
WHITE, BLACK = 1, 2

tiles = defaultdict(int)
white = black = 0

def main():
    global white, black
    input_count = int(sys.stdin.readline().strip())
    cur = OFFSET
    
    for _ in range(input_count):
        flip_count, direction = sys.stdin.readline().strip().split()
        flip_count = int(flip_count)
        
        if direction == "L":
            while flip_count > 0:
                tiles[cur] = WHITE
                flip_count -= 1
                if flip_count > 0:
                    cur -= 1
        else:
            while flip_count > 0:
                tiles[cur] = BLACK
                flip_count -= 1
                if flip_count > 0:
                    cur += 1
    
    white = sum(1 for v in tiles.values() if v == WHITE)
    black = sum(1 for v in tiles.values() if v == BLACK)
    print(white, black)

if __name__ == "__main__":
    main()

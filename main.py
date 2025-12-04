import sys
import math
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_normal_map.py <input.png> <output.png>")
        sys.exit(1)

    print(f"Loading {sys.argv[1]}...")
    img = Image.open(sys.argv[1]).convert("L")
    pixels = img.load()
    width, height = img.size

    out_img = Image.new("RGB", (width, height))
    out_pixels = out_img.load()
    
    strength = 6.0 

    print("Processing pixels...")
    
    for y in range(height):
        for x in range(width):
            left  = pixels[max(x - 1, 0), y]
            right = pixels[min(x + 1, width - 1), y]
            up    = pixels[x, max(y - 1, 0)]
            down  = pixels[x, min(y + 1, height - 1)]

            dx = (right - left) / 255.0 * strength
            dy = (down - up)  / 255.0 * strength
            dz = 1.0

            length = math.sqrt(dx*dx + dy*dy + dz*dz)
            
            r = int(((-dx / length) + 1.0) * 127.5)
            g = int(((-dy / length) + 1.0) * 127.5)
            b = int((( dz / length) + 1.0) * 127.5)

            out_pixels[x, y] = (r, g, b)

    out_img.save(sys.argv[2])
    print(f"Saved to {sys.argv[2]}")

if __name__ == "__main__":
    main()

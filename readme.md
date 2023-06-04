# Palette Grabber
## About
This Python script takes an input directory full of `.png` files and returns an 
image containing every color used in every image in the input directory. This 
works best for retrieving the color palette of games using pixel art as assets 
or textures.

**Requirements**

- Python3
- PIL

**Example**

Here is an example output using the textures directory from the game Minecraft

![An exmaple output image](example.png)

*Image scaled up to show detail, orginal image generated at 100x100 pixels*

**Current restrictions**

- The total number of colors in the final palette cannot exceed 10,000
- The returned image will always been 100x100 pixels regardless of input size

## Changelog
- 2023/06/01 - v1.0 - Initial release

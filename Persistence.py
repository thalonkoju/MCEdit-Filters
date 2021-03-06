# This filter makes any mob in the selection box persistent
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from math import sqrt
import random

displayName = "Make Mobs Persistent"

VERSION = "1.3.0"
UPDATE_URL = "http://podshot.github.io/update/Persistence.json"

inputs = (
        ("Makes any mobs in the Selection Box Persistent", "label"),
        ("Version: 1.3","label"),
)
# The user can't interact with that input, its great for giving extra info
def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value
            # Gets the position of the mob

            if (x,y,z) in box:
                if "Health" in e:
                        # Checks to see if the Entity has the Health tag
                        # Checking the entity for a health tag slows down the filter though
                                        if "PersistenceRequired" not in e:
                                            e["PersistenceRequired"] = TAG_Byte()

                                        e["PersistenceRequired"] = TAG_Byte(1)
                                        # Changes the byte to 1
                                        chunk.dirty = True
                                        # Marks chunk as changed and that the changes need to be saved

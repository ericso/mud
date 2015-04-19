# mud
A MUD (Multi-User Dungeon) Game built in Javascript backed by Django

This is personal project to build a text adventure game much like Zork.

Requirements for the game:
The game UI will be a text input field and a text output area.
The user will type commands, taking the form of
  <verb> <noun> <preposition> <noun>

Examples of commands:
 - go north
 - give cup to girl
 - open door
 - look east

The game world consists of a grid of nodes. The player can explore by typing movement commands. When the player arrives on a new node, description text will output on the console.

If there are items, containers, or dungeons at the node, the player can take additional actions such as picking up the item, opening the container, or enter the dungeon, respectively.

The player may come across puzzles or riddles. For example, a safe might ask a riddle which the player must answer before it will open. The player can type the answer to the riddle which should trigger the container to open.


player
  - name
  - position
  - inventory

world
  - the gameworld, a grid of nodes representing locations
  - the world can contain
    - dungeons
    - barriers
barriers
  - prevents the player from advancing in a given direction
  - river, wall, thick trees

dungeons
  - house, building, cave, ship, anything that is indoors
  - dungeons are accessed from the game world
  - they are entered and exited by passageways
    - door, window, grate, etc

containers
  - can hold items
  - can be locked, requiring a key to open

items
  - can be picked up by the user and placed into their inventory
  - keys: unlock doors, cabinets, chests

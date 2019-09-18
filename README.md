# MARS-LANDER-PROJECT
One of the first arcade games to be based on a real space mission and using pseudo-realistic physics was Lunar Lander (Atari, 1979). The aim of this project is to create a similar application about landing on Mars.

In the game, players control a space vehicle as it makes its
approach to the surface of the moon. By pressing various
keyboard keys, the vehicle can be rotated right or left, or
the main rocket engine fired (to decelerate the vehicle).
Fuel is limited, so the player has to carefully manage use
of the main engine. Points are scored by landing on various
landing zones, but the vehicle must have horizontal and
vertical velocity below certain acceptable limits or it is
destroyed. Similarly, attempting to land outside a landing
zone results in a crash. A successful landing triggers an award of points, and a new landing
mission (with landing zones in new, random locations).

## MY AIM:
Design and build
an updated version of the Lunar Lander game in pygame. A basic version (called “Mars Lander”) should
have the following characteristics:

• The player begins with 3 ‘lives’ – i.e. has 3 lander vehicles to use (one after another) before the
game ends.

• The lander starts at the top of the screen (assumed to be 1000m above the surface of the planet) with
vertical velocity (veloc_y) set to a random value between 0.0 and 1.0 m/s and horizontal velocity
(veloc_x) set to a random value between -1.0 and +1.0 m/s.

• The lander controls are as follows:
o rotate right [right-arrow key]: rotate the vehicle 1 degree clockwise;
o rotate left [left-arrow key]: rotate the vehicle 1 degree counter-clockwise;
o fire main engine [spacebar]: fire the rocket (burning fuel) to counteract gravity.

• Each lander starts with 500 kg of rocket fuel, and this is reduced every time the main engine thruster
is fired. 5 kg of thrust is used for each press of the spacebar.

• When the thrust key is pressed, a small image is positioned below the lander to illustrate the rocket
thrust is on.

• If the lander flies off the right of the screen it should wrap onto the left side (and vice-versa); the
lander should not be permitted to fly off the top of the screen.

• Three landing pads appear at different locations on the screen; pad locations are not restricted to the
bottom of the screen (0m altitude) and you could, for example, place a landing pad on top of a
mountain (with an altitude > 0 m). Landing outside of a landing pad location causes an immediate
crash (lander destroyed).

• A successful landing is defined as one in which the lander is horizontal, has both landing legs on the
landing pad (i.e. the lander sprite fully overlaps the pad) and is moving slowly enough. An
acceptable landing is defined as one where the lander touches down with horizontal velocity
(veloc_x) < 5.0 m/s and vertical velocity (veloc_y) < 5.0 m/s. A successful landing results in the
award of 50 points to the player’s score, and the game pauses until a key is pressed – after which a
new landing mission starts. Successful landings do not cost one of the player’s lives.

• Each lander starts with 0% damage but this immediately increases to 100% (a crash) if the vehicle
hits a landing pad too hard. A hard landing is defined as one where the lander touches down on the
landing pad with horizontal velocity (veloc_x) >= 5.0 m/s and vertical velocity (veloc_y) >= 5.0
m/s.

• Crashes cost a player a life and result in a “You Have Crashed!” message being displayed on the
game screen. The game pauses until a player presses a key, after which a new landing mission
begins.

• During a mission, various instruments display flight data to the player. These are: time (mins:secs)
since start of the mission; fuel (kg); damage (%age); altitude (m); x-velocity (m/s); y-velocity (m/s).
These are updated continuously in the top-left (instrument panel) region of the main game screen.

• The player’s score is recorded (and updated as points are scored) throughout the game; the score is
recorded in the region to the right of the “SCORE” label in the instrument panel.



## Physics


Although the original Lunar Lander game was often characterised as a ‘simulation’, in reality it was some
way from a true simulation of spaceflight. For the purposes of this assignment you should also not attempt to
create a fully realistic working simulation. Instead, it will be sufficient to create an approximate solution.

A few things to note:

• Each time the main rocket engine is activated (each press of spacebar) we need to increase the
lander’s velocity. To do this we need to know the angle of rotation of the lander, so that the x and y
components of the velocity vector can be calculated. The following equations will be of use:


***veloc_xi+1 = veloc_xi + 0.33 x sin(-angle)***


***veloc_yi+1 = veloc_yi - 0.33 x cos(angle)***


Note: The value of 0.33 shown above is a constant that seems to give a reasonable magnitude to
the thrust vector and makes for a playable game. You may want to experiment with this.


• Gravity needs to act on the lander vehicle – pulling it down towards the Martian surface. When the
lander is not at rest (landed or crashed) we need to increase the vertical (y) component of the velocity
by a small amount every game cycle. Acceleration due to gravity on Mars is 3.711 m/s2
, or 0.38g,
but increasing the y-velocity by this amount every game cycle will be too much; in the demo version
of the game, the course lecturer found that increasing veloc_y by 0.1 m/s was sufficient.


## IMAGE COLLECTION

***The image collection used for the creation of this application belongs to THE UNIVERSITY OF ABERDEEN***



# GenCyber-Badge Guide
Participant guide to the DSU GenCyber electronic badge

![PCB design of the badge](https://github.com/DSUmjham/GenCyber/blob/master/Badge/Images/pcb-design.png?raw=true)![PCB gerber image of the badge](https://github.com/DSUmjham/GenCyber/blob/master/Badge/Images/pcb-gerber.png?raw=true)

## The Badge
This is the first (that we know of) electronic badge designed for use in a GenCyber camp! The badge offers participants an opportunity to master soldering, and the six security concepts. This device is also capable of communicating with others like it over Infrared (IR), which is a great way to meet the other participants. A successfully-built badge allows participants to join our camp game in pursuit of the highest score. 

 - [Assembly Instructions](https://github.com/DSUmjham/GenCyber/blob/master/Badge/Articles/Assembly.md) - Step-by-step instructions on how to assemble your badge
 - [Datasheets](https://github.com/DSUmjham/GenCyber/tree/master/Badge/Datasheets) - All of the nerdy specs on the components we used
 - [Gerbers](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Gerbers/gencyber-badge-22_2-gerbers.zip) - Archive of the gerber files needed to order your own badges

### The Game
Your buy-in for the game is getting a badge built and registered with camp staff. Once that is done, the competition begins! The overall premise of the game is pretty simple: connect with as many *unique* badges as possible. Whoever collects the most wins the game.

**Gameplay**
 1. Find another camp-goer who is willing to connect badges.
 2. Place your badge into receive mode by pressing the button labeled **SW2**
 3. While your badge is listening in receive mode, have the other person transmit their badge info to you; they will need to press **SW1** on their badge to transmit the data.
 4. When receiving data, your badge will blink blue to show the bitstream coming in.
 5. If you scanned a new badge, your badge will display a green LED. If unsuccessful or if it was not a unique badge, your LED will light up red.
 6. Be courteous, flip the process and send them your info too. Teamwork makes the dream work.

**Winning**

Each camp will have a different number of participants and staff helping out. The first person to collect all of the badges wins the game. If nobody has gotten all of them by the end of camp, the person with the most gets the win. You can check your current status in a couple of different ways:

 1. Scan your badge at one of the scoring kiosks to see your overall score.
 2. Press both **SW1** and **SW2** simultaneously and your RGB LED will give you an on-board indicator.
   
   The points breakdown is as follows:
 
 | # of Badges  | % | Color |
 |---: |---:|---    |
 | 0   | 10 | Red   |
 | 10  | 20 | Yellow|
 | 15  | 30 | Green |
 | 20  | 40 | Cyan  |
 | 25  | 50 | Blue  |
 | 30  | 60 | Purple|
 | 35  | 70 | White |
 | 40+ | 80 | ???   |


If you played the game and met some friends along the way, you're a winner in our book :smile:!

## Resources
* [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) - library used with the ATTINy to enable IR TX/RX
* [OSH Park](https://oshpark.com) -  PCB manufacture located in the US
* [JLCPCB](https://jlcpcb.com) - PCB manufacture located overseas
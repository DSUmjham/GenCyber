

# Badge Assembly
The first objective you have is to assemble your badge. Make sure you've got a good grasp on the components you are working with and soldering safely before starting this!

The order of assembly is not critical, but this approach should work well:
 1. Verify you have all of the parts needed:
	 1. Badge PCB
	 2. Battery Holder
	 3. Battery
	 4. Resistor 56 Ohm % 1/4 Watt
	 5. IR Receiver
	 6. RGB LED 5MM
	 7. IR Transmitter 5MM
	 8. 2 Pushbuttons
	 9. DIP Socket
	 10. Microcontroller ATTINy (this may be handed out at the end)
![Badge components labeled](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly01.jpeg?raw=true)

2. The DIP Socket is the first component to solder onto the badge. This will eventually hold the ATTINy chip onto the badge. Pay special attention to the notch on the socket; it should line up with the notch on the silk screen next to **U1** of the badge.
![DIP socket placed onto badge with notch orientation](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly02.jpg?raw=true)
![Soldering the DIP socket](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly03.jpg?raw=true)
3. After soldering the DIP socket, move on to the two buttons labeled **SW1** and **SW2**. The pinouts of the buttons are rectangular and will only fit onto the badge one way. You should not need to bend any pins to get the buttons to fit.
![Button SW1 placed onto the badge](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly04.jpg?raw=true)
![Soldering the button SW1](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly05.jpg?raw=true)
4. Once both buttons are soldered on, the transmitting IR LED can be soldered on. This will go in the **D2** place on the badge. **Note:** The silkscreen on the badge shows a flat edge of the **D2** component on the right-hand side. The IR LED also has a flat edge; line this side up with the silk screen.
![IR Transmitting LED placed on the badge with flat edge properly aligned](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly06.jpg?raw=true)
Another way to verify the correct orientation is that the long lead of the LED is through the hole closest to the outside edge of the PCB and the short lead is through the hole closest to the DIP socket.
![Soldering the IR transmitting LED](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly07.jpg?raw=true)
5. Next, solder the resistor onto the badge in the **R1** location. The orientation of the resistor does not matter. It may be helpful to pre-bend the leads so that the component fits nicely. Avoid bending them at a sharp angle.
![Bending the resistor leads](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly08.jpg?raw=true)
6. The RGB LED can be soldered onto the badge next. This one is a little bit tricky because the solder pads are closer together than other components. It may be helpful to cut off each lead after it has been soldered to give you more room. The LED will not sit completely flush with the PCB because of the staggered leads. **Note:** Much like the IR transmitter LED, the RGB LED has a flat edge. This edge should be aligned with the flat edge on the silkscreen (right side). The image also shows the correct order of the pins; pin 1 is in the top-left corner.
![RGB LED placed on the badge](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly09.jpg?raw=true)
![RGB LED soldered onto the badge](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly10.jpg?raw=true)
7. Just a few components left! Solder the IR Receiver next in the **U2** spot.
![IR Receiver placed on the badge](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly11.jpg?raw=true)
![IR Receiver being soldered onto the badge](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly12.jpg?raw=true)
8. The battery holder is the last piece to solder. Since the battery is held on the back of the badge, your solder joints will be on the front side of the badge - this is the opposite of the other components that you've soldered so far.
![Battery holder in position](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly13.jpg?raw=true)
9. Trim off any remaining leads from the components.
![Trimming component leads](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly14.jpg?raw=true)
10. If you don't already have your ATTINy, find a camp staff member. They will flash the firmware onto a chip for you and record your unique ID.
11. Place the ATTINy in the DIP socket making sure to line up the indented dot on the chip with the notch of the socket.
![ATTINy aligned with the notch on DIP socket](https://github.com/DSUmjham/GenCyber/raw/master/Badge/Images/assembly15.jpeg?raw=true)
13. Install the battery into the holder minding the + and - sides.
14.  Test it out and if all is well, you're officially in the game!
/* keyPadHiduino Example Code
   by: Jim Lindblom
   date: January 5, 2012
   license: MIT license. If you find this code useful, please
   feel free to use this code however you'd like, commercially 
   or otherwise. Just keep this license on there whatever you do.

   This code implements a 12-key USB keypad. You can type 0-9,
   * is the + sign and the # key is enter. I'm using SparkFun's
   12-button keypad, your pinouts may vary. Multi-touch is
   not supported.

   SparkFun Keypad P
   Rows and columns are connected as such:
   -------------
   | 1 | 2 | 3 | - 3
   | 4 | 5 | 6 | - 7
   | 7 | 8 | 9 | - 6
   | * | 0 | # | - 1
   -------------
     |   |   |
     2   4   5
*/
// Pins 1-7 of the keypad connected to the Arduino respectively:
int keypadPins[7] = {6, 7, 8, 9, 5, 4, 3};
int keypadStatus;  // Used to monitor which buttons are pressed.
int timeout;  // timeout variable used in loop

void setup()
{
  for (int i=0; i<7; i++)
  {
    pinMode(keypadPins[i], INPUT);  // Set all keypad pins as inputs
    digitalWrite(keypadPins[i], HIGH);  // pull all keypad pins high
  }
}

void loop()
{
  keypadStatus = getKeypadStatus();  // read which buttons are pressed
  if (keypadStatus != 0)  // If a button is pressed go into here
  {
    sendKeyPress(keypadStatus);  // send the button over USB
    timeout = 2000;  // top of the repeat delay
    while ((getKeypadStatus() == keypadStatus) && (--timeout))  // Decrement timeout and check if key is being held down
      delayMicroseconds(1);
    while (getKeypadStatus() == keypadStatus)  // while the same button is held down
    {
      sendKeyPress(keypadStatus);  // continue to send the button over USB
      delay(50);  // 50ms repeat rate
    }
  }
}

/* sendKeyPress(int key): This function sends a single key over USB
   It requires an int, of which the 12 LSbs are used. Each bit in
   key represents a single button on the keypad.
   This function will only send a key press if a single button
   is being pressed */
void sendKeyPress(int key)
{
  switch(key)
  {
    case 1:  // 0x001
      Keyboard.write('1');  // Sends a keyboard '1'
      break;
    case 2:  // 0x002
      Keyboard.write('2');
      break;
    case 4:  // 0x004
      Keyboard.write('3');
      break;
    case 8:  // 0x008
      Keyboard.write('4');
      break;
    case 16:  // 0x010
      Keyboard.write('5');
      break;
    case 32:  // 0x020
      Keyboard.write('6');
      break;
    case 64:  // 0x040
      Keyboard.write('7');
      break;
    case 128:  // 0x080
      Keyboard.write('8');
      break;
    case 256:  // 0x100
      Keyboard.write('9');
      break;
    case 512:  // 0x200
      Keyboard.write('.');
      break;
    case 1024:  // 0x400
      Keyboard.write('0');  // Sends a keyboard '0'
      break;
    case 2048:  // 0x800
      Keyboard.write('\b');  // Sends the 'ENTER' key
      break;
  }
}

/* getKeypadStatus(): This function returns an int that represents
the status of the 12-button keypad. Only the 12 LSb's of the return
value hold any significange. Each bit represents the status of a single
key on the button pad. '1' is bit 0, '2' is bit 1, '3' is bit 2, ..., 
'#' is bit 11.

This function doesn't work for multitouch.
*/
int getKeypadStatus()
{
  int rowPins[4] = {keypadPins[2], keypadPins[6], keypadPins[5], keypadPins[0]};  // row pins are 2, 7, 6, and 1 of the keypad
  int columnPins[3] = {keypadPins[1], keypadPins[3], keypadPins[4]};  // column pins are pins 2, 4, and 5 of the keypad
  int keypadStatus = 0;  // this will be what's returned
  
  /* initialize all pins, inputs w/ pull-ups */
  for (int i=0; i<7; i++)
  {
    pinMode(keypadPins[i], INPUT);
    digitalWrite(keypadPins[i], HIGH);
  }
  
  for (int row=0; row<4; row++)
  {  // initial for loop to check all 4 rows
    pinMode(rowPins[row], OUTPUT);  // set the row pin as an output
    digitalWrite(rowPins[row], LOW);  // pull the row pins low
    for (int col=0; col<3; col++)
    {  // embedded for loop to check all 3 columns of each row
      if (!digitalRead(columnPins[col]))
      {
        keypadStatus |= 1 << ((row+1)*3 + (col+1) - 4);  // set the status bit of the keypad return value
      }
    }
    pinMode(rowPins[row], INPUT);  // reset the row pin as an input
    digitalWrite(rowPins[row], HIGH);  // pull the row pin high
  }
  
  return keypadStatus;
}


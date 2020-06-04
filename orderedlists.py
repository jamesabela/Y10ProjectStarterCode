""" A set of lists that you can shuffle and choose randomly
ARQ 
QRCode 
barcode 
Microphone 
ABS 
fetch_execute 
digital_camera 
scanner_2d scanner_3d
AccessSecureWebsite
inkjet_printer
laser_printer

There are many games you could play with such lists from 
multiple choice, odd one out etc.

"""
import random

ARQ = ['Uses acknowledgement and time out','Check performed on received data','If error detected, request sent to resend data','If no acknowledgement is sent that data is received','Data is resent till data is resent correctly']
        
QRCode =['Read or scanned using app (on mobile device)',
        'It is the camera that is used to scan or capture the image',
        'The three large squares are used to define the alignment',
        'Black squares reflect less light',
        'The app/device processes the image', 
        'Each small square/pixel is converted to a binary value']
        
barcode=['The barcode is first read by a red laser', 
        'Light is reflected back off the barcode', 
        'The reflected light is read by sensors (photoelectric cells)', 
        'As the laser or LED light is scanned across the barcode, a pattern Is generated', 
        ' This is converted into digital data']
        
Microphone=['Someone says a word into the microphone', 
        'The sound card in the computer will convert the sound wave into a digital form', 
        'The digital image is then broken up into phonemes', 
        "The phonemes are compared with words in the computer's built in dictionary", 
        'The word said will then be suggested by the computer']
        
ABS = [ 'use magnetic field sensors to stop the wheels locking up on the car.', 
        'When one of the car wheels rotates too slowly', 
        'a magnetic field sensor sends data to a microprocessor.', 
        'The microprocessor check the rotation speed of the three wheels.', 
        'If they are different, it sends a signal to the braking system', 
        'If one of the wheels is rotating too quickly', 
        'braking pressure is increased to that wheel.', 
        ' Until it matches the other three.']
        
fetch_execute = ['PC contains the address of the memory location of the next instruction which has to be fetched', 
        'This address is then copied from the PC to the MAR', 
        'The contents at the memory location contained in MAR are then copied into the MDR', 
        'The contents of the MDR are then copied CIR', 
        'The value in the PC is then incremented by 1', 
        'The instruction is finally decoded and then executed.']
        
digital_camera = ['Image is converted from analogue to digital (using ADC)', 
        'Image is turned into pixels', 
        'Each pixel is given a binary value', 
        'Pixels form a grid', 
        'Each pixel has a colour', 
        'Pixels are stored in sequence.'] 
scanner_2d = ['shines a light onto the surface of a document', 
        'Reflected light is captured', 
        'Uses mirrors and lenses', 
        'Captured image is converted into a digital file']
        
scanner_3d = ['shines a laser (or light) over the surface of a 3D object', 
        'Records measurements of the geometry/dimensions of the object', 
        'Measurements are converted to digital file'] 

AccessSecureWebsite =['the web browser attempts to connect to a web site which is secured by SSL', 
        'the web browser requests the web server to identify itself', 
        'the web server sends the web browser a copy of its SSL certificate', 
        'the web browser checks whether the SSL certificate is trustworthy', 
        'if it is then the web browser sends a message back to the web server', 
        'the web server will then send back some form of acknowledgement', 
        'the encrypted data is then shared securely between the web browser and the web server'], 
        
inkjet_printer =['The data from the document is sent to a printer driver',
        'The printer driver ensures that the data is in a format that the chosen printer can understand',
        'A check is made by the printer driver to ensure that the chosen printer is available to print.',
        'The data is then sent to the printer',
        'and it is stored in temporary memory known as a print buffer.',
        'A sheet of paper is then fed into the main body of the the printer.',
        'As the sheet of paper is fed through the printer,',
        'the print head moves from side to side across the paper printing the text or image.',
        'Ink droplets are pushed onto the paper with either a Thermal bubble or a piezoelectric crystal.',
        'The four ink colours are sprayed in their exact amounts to produce the desired final colour.',
        'At the end of each pass, the paper is advanced slightly.',
        'Once the printer buffer is empty, then the printer sends an interrupt.',
        'The whole process continues until the whole of the document is printed.']
        
laser_printer = ['The printer driver ensures that the data is in a format that the laser printer can understand', 
        'Data is then sent to the laser printer and stored temporarily in the printer buffer', 
        'The printing drum is given a positive charge', 
        'As the printing drum rotates, a laser scans across it', 
        'this removes the positive charge in certain areas', 
        'Negatively-charged areas are then produced on the printing drum', 
        'these match exactly with the text and images to be printed', 
        'The printing drum is coated in positively-charged toner', 
        'this then sticks to the negatively-charged parts of the printing drum', 
        'A negatively-charged sheet of paper is then rolled over the printing drum', 
        'The toner on the printing drum is now transferred to the paper to reproduce the required text and images', 
        'The paper goes through a fuser which melts the toner so it fixes permanently to the paper']

# Sample random chooser
rand_choose = random.randint(0,4)
if rand_choose == 0: print(ARQ)
elif rand_choose == 1: print(ARQ)
elif rand_choose == 2: print(QRCode)
elif rand_choose == 3: print(barcode)
elif rand_choose == 4: print(Microphone)

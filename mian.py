from config import wifi_ssid, wifi_password
from updates import tens, ones, tenscent, pennys
from epd2in13b_V4 import EPD_2in13_B_V4_Landscape
from font8 import font8
from font12 import font12
from font24 import font24
import urequests
import network
import time

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#--------------------------wifi connection function---------
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        time.sleep(1)
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True
#===========================================================
#---------------------------------------------------------------Starting the wifi and getting time------------
init_wifi(wifi_ssid, wifi_password) 
current_time = time.time()
print('Epoch Time:', current_time)
time_tuple = time.localtime(current_time)
print('Time tuple:', current_time)

#===========================================================
#---- 12 POINT FONT -------------------------------------------------------------------
def printltrfontx(px, py, ltr, fontx, color):
    oldpx = px
    for x in fontx:
        if x==ltr:
            for i in fontx[x]:
                letter = '{:08b}' .format(i)
                bstring = letter
                px = oldpx
                for z in bstring:
                    if z=='1':
                        if color == 'red':
                            epd.imagered.pixel(px,py,0x00)
                        else:
                            epd.imageblack.pixel(px,py,0x00)
                    px = px + 1
                py = py + 1

def printStringFontx(ltrx, ltry, str, fontx, color):
    oldy = ltry
    for i in range(len(str)):
        printltrfontx(ltrx, ltry, str[i], fontx, color)
        ltry = oldy
        ltrx = ltrx + 8
#============================================================================================
#---- 24 POINT FONT -------------------------------------------------------------------
def printltrfont24(px, py, ltr, color):
    oldpx = px
    for x in font24:
        if x==ltr:
            i = 0
            while i < len(font24[x]):
                ltr1 = str('{:08b}' .format(font24[x][i]))
                bstring1 = ltr1
                ltr2 = str('{:08b}' .format(font24[x][i+1]))
                bstring2 = ltr2
                ltr3 = str('{:08b}' .format(font24[x][i+2]))
                bstring3 = ltr3
                bstring = bstring1+bstring2+bstring3
                i = i + 3
                px = oldpx
                for z in bstring:
                    if z=='1':
                        if color == 'red':
                            epd.imagered.pixel(px,py,0x00)
                        else:
                            epd.imageblack.pixel(px,py,0x00)
                    px = px + 1
                py = py + 1

def printStringFont24(ltrx, ltry, str, color):
    oldy = ltry
    for i in range(len(str)):
        printltrfont24(ltrx, ltry, str[i], color)
        ltry = oldy
        ltrx = ltrx + 12
#============================================================================================
#-------------Draw 212x104 .pbm --------------------------------------------
def pbm_draw(px,py,file):
    oldpx = px
    flist = ""
    with open(file, 'rb') as f:
        f.readline()
        f.readline()
        f.readline()
        flist = f.readlines()
    f.close()

    i = 0
    newfile = ''
    while i < len(flist):
        str = flist[i].decode("utf-8").rstrip()
        newfile = newfile + str
        i = i + 1

    col = 0
    row = 0
    x = 0
    y = 0
    bstr = ''
    while row < 22048:
        col = 0
        px = oldpx
        while col < 212:
            if newfile[x] == '1':
                epd.imageblack.pixel(px,py,0x00)
            px = px + 1
            col = col + 1
            x = x + 1
        py = py + 1
        row = row + 212
        y = y + 1
#=============================================================
#-------------Draw 52x70 .pbm --------------------------------------------
def pbm_drawFont(px,py,file):
    oldpx = px
    flist = ""
    with open(file, 'rb') as f:
        f.readline()
        f.readline()
        f.readline()
        flist = f.readlines()
    f.close()

    i = 0
    newfile = ''
    while i < len(flist):
        str = flist[i].decode("utf-8").rstrip()
        newfile = newfile + str
        i = i + 1

    col = 0
    row = 0
    x = 0
    y = 0
    bstr = ''
    while row < 3640:
        col = 0
        px = oldpx
        while col < 52:
            if newfile[x] == '1':
                epd.imageblack.pixel(px,py,0x00)
            px = px + 1
            col = col + 1
            x = x + 1
        py = py + 1
        row = row + 52
        y = y + 1
#=============================================================
#---------------------------check for updates --------------------
def check_for_updates(OTA):
    try:
        response = urequests.get(upd_url).text
        print('response = = = = = = = ')
        print(response)
        x = len(response)
        print(x)
        if response == 'FAIL':
            print('There are no updates available.')
            return(OTA)
        else:
            OTA = 1
            print('There is an update available')
            return(OTA)

    except:
        print('unable to reach internet')
        return(OTA)
#=================================================================
#--------------------------------------------------------------------------------Makes e-paper work!!! ------------
#--------------------------------epd setup ----------------------
epd = EPD_2in13_B_V4_Landscape()
epd.Clear(0xff, 0xff)
epd.imageblack.fill(0xff)
epd.imagered.fill(0xff)
#=============================================================
#=================== price lable ================
printltrfont24(10, 20, '$', 'black')
pbm_drawFont(20,20, str(tens) + '.pbm')
pbm_drawFont(70,20, str(ones) + '.pbm')
printltrfont24(120, 30, str(tenscent), 'black')
printltrfont24(135, 30, str(pennys), 'black')
#=================================================

#--------------------Test Stuff ---------------------
#printStringFont24(10, 5, 'Snoopy', 'red')
#pbm_draw(20,20,'snoopy.pbm')
epd.imagered.vline(160, 0, 120, 0x00)
#epd.imageblack.hline(0, 122, 249, 0x00)
#epd.imagered.text("Hello World", 0, 40, 0x00)
#printStringFontx(15, 80, 'Augie Doggy', font8, 'red')
#printStringFontx(10, 60, 'Yang Yang', font12, 'black')
printStringFontx(20, 100, 'minutes:', font12, 'red')
printStringFontx(100, 100, str(time_tuple[4]), font12, 'red')
#printltrfont24(80, 20, 'B', 'black')
#printltrfontx(150, 20, 'R', font8, 'black')
#======================================================
# -------------------------epd.display()----------------------------------
epd.display()
print("edp sleeps")
epd.sleep()
print('but python is not asleep....')
#=========================================================
#========================================================================================== Makes e-paper work ----------
#------------------------------------check for updates ---------

check_url="http://192.168.0.12/checkup.php"

while True:
    response = urequests.get(check_url).text

    if 'Y' in response:
        print("Time to update!")
        upd_url = "http://192.168.0.12/readdata.php"
        numstr = urequests.get(upd_url).text
        print(numstr)
        clear_url = "http://192.168.0.12/clearflag.php"
        noresponse = urequests.get(clear_url)

        if len(numstr.strip()) == 5:
            print("tens = " + numstr[0])
            print("ones = " + numstr[1])
            print("tenscent = " + numstr[3])
            print("pennys = " + numstr[4])
            f = open("updates.py","w")
            f.write("tens = " + numstr[0] + "\n" + "ones = " + numstr[1]  + "\n" + "tenscent = " + numstr[3] + "\n" + "pennys = " + numstr[4])
            f.flush()
            f.close
            print('reboot now')
            machine.reset()
    else:
        print("No update today.")
        print("pico going to sleep now")
        time.sleep(300)
        time_tuple = time.localtime(current_time)
        print('Minute:', time_tuple[4])

#======================================================================================


#while True: # ------------------- A loop to continually print time ------------
#    current_time = time.time()
#    print('Epoch Time:', current_time)
    
#    time_tuple = time.localtime(current_time)
#    print('Time tuple:', current_time)
    
#    print('Current date and time:')
#    print('Year:', time_tuple[0])
#    print('Month:', time_tuple[1])
#    print('Day:', time_tuple[2])
#    print('Hour:', time_tuple[3])
#    print('Minute:', time_tuple[4])
#    print('Second:', time_tuple[5])
#    print('Day of the Week:', days_of_week[time_tuple[6]])
    
#    time.sleep(1)



import cv2
import numpy as np
import tkinter

gui = tkinter.Tk()
gui.title('Sárdi András Mihály: Digitális képfeldolgozás beadandó')


def bezaras():
    gui.destroy()


def inditas():
    # Beolvasom a képet, majd pedig megjelenítem.
    img = cv2.imread("crosswalk.jpg")
    cv2.imshow('Kezdo kep:', img)
    # Átkonvertálom grayscale formátumúra a képet, majd pedig megjelenítem
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale kep:', grayscale)
    # Gaussian blur alkalmazása után megjelenítem a képet
    blurred = cv2.GaussianBlur(grayscale, (15, 15), 6)
    cv2.imshow('Blurred kep: ', blurred)
    # Tresholdingolok, minden pixel érték ami 130 felett van 255 értékre vált, azaz fehérre. A többi feketére vált.
    ret, thresh1 = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)
    # A funkció contourokkal tér vissza.
    contourok, hier = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # A megfelelő pixelterületű contourokkal haladok tovább.
    for contour in contourok:
        if cv2.contourArea(contour) < 1000:
            continue

        minarea = cv2.minAreaRect(contour)
        intcontour = cv2.boxPoints(minarea)
        # Intté konvertálom a pontokat.
        intcontour = np.int64(intcontour)
        # Megrajzolom a kontourokat, a -1
        cv2.drawContours(img, [intcontour], -1, (0, 0, 255), thickness=-1)
        cv2.imshow('Vegeredmeny:', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


button1 = tkinter.Button(gui, text='Program indítása', width=100, command=inditas)
button2 = tkinter.Button(gui, text='Program leállítása', width=100, command=bezaras)
button1.pack()
button2.pack()

gui.mainloop()

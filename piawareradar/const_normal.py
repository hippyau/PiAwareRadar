FLIGHTDATAREFRESH = 1000
FLIGHTDATATIMEOUT = 30


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BUTTONCOLOR = (128,128,128)


FONT = "monospace"
FONTSIZE = 16
LINESPACE = 20
SIZE = (600, 600)


BUTTONSIZEX = 20
BUTTONSIZEY = BUTTONSIZEX

RADARPADDING = 10 # from edges
SCALEPADDING = 10 # from edge
BUTTONPADDING = 10 # space between buttons

RADARRECT = (RADARPADDING, RADARPADDING, SIZE[0]-RADARPADDING*2, SIZE[1]-RADARPADDING*2)
CLOSERECT = (SIZE[0]-SCALEPADDING-RADARPADDING-(BUTTONSIZEX-BUTTONPADDING), BUTTONPADDING, BUTTONSIZEX, BUTTONSIZEY)

SCALEPLUSRECT = (SIZE[0]-SCALEPADDING-RADARPADDING-BUTTONPADDING, SIZE[1]-BUTTONSIZEY*3, BUTTONSIZEX, BUTTONSIZEY)
SCALENEGRECT = (SIZE[0]-SCALEPADDING-RADARPADDING-(BUTTONPADDING*2)-BUTTONSIZEX, SIZE[1]-BUTTONSIZEY*3, BUTTONSIZEX, BUTTONSIZEY)

SCALELINERECT = (SIZE[0]-SCALEPADDING-RADARPADDING-40, SIZE[1]-BUTTONSIZEY*2 + SCALEPADDING, 50, 10)
SCALETEXTRECT = (SIZE[0]-SCALEPADDING-RADARPADDING-40, SIZE[1]-BUTTONSIZEY*1, 70, 20)

TITLEPOS = (10, 10)

FLIGHTDATAPOS = (650, 430)
FLIGHTDATARECT = (FLIGHTDATAPOS[0], FLIGHTDATAPOS[1], 150, 200)



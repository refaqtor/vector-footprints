#!/usr/bin/env python
#-*- coding: utf-8 -*-

from svgwrite import Drawing

def TSSOP(name,offset,width,height,padh,padw,spaceing,padcount,bodyw,bodyh,pinw,pinh,thermalw=0,thermalh=0):
    
    # document sizes
    doc = (width + 2 * offset[0], height + 2 * offset[1])

    # basic SVG sheet
    svg = Drawing(filename=name, size=doc) 

    #######################################################################################################
    # PCB Pads
    #######################################################################################################

    pads = svg.g(id="pads")

    for n in range(0,padcount):
        x = offset[0] + (n * spaceing)
        y = offset[1]
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)

    for n in range(0,padcount):
        x = offset[0] + (n * spaceing)
        y = offset[1] + height - padh
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
 
    if thermalw is not 0 and thermalh is not 0:
        # thermal pad
        t = svg.rect(insert=((doc[0] / 2) - (thermalw / 2), (doc[1] / 2) - (thermalh / 2)), size=(thermalw,thermalh), stroke_width=0.05, stroke="black", fill="#D4AA00")
        pads.add(t) 

    svg.add(pads)
    
    #######################################################################################################
    # Part
    #######################################################################################################

    cornerx = (doc[0] / 2) - (bodyw / 2 )
    cornery = (doc[1] / 2) - (bodyh / 2 )
    
    part = svg.g(id="part")
    
    for n in range(0,padcount):
        x = offset[0] + (n * spaceing) + ((padw - pinw) / 2)
        y = offset[1] + (padh - pinh)
        pin = svg.rect(insert=(x,y),size=(pinw,pinh),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pin)

    for n in range(0,padcount):
        x = offset[0] + (n * spaceing) + ((padw - pinw) / 2)
        y = offset[1] + (height - padh)
        pin = svg.rect(insert=(x,y),size=(pinw,pinh),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pin)

    body = svg.rect(insert=(cornerx, cornery), size=(bodyw,bodyh), stroke_width=0.05, stroke="black", fill="#333333")
    part.add(body)

    # pin 1 indicator
    ind = svg.circle(center=(cornerx+0.5 ,cornery+bodyh-0.5), r=0.2,stroke_width=0.05, stroke="black", fill="#333333") 
    part.add(ind)

    svg.add(part)

    svg.save()

# TSSOP8
TSSOP(
    name = "tssop-8.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 2.37,     # row width
    padh = 1.78,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 4,    # pins per side
    bodyw = 3,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.3,      # pin width
    pinh = 1.0       # pin height  
    )

# TSSOP14
TSSOP(
    name = "tssop-14.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 4.35,     # row width
    padh = 1.65,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 7,    # pins per side
    bodyw = 4.9,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.25,      # pin width
    pinh = 1.0       # pin height  
    )

# TSSOP16
TSSOP(
    name = "tssop-16.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 5,     # row width
    padh = 1.65,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 8,    # pins per side
    bodyw = 5.0,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.25,      # pin width
    pinh = 1.0,       # pin height  
    thermalw = 2.74,  # thermal pad size
    thermalh = 2.74   # thermal pad size
    )

# TSSOP20
TSSOP(
    name = "tssop-20.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 6.3,     # row width
    padh = 1.65,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 10,    # pins per side
    bodyw = 6.4,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.25,      # pin width
    pinh = 1.0,       # pin height  
    thermalw = 2.74,  # thermal pad size
    thermalh = 2.74   # thermal pad size
    )

# TSSOP24
TSSOP(
    name = "tssop-24.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 7.6,     # row width
    padh = 1.65,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 12,    # pins per side
    bodyw = 7.8,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.25,      # pin width
    pinh = 1.0,       # pin height  
    thermalw = 4.32,  # thermal pad size
    thermalh = 3.0   # thermal pad size
    )

# TSSOP28
TSSOP(
    name = "tssop-28.svg", # filename for svg
    offset = (10,10), # global offset
    height = 7.75,    # row height
    width  = 8.9,     # row width
    padh = 1.65,      # pad height
    padw = 0.42,      # pad width
    spaceing = 0.65,  # pin spacing
    padcount = 14,    # pins per side
    bodyw = 9.6,      # body width
    bodyh = 4.4,      # body height
    pinw = 0.25,      # pin width
    pinh = 1.0,       # pin height  
    thermalw = 4.75,  # thermal pad size
    thermalh = 2.74   # thermal pad size
    )


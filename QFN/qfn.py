#!/usr/bin/env python
#-*- coding: utf-8 -*-

from svgwrite import Drawing

def QFN(name,offset,width1,width2,padh,padw,spaceing,padcount,bodyw, thermal):
    
    # document sizes
    doc = (width1 + 2 * offset[0], width1 + 2 * offset[1])

    # basic SVG sheet
    svg = Drawing(filename=name, size=doc) 

    #######################################################################################################
    # PCB Pads
    #######################################################################################################

    pads = svg.g(id="pads")

    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + (n * spaceing)
        y = offset[1]
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)

    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + (n * spaceing)
        y = offset[1] + (width1 - padh)
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
    
    for n in range(0,padcount):
        x = offset[0]
        y = offset[1] + ((width1 - width2) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(padh,padw),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
    
    for n in range(0,padcount):
        x = offset[0] + (width1 - padh)
        y = offset[1] + ((width1 - width2) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(padh,padw),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
 
    # thermal pad
    t = svg.rect(insert=((doc[0] / 2) - (thermal / 2), (doc[1] / 2) - (thermal / 2)), size=(thermal,thermal), stroke_width=0.05, stroke="black", fill="#D4AA00")
    pads.add(t) 

    svg.add(pads)

    #######################################################################################################
    # Part
    #######################################################################################################

    corner = (doc[0] / 2) - (bodyw / 2 )
    
    part = svg.g(id="part")

    body = svg.rect(insert=(corner, corner), size=(bodyw,bodyw), stroke_width=0.05, stroke="black", fill="#333333")
    part.add(body)

    # pin 1 indicator
    ind = svg.circle(center=(corner+0.5 ,corner+bodyw-0.5), r=0.2,stroke_width=0.05, stroke="black", fill="#333333") 
    part.add(ind)

    svg.add(part)

    svg.save()

# QFN16
QFN(
    name = "qfn-16.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 3.5,   # outer distance
    width2 = 1.75,   # row width
    padh = 0.7,   # pad height
    padw = 0.25,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 4,     # pins per side
    bodyw = 3.0,   # outer body size
    thermal= 1.65 # thermal pad size
    )

# QFN20
QFN(
    name = "qfn-20.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 4.5,   # outer distance
    width2 = 2.25,   # row width
    padh = 0.7,   # pad height
    padw = 0.25,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 5,     # pins per side
    bodyw = 4.0,   # outer body size
    thermal= 2.45 # thermal pad size
    )

# QFN24
QFN(
    name = "qfn-24.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 4.5,   # outer distance
    width2 = 2.75,   # row width
    padh = 0.7,   # pad height
    padw = 0.25,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 6,     # pins per side
    bodyw = 4.0,   # outer body size
    thermal= 2.45 # thermal pad size
    )

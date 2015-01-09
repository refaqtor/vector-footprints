#!/usr/bin/env python
#-*- coding: utf-8 -*-

from svgwrite import Drawing

def LQFP(name,offset,width1,width2,padh,padw,spaceing,padcount,bodyw,edge,pinh,pinw):
    
    # document sizes
    doc = (width1 + 2 * offset[0], width1 + 2 * offset[1])

    # basic SVG sheet
    svg = Drawing(filename=name, size=doc) 

    #######################################################################################################
    # PCB Pads
    #######################################################################################################

    pads = svg.g(id="pads")

    # pins 51 to 75 
    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + (n * spaceing)
        y = offset[1]
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)

    # pins 1 to 25
    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + (n * spaceing)
        y = offset[1] + (width1 - padh)
        pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
    
    # pins 76 to 100
    for n in range(0,padcount):
        x = offset[0]
        y = offset[1] + ((width1 - width2) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(padh,padw),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
    
    # pins 26 to 50
    for n in range(0,padcount):
        x = offset[0] + (width1 - padh)
        y = offset[1] + ((width1 - width2) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(padh,padw),stroke_width=0.05,stroke="black",fill="#D4AA00")        
        pads.add(pad)
  
    svg.add(pads)

    #######################################################################################################
    # Part
    #######################################################################################################

    corner = (doc[0] / 2) - (bodyw / 2 )
    
    part = svg.g(id="part")
    
    # pins 51 to 75 
    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + ((padw - pinw) / 2) + (n * spaceing)
        y = corner - pinh
        pad = svg.rect(insert=(x,y),size=(pinw,pinh),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pad)
    
    # pins 1 to 25
    for n in range(0,padcount):
        x = offset[0] + ((width1 - width2) / 2) + ((padw - pinw) / 2) + (n * spaceing)
        y = corner + bodyw
        pad = svg.rect(insert=(x,y),size=(pinw,pinh),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pad)
    
    # pins 76 to 100
    for n in range(0,padcount):
        x = corner - pinh
        y = offset[0] + ((width1 - width2) / 2) + ((padw - pinw) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(pinh,pinw),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pad)
    
    # pins 26 to 50
    for n in range(0,padcount):
        x = corner + bodyw
        y = offset[0] + ((width1 - width2) / 2) + ((padw - pinw) / 2) + (n * spaceing)
        pad = svg.rect(insert=(x,y),size=(pinh,pinw),stroke_width=0.05,stroke="black",fill="#999999")        
        part.add(pad)

    # plastic body 
    points = [(corner, corner+edge), (corner+edge, corner),
              (corner+bodyw-edge, corner), (corner+bodyw, corner+edge),
              (corner+bodyw, corner+bodyw-edge), (corner+bodyw-edge, corner+bodyw),
              (corner+edge, corner+bodyw), (corner, corner+bodyw-edge)]

    body = svg.polygon(points=points, stroke_width=0.05, stroke="black", fill="#333333")
    part.add(body)

    # pin 1 indicator
    ind = svg.circle(center=(corner+1 ,corner+bodyw-1), r=0.5,stroke_width=0.05, stroke="black", fill="#333333") 
    part.add(ind)

    svg.add(part)

    svg.save()


# parameters for package found here: http://www.st.com/web/en/resource/technical/document/datasheet/DM00037051.pdf

# LQFP64
LQFP(
    name = "lqfp-64.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 12.7,   # outer distance
    width2 = 7.8,   # row width
    padh = 1.2,   # pad height
    padw = 0.3,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 16,     # pins per side
    bodyw = 10.0,   # outer body size
    edge = 0.75,   # edge size
    pinh = 1.0,    # pin height
    pinw = 0.22   # pin width
    )

# LQFP100
LQFP(
    name = "lqfp-100.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 16.7,   # outer distance
    width2 = 12.3,   # row width
    padh = 1.2,   # pad height
    padw = 0.3,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 25,     # pins per side
    bodyw = 14.0,   # outer body size
    edge = 0.75,   # edge size
    pinh = 1.0,    # pin height
    pinw = 0.22   # pin width
    )

# LQFP144
LQFP(
    name = "lqfp-144.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 22.6,   # outer distance
    width2 = 17.85,   # row width
    padh = 1.35,   # pad height
    padw = 0.35,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 36,     # pins per side
    bodyw = 20.0,   # outer body size
    edge = 0.75,   # edge size
    pinh = 1.0,    # pin height
    pinw = 0.22   # pin width
    )

# LQFP176
LQFP(
    name = "lqfp-176.svg", # filename for svg
    offset = (10,10), # global offset
    width1 = 26.7,   # outer distance
    width2 = 21.8,   # row width
    padh = 1.2,   # pad height
    padw = 0.3,   # pad width
    spaceing = 0.5,    # pin spacing
    padcount = 44,     # pins per side
    bodyw = 24.0,   # outer body size
    edge = 0.75,   # edge size
    pinh = 1.0,    # pin height
    pinw = 0.22   # pin width
    )

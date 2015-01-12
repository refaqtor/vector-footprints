#!/usr/bin/env python
#-*- coding: utf-8 -*-

from svgwrite import Drawing

def RC(name,offset,width,height,padh,padw,bodyw,bodyh):
    
    # document sizes
    doc = (width + 2 * offset[0], height + 2 * offset[1])

    # basic SVG sheet
    svg = Drawing(filename=name, size=doc) 

    #######################################################################################################
    # PCB Pads
    #######################################################################################################

    pads = svg.g(id="pads")
    x = offset[0]
    y = offset[1]
    pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
    pads.add(pad)
    
    x = offset[0] + (width - padw)
    y = offset[1]
    pad = svg.rect(insert=(x,y),size=(padw,padh),stroke_width=0.05,stroke="black",fill="#D4AA00")        
    pads.add(pad)

    svg.add(pads)
    
    #######################################################################################################
    # Part
    #######################################################################################################

    x = offset[0] + ((width - bodyw) / 2)
    y = offset[1]

    # I just estimate 25% of the body width to be the solder connection. Found no data about this size
    pinw = bodyw * 0.25
    bodyw = bodyw / 2

    part = svg.g(id="part")
    
    pin = svg.rect(insert=(x,y),size=(pinw,bodyh),stroke_width=0.05,stroke="black",fill="#999999")        
    part.add(pin)
    
    body = svg.rect(insert=(x+pinw,y),size=(bodyw,bodyh),stroke_width=0.05,stroke="black",fill="#282828")        
    part.add(body)
    
    pin = svg.rect(insert=(x+pinw+bodyw,y),size=(pinw,bodyh),stroke_width=0.05,stroke="black",fill="#999999")        
    part.add(pin)
    
    svg.add(part)
    
    svg.save()

# 0603
RC(
    name = "0603.svg", # filename for svg
    offset = (10,10), # global offset
    height = 0.8,    # row height
    width  = 2.7,     # row width
    padh = 0.8,      # pad height
    padw = 0.9,      # pad width
    bodyw = 1.5,      # body width
    bodyh = 0.8,      # body height
    )

# 0805
RC(
    name = "0805.svg", # filename for svg
    offset = (10,10), # global offset
    height = 1.3,    # row height
    width  = 3.4,     # row width
    padh = 1.3,      # pad height
    padw = 1.05,      # pad width
    bodyw = 2.0,      # body width
    bodyh = 1.3,      # body height
    )

# 1206
RC(
    name = "1206.svg", # filename for svg
    offset = (10,10), # global offset
    height = 1.5,    # row height
    width  = 4.8,     # row width
    padh = 1.5,      # pad height
    padw = 1.25,      # pad width
    bodyw = 3.0,      # body width
    bodyh = 1.5,      # body height
    )

# 2010
RC(
    name = "2010.svg", # filename for svg
    offset = (10,10), # global offset
    height = 2.5,    # row height
    width  = 6.3,     # row width
    padh = 2.5,      # pad height
    padw = 1.4,      # pad width
    bodyw = 5.2,      # body width
    bodyh = 2.5,      # body height
    )

# 2512
RC(
    name = "2512.svg", # filename for svg
    offset = (10,10), # global offset
    height = 3.2,    # row height
    width  = 8.5,     # row width
    padh = 3.2,      # pad height
    padw = 2.0,      # pad width
    bodyw = 6.5,      # body width
    bodyh = 3.2,      # body height
    )

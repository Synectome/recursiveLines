import random

class CustomLine():
    def __init__(self, current, iterations):
        self.current = current
        self.iterations = iterations
        self.recursive = 0
        
    def pattern_a(self):
        for i in range(self.iterations):
            x, y = self.current
            self.current[0] += sin(i)*16
            self.current[1] += cos(i)*16
            line(x,y, self.current[0], self.current[1])
            if (round(x) > width) | (round(y) > height)| (round(x) < 0) | (round(y) < 0):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1
                self.pattern_a()
                
    def pattern_b(self):
        global count
        for i in range(self.iterations):
            x, y = self.current
            self.current[0] += sin(i)*16
            self.current[1] += cos(i)*16
            line(x,y, self.current[0], self.current[1])
            x, y = self.current
            self.current[0] += sin(x)*8
            self.current[1] += cos(y)*8
            stroke(color(((self.current[1]+count)/height)*255,(count % 255),(y/x)*10))
            line(x,y,self.current[0], self.current[1])
            if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                self.recursive += 1
                #print("im so triggered b {}".format(self.recursive))
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1
                # MAXIMUM RECURSION at 2514
                #self.pattern_b()
                
    def pattern_bb(self):
        global count
        for i in range(self.iterations):
            x, y = self.current
            self.current[0] += sin(i)*16
            self.current[1] += cos(i)*16
            line(x,y, self.current[0], self.current[1])
            x, y = self.current
            self.current[0] += sin(x)*8
            self.current[1] += cos(y)*8
            stroke(color(((self.current[1]+count)/height)*255,(count % 255), 10))
            line(x,y,self.current[0], self.current[1])
            if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1 
                self.pattern_c()
                
    def pattern_bc(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            for j in range(1,i):
                x, y = self.current
                if ( i % 3 == 0):
                    self.current[0] -= sin(j)*8
                    self.current[1] += cos(j)*8
                elif (i % 2 == 0):
                    self.current[0] += sin(j)*8
                    self.current[1] -= cos(j)*8
                stroke(color(j%255, i%255, (j*i)%255))
                line(x,y, self.current[0], self.current[1])
                if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                    self.current[0] = width/2
                    self.current[1] = height/2
                    self.iterations += 1 
            
    def pattern_bcb(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            for j in range(1,i):
                x, y = self.current
                if ( j % 13 == 0):
                    self.current[0] -= sin(self.iterations)*8
                    self.current[1] += cos(j)*8
                    stroke(color(j%255, i%255, (j*i)%255))
                    line(x,y, self.current[0], self.current[1])
                else:
                    self.current[0] += sin(j)*8
                    self.current[1] += cos(j)*8
                    stroke(color(j%255, i%255, (j*i)%255))
                    line(x,y, self.current[0], self.current[1])                    
                if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                    self.current[0] = width/2
                    self.current[1] = height/2
                    self.iterations += 1
                     
    def pattern_bcc(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            x, y = self.current
            self.current[0] += sin(self.iterations)
            self.current[1] += cos(self.current[0]*self.current[0])/sin(self.current[0])
            stroke(color(255, i%255, (i*i)%255))
            line(x,y, self.current[0], self.current[1]) 
                
            if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1 
                
    def pattern_bccb(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            x, y = self.current
            self.current[0] += sin(self.iterations)*2
            self.current[1] += cos(self.current[0]*self.current[0])*4
            stroke(color(100, width/i, ((self.current[1]+count)/height)*255 ))
            line(x,y, self.current[0], self.current[1]) 
                
            if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1 
                
    def pattern_bccc(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            x, y = self.current
            self.current[0] += sin(self.iterations*self.current[1])*2
            self.current[1] += cos(self.current[0]*self.current[0])*2
            stroke(color(60, 170, 200))
            line(x,y, self.current[0], self.current[1]) 
            self.recenter(x,y)

                
    def pattern_bccd(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            #right
            x, y = self.current
            self.current[0] += cos(i)*i
            stroke(color(70, 150, 200))
            line(x,y, self.current[0], self.current[1]) 
            #up
            x, y = self.current
            self.current[1] -= sin(i)
            stroke(color(250, 130, 200))
            line(x,y, self.current[0], self.current[1]) 
            #left
            x, y = self.current
            self.current[0] -= tan(i)
            stroke(color(50, 110, 200))
            line(x,y, self.current[0], self.current[1]) 
            #down
            x, y = self.current
            self.current[1] += cos(i)*i
            stroke(color(40, 90, 0))
            line(x,y, self.current[0], self.current[1]) 
            self.iterations += 1
            self.recenter(x, y)
            
    def pattern_bccdb(self):
        global count, CENTER
        x, y = self.current
        for i in range(1, self.iterations):
            #right
            x, y = self.current
            self.current[0] += cos(i)*i
            stroke(color(70, x, 200))
            line(x,y, self.current[0], self.current[1]) 
            #up
            x, y = self.current
            self.current[1] -= sin(i)
            stroke(color(250, 130, 200))
            line(x,y, self.current[0], self.current[1]) 
            #left
            x, y = self.current
            self.current[0] -= tan(i)%height
            stroke(color(50, 110, 200))
            line(x,y, self.current[0], self.current[1]) 
            #down
            x, y = self.current
            self.current[1] += cos(i)*i
            stroke(color(y, 90, 0))
            line(x,y, self.current[0], self.current[1]) 
            self.iterations += 1
            self.recenter(x, y)
                                
    def pattern_c(self):
        for i in range(self.iterations):
            x, y = self.current
            self.current[0] += sin(i)*16
            self.current[1] += cos(i)*16
            line(x,y, self.current[0], self.current[1])
            x, y = self.current
            self.current[0] += sin(x)*8
            self.current[1] += cos(y)*8
            stroke(color((self.current[0]/width)*255, sqrt(x*y),(self.current[1]+count)/height)*255)
            line(x,y,self.current[0], self.current[1])
            if (round(x) > width) | (round(y) > height) | (round(x) < 0) | (round(y) < 0):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1
                # self.pattern_c()
    
    def pattern_d(self):
        for y in range(height):
            stroke(color(125, 255/(y+1), y%255))
            line(0, y, CENTER[0], CENTER[1])
            line(width, y, CENTER[0], CENTER[1])
            self.pattern_c()
        for x in range(width):
            stroke(color(250, x%255, 255/(x+1)))
            line(x, 0, CENTER[0], CENTER[1])
            line(x, height, CENTER[0], CENTER[1])
            self.pattern_bb()
        print("end of pattern_d")
        save("pattern_d_1.tif")
        exit()
    
    def pattern_e(self, spirals):
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(count%255, count, count))
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(spirals):
            curveVertex(sin(i)*count, cos(i)*count)
        endShape()
        
    def pattern_eb(self, spirals):
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(count%255, count, count))
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(spirals):
            curveVertex(i*sin(i)*count, i*cos(i)*count)
        endShape()
        
    def pattern_ec(self, spirals):
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(count%255, count, count))
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(spirals):
            if count != 0:
                curveVertex(sin(i%count)*i, cos(i%count)*i)
            else:
                curveVertex(sin(i)*i, cos(i)*i)
        endShape()
        
    def pattern_ecb(self, spirals):
        # like looking up the nose of God
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(0, 0, 0))
        smooth()
        translate(CENTER[0], 100)
        rotate(PI/4)
        beginShape()
        for i in range(1, spirals):
            curveVertex(sin(i)*count%i, cos(i)*count%i)
        endShape()
        
    def pattern_ecc(self, spirals):
        # like looking up the nose of God
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(0, 0, 0))
        smooth()
        translate(CENTER[0], 100)
        rotate(PI/4)
        beginShape()
        for i in range(1, spirals):
            curveVertex(sin(i)*count%i, cos(i)*count%i)
            if i % 7 == 0:
                curveVertex(cos(i*7)*i, sin(i*7)*i)
            if i % 5 == 0:
                curveVertex(cos(i*5)*count, sin(i*5)*count)
            if i % 11 == 0:
                curveVertex(sin(i*i)*count, cos(i*i)*count)
        endShape()

    def pattern_ecd(self, spirals):
        # like looking up the nose of God
        global count
        self.current[0] = CENTER[0]
        self.current[1] = CENTER[1]
        stroke(color(0, 0, 0))
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate(PI/count)
        beginShape()
        for i in range(1, spirals):
            if i % 2 == 0:
                curveVertex(cos(i*2)*(i/count), sin(i*2)*(i/count))
            if i % 3 == 0:
                curveVertex(cos(i*3)*count, sin(i*3)*count)
            if i % 5 == 0:
                rotate(PI/12)
                curveVertex(cos(i*5)*i, sin(i*5)*i)    
            # if i % 7 == 0:
            #     curveVertex(cos(i*7)*i, sin(i*7)*i)
            # if i % 11 == 0:
            #     curveVertex(sin(i*11)*i, cos(i*11)*i)
            # if i % 13 == 0:
            #     curveVertex(cos(i*13)*i, cos(i*13)*i)
        endShape()            

    def pattern_ece(self, spirals):
        # like looking up the nose of God
        global count
        stroke(color(0, 0, 0))
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate(PI/count)
        beginShape()
        for i in range(1, spirals):
            curveVertex(cos(i*2)*(i/count), sin(i*2)*(i/count))
            if i % 5 == 0:
                rotate(PI/12)
                curveVertex(cos(i*5)*i, sin(i*5)*i)    
        endShape()
        
    def pattern_f(self, spirals):
        # like looking up the nose of God
        global count, countcount
        smooth()
        translate(180+count, (height-50)-count)
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i, (count/(countcount+1))%255))
            curveVertex(cos(i)*i, sin(i)*50)
        endShape()
        
    def pattern_fb(self, spirals):
        # like looking up the nose of God
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i%count, count%255))
            curveVertex(sin(i)*i, sin(i)*i)
            curveVertex(cos(i)*i, cos(i)*i)
        endShape()
        
    def pattern_fc(self, spirals):
        # like looking up the nose of God
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i%count, count%255))
            curveVertex(sin(i)*i, sin(i)*i)
            curveVertex(sin(i)*i, cos(i)*i)
            curveVertex(cos(i)*i, cos(i)*i)
            curveVertex(cos(i)*i, sin(i)*i)
        endShape()
        
    def pattern_fd(self, spirals):
        # like looking up the nose of God
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i%count, count%255))
            curveVertex(sin(i)*count/i, sin(i)*i)
            curveVertex(sin(i)*i, cos(i)*i)
            curveVertex(cos(i)*i, cos(i)*count/i)
            curveVertex(cos(i)*i, sin(i)*i)
        endShape()
    
    def pattern_fe(self, spirals):
        # ANGELS WINGS
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i%count, count%255))
            curveVertex(sin(i)*count/i, sin(i)*i)
            curveVertex(sin(i)*i/count, cos(i)*i)
            curveVertex(cos(i)*i, cos(i)*count/i)
            curveVertex(cos(i)*i, sin(i)*i/count)
        endShape()
        
    def pattern_ff(self, spirals):
        # Jelly FISH
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI*count/360))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(i%255, 255-i%count, count%255))
            curveVertex(sin(i)*sin(i)*i, sin(i)*i)
            curveVertex(sin(i)*i, cos(i)*i)
            curveVertex(cos(i)*i, cos(i)*cos(i)*i)
            curveVertex(cos(i)*i, sin(i)*i)
        endShape()
        
    def pattern_ffb(self, spirals):
        # Jelly FISH-evolution
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI/4))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(70, 70+(count%255), 255))
            curveVertex(sin(i)*sin(i)*i, sin(i)*i+(cos(i)))
            curveVertex(sin(i)*i+sin(count), cos(i)*i)
            curveVertex(cos(i)*i, cos(i)*cos(i)*i+(sin(i)))
            curveVertex(cos(i)*i+cos(count), sin(i)*i)
        endShape()
        
    def pattern_ffc(self, spirals):
        # A ROAD
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI/4))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(70, 0, 108))
            curveVertex(sin(i)*sin(i)*(PI/count)*400, cos(i)*cos(i)*(PI/count)*400)
        endShape()

    def pattern_ffd(self, spirals):
        # A ROAD
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI/4))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(108, 0, 108))
            curveVertex(count/sin(i), count/cos(i))
        endShape()
        
    def pattern_ffe(self, spirals):
        # The pyramids
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI/4))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(10, 10, 10))
            curveVertex(cos(count)/sin(i), sin(count)/cos(i))
            curveVertex(sin(count)/cos(i), cos(count)/sin(i))
        endShape()
        
    def pattern_fff(self, spirals):
        # Rocket ship design
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        rotate((PI/4))
        beginShape()
        for i in range(1, (spirals)):
            stroke(color(10, 10, 10))
            curveVertex(cos(count)*i/count, sin(i)*count)
            curveVertex(sin(count)*i/count, i)
        endShape()

    def pattern_ffg(self, spirals):
        # galaxy two wings
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex((cos(count)*i)/count, sin(i)*count)
            curveVertex(sin(count)*i/count, cos(i)*count)
        print("EHNDED")
        endShape()
        
    def pattern_ffh(self, spirals):
        # Thumb print motif
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            #rotate((PI/180))
            stroke(color(10, 10, 10))
            curveVertex(sin(i%7)*i, cos(i%7)*i)
            # curveVertex(200, 200)
        print("EHNDED")
        endShape()

    def pattern_ffhb(self, spirals):
        # Hip t shirt chaos
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex((sin(i)*i)%count + cos(count)*i, (cos(i)*i)%count - sin(count)*i)
        print("EHNDED")
        endShape()
        
    def pattern_ffhc(self, spirals):
        # Bouncing spirals, bounded by a diamond
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex(sin(count)*sin(i)*i, cos(count)*cos(i)*i)
        print("EHNDED")
        endShape()
        
    def pattern_ffhc(self, spirals):
        # bouncing growing circles
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex(sin(count)*sin(i)*count, cos(count)*cos(i)*count)
        print("EHNDED")
        endShape()

    def pattern_g(self, spirals):
        # A star abyss
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex(count/(sin(count)*i), (sin(i)/sin(count))*i)
            curveVertex(count/(cos(count)*i), (cos(i)/cos(count))*i)
        print("EHNDED")
        endShape()
        
    def pattern_gb(self, spirals):
        # A Random sliver unfolding
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex(count/(sin(i)*i), (cos(i)/sin(i))*i)
            curveVertex(count/(cos(i)*i), (sin(i)/cos(i))*i)
        print("EHNDED")
        endShape()
        
    def pattern_gc(self, spirals):
        # Matricese Unravel
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, (spirals)):
            # rotate((PI/count))
            stroke(color(10, 10, 10))
            curveVertex(count/(sin(i)*i), (cos(i)/sin(i))*i)
            curveVertex((sin(i)/cos(i))*i, count/(cos(i)*i))
        print("EHNDED")
        endShape()
        
    def pattern_h(self, spirals):
        # spirograph remenicent
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, height/2, 10):
            # rotate((PI/count))
            
            for j in range(1, (width/2), 10):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(j)*j)
        print("EHNDED")
        endShape()
        
    def pattern_hb(self, spirals):
        # spirograph remenicent - Orbital
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, height/2, 10):
            # rotate((PI/count))
            curveVertex(cos(i)*i, sin(i)*i)
            for j in range(1, (width/2), 10):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(j)*j)
        print("EHNDED")
        endShape()
        
    def pattern_hc(self, spirals):
        # spirograph decendant - warp field
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, height/2, 10):
            # rotate((PI/count))
            curveVertex(cos(i)*i%count, sin(i)*i)
            for j in range(1, (width/2), 10):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j%count, cos(j)*j)
        print("EHNDED")
        endShape()
        
    def pattern_hd(self, spirals):
        # warp flower blooming - DIRTY
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, height/2, 10):
            # rotate((PI/count))
            curveVertex(cos(i)*i, sin(i)*i)
            for j in range(1, (width/2), 10):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(j)*j)
                curveVertex(cos(j)*count, sin(j)*count)
        print("EHNDED")
        endShape()
        
    def pattern_he(self, spirals):
        # warp flower blooming - CLEAN pillow
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, height/2, 10):
            # rotate((PI/count))
            # curveVertex(cos(i)*i, sin(i)*i)
            for j in range(1, (width/2), 10):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(j)*j)
                curveVertex(cos(j)*count, sin(j)*count)
        print("EHNDED")
        endShape()
        
    def pattern_hf(self, spirals):
        # Cleanest flower yet - morphs into a taurus
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, spirals, 10):
            for j in range(1, i):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(j)*j)
                curveVertex(cos(j)*count, sin(j)*count)
        print("EHNDED")
        endShape()

    def pattern_hg(self, spirals):
        # another center morpher
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        beginShape()
        for i in range(1, spirals, 10):
            for j in range(1, i, 3):
                stroke(color(j%200, (j/i)%255, count%255))
                curveVertex(sin(j)*j, cos(i)*j)
                curveVertex(cos(j)*count, sin(j)*count)
        print("EHNDED")
        endShape()
        
    def pattern_hh(self, spirals):
        # another center morpher
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        for j in range(4):
            beginShape()
            for i in range(spirals):
                curveVertex(sin(sin(i)/cos(count))*i, cos(cos(i)/sin(count))*i)
            endShape()
            # rotate(PI/2)
            
    def pattern_hi(self, spirals):
        # another center morpher
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        for j in range(4):
            beginShape()
            for i in range(spirals):
                curveVertex(sin(cos(i))*i, cos(sin(i))*i)
            endShape()
            rotate(PI/2)
            
    def pattern_hj(self, spirals):
        # Sunflower pointalism
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        for j in range(4):
            beginShape()
            for i in range(spirals):
                curveVertex(sin(count)*(count%324), cos(count)*(count%324))
            endShape()
            rotate(PI/2)
                
    def pattern_hk(self, spirals):
        # BORG
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        factor = random.randint(1, 40)
        stroke(color(factor, factor, factor))
        for j in range(4):
            beginShape()
            for i in range(spirals):
                curveVertex(sin(count)*(count%324), cos(i%count)*(count%324))
            endShape()
            rotate(PI/2)
            
    def pattern_hl(self, spirals):
        # sunflower 2
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        factor = random.randint(1, 40)
        
        for j in range(4):
            beginShape()
            for i in range(spirals):
                # stroke(color(factor, factor, factor))
                # curveVertex(sin(count)*(count%324), cos(count)*(count%324))
                stroke(color(225-factor, 225-factor, 225-factor))
                curveVertex(cos(count)*(count%324), sin(count)*(count%324))
            endShape()
            beginShape()
            for i in range(spirals):
                stroke(color(factor, factor, factor))
                curveVertex(sin(count)*(count%324), cos(count)*(count%324))
                # stroke(color(225-factor, 225-factor, 225-factor))
                # curveVertex(cos(count)*(count%324), sin(count)*(count%324))
            endShape()
            rotate(PI/2)

    def pattern_hm(self, spirals):
        # cleaner sunflower
        global count, countcount
        smooth()
        translate(CENTER[0], CENTER[1])
        factor = random.randint(1, 40)
        beginShape()
        for i in range(spirals):
            a = random.randint(1-factor,50)
            b = random.randint(1-factor,50)
            c = random.randint(1-factor,50)
            stroke(color(factor+a, factor+b, factor+c))
            curveVertex(sin(count)*(count%324), cos(count)*(count%324))
            # stroke(color(225-factor, 225-factor, 225-factor))
            # curveVertex(cos(count)*(count%324), sin(count)*(count%324))
        endShape()
        rotate(PI/2)

    def recenter(self, x, y):
        if (round(x) > (width+10)) | (round(y) > (height+10)) | (round(x) < (-10)) | (round(y) < (-10)):
            self.current[0] = width/2
            self.current[1] = height/2
            self.iterations += 1
             
    def mirror(self):
        x = self.current[0]
        y = self.current[1]
        self.current[1] = x
        self.current[0] = y

def setup():
    size(1400, 960)
    background(240)
    global CENTER, linelist, baking, myline
    baking = 0
    CENTER = [width/2, height/2]
    # make a list of my line objects
    # linelist = [CustomLine(CENTER, i) for i in range(20)]
    # print(linelist)
    myline = CustomLine(CENTER, 13)
    
count = 2
increase = True
reps = 0
countcount = 0
spinum = 400

def record(name):
    saveFrame(name)
    # reps += 1
    # if reps == 1080:
    #     exit()
        
def draw():
    strokeWeight(2)
    color(20, 20, 100)
    global baking, myline, count, increase, reps, countcount, spinum
    # if count >= 720:
    #     increase = False
    #     spinum += 10
    # if count <= 1:
    #     increase = True
    #     spinum += 5
    #     countcount += 5
    # if increase:
    #     count += 1
    # else:
    #     count -= 1
    count += 1
    print(count)
    myline.pattern_hm(spinum)

    # myline.pattern_bb()
    # if (count % 2 == 0):
    #     record("Double_Sunflower_#######.png")
    # if count == 108000:
    #     # save("pattern_eb_1000000.tif")
    #     exit()
    #     return
    

# EDIT THE FILE WITH YOUR SOLUTION
import re
import numpy 

#f = "/Users/wangzixing/Desktop/chrislordau-tangram-doctest-98a9e7f42ce9/files/chris/is_solution/A-not-solution-outside-2.xml" 
#ff =  "/Users/wangzixing/Desktop/chrislordau-tangram-doctest-98a9e7f42ce9/files/chris/is_solution/A-shape.xml"        
def available_coloured_pieces(file) :
    #\filename = input(file)
    #with open(file) as file:
    text = file.read()
    lines = re.findall('<path d=(.*)/>', text)
    coloured_pieces = {}
    for a in lines :
        color = re.findall('fill="(.*)"', a)[0]
        vertices = re.findall('[ML] *(\d+) (\d+) ', a)
        ver = []
        vv = []
        for a in vertices :
            alist = list(a)
            #print(alist)
            for i in alist :
                vv.append(int(i))
            ver.append(vv)
            vv = []
        coloured_pieces[color]=ver
    return coloured_pieces
          
def are_valid(coloured_pieces) :
    for color, verrr in coloured_pieces.items() :
        if not is_valid(verrr) :
            return False
    return True
       
def is_valid(verrr) :
    n = len(verrr)
    if n < 3:
        return False
    verrr = verrr + verrr[:2]
    orientation = same_orientation(verrr[0],verrr[1],verrr[2])
    for i in range(len(verrr)-3) :
        if same_orientation(verrr[i],verrr[i+1],verrr[i+2]) != orientation  :
            #print(1)
            return False
        #return True
    for i in range(len(verrr)-3) :
        for j in range(i+2, len(verrr)-2):
            if cross(verrr[i],verrr[i+1],verrr[j],verrr[j+1]) == True :
                #print(0)
                return False
            #return True      
    return True

def same_orientation(a,b,c) : #判断是不是统一方向
    aa = numpy.array([[1,a[0],a[1]],[1,b[0],b[1]],[1,c[0],c[1]]])
    d = numpy.linalg.det(aa)
    if d > 0 :
        return "left"
    if d < 0 :
        return "right"
    if d == 0 :
        return "no turn"
    
def cross(a,b,c,d) :#判断是否相交
    if a == d or b == c :
        return False
    if same_orientation(a,b,c) != same_orientation(a,b,d) and same_orientation(c,d,a) != same_orientation(c,d,b) :
         #print(a,b,c,d)
         #print(7)
         return True
    else :
         return False
     
def are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2) :
    for colorr, vverr in  coloured_pieces_1.items():
        if colorr not in coloured_pieces_2:
            return False
        if not if_the_same(vverr,coloured_pieces_2[colorr]) :
            return False
    for colorr, vverr in  coloured_pieces_2.items():
        if colorr not in coloured_pieces_1:
            return False
    '''
    color = []
    for a, b in coloured_pieces_2.items() :
        color.append(b)
    for colorr, vverr in  coloured_pieces_1.items():
        if not if_the_same(vverr,color):
            return False
    '''
    return True
    
        
def if_the_same(ver1,ver2):
    #print(ver1)
    #print(ver2)
    ver1 = move_to_top(ver1)
    ver2 = move_to_top(ver2)
    #print('1',ver1)
    #print('2',set(duijiao(ver1)))
    #print(set(ver2))
    #print(set(duijiao(ver2)))
    if set(ver2) == set(ver1):
        return True
    if set(ver2) == set(updown(ver1)) :
        return True
    if set(ver2) == set(leftright(ver1)) :
        return True
    if set(ver2) == set(duijiao(ver1)) :
        #print(111)
        return True
    if set(ver2) == set(updown(leftright(ver1))) :
        return True
    if set(ver2) == set(duijiao(leftright(ver1))) :
        return True
    if set(ver2) == set(updown(duijiao(ver1))) :
        return True
    if set(ver2) == set(duijiao(leftright(updown(ver1)))) :
        return True
    if set(ver2) == set(duijiao(duijiao(ver1))) :
        return True
    return False
def minx(ver):
    #xx = ver[0][0]
    minnnx = []
    for x in ver :
        minnx = []
        minnx.append(x[0])
        minnnx.append(minnx)
    return min(minnnx)

def miny(ver):
    minnnx = []
    for x in ver :
        minnx = []
        minnx.append(x[1])
        minnnx.append(minnx)
    return min(minnnx)
def maxx(ver) :
    minnnx = []
    for x in ver :
        minnx = []
        minnx.append(x[0])
        minnnx.append(minnx)
    return max(minnnx)
def maxy(ver) :
    minnnx = []
    for x in ver :
        minnx = []
        minnx.append(x[1])
        minnnx.append(minnx)
    return max(minnnx)
    
def move_to_top (ver) :
    new_ver =[]
    for a in ver :
        #print('0',a[1])
        #print('1',minx(ver)[0])
        new_ver.append((a[0]-minx(ver)[0], a[1]-miny(ver)[0]))
    return new_ver

def updown(ver) :
    new_ver = []
    for a in ver :
        new_ver.append((a[0], maxy(ver)[0]-a[1]))
    return new_ver
def leftright(ver) :
    new_ver=[]
    for a in ver :
        new_ver.append((maxx(ver)[0]-a[0], a[1]))
    return new_ver
def duijiao(ver):
    new_ver=[]
    for a in ver :
        new_ver.append((a[1], a[0]))
    return new_ver





def mianji(shape) :
    mianji = 0
    #dian = list(shape.value())
    if len(shape) < 3 :
        return False
    for i in range(len(shape)-1) :
        p1 = shape[i]
        p2 = shape[i+1]
        meigemianji = (p1[0]-shape[0][0])*(p2[1]-shape[0][1])-(p2[0]-shape[0][0])*(p1[1]-shape[0][1])
        mianji += meigemianji/2
    return abs(mianji)
        

    
def is_solution(tangram, shape)  :
    #area1 = mianji(shape)
    tangram_area = 0
    shape_area = 0
    vver = {}
    for color,ver in tangram.items() :
        tangram_area +=mianji(ver)
        vver[str(ver)]= 1
    if len(vver) != len(tangram) :
        return False
    #print(tangram_area)
    for color,ver in shape.items() :
        shape_shape = ver
        shape_area += mianji(ver)
    if tangram_area != shape_area :
        #print(0)
        return False
    for color,ver in tangram.items() :
        for point in ver :
            if outside(point,shape_shape) :
                #print('cuo=1')
                return False
    ndict=zhongdian(tangram)
    for color,ver in ndict.items() :
        for point in ver :
            if outside(point,shape_shape) :
                #print('cuo=1')
                return False
    shape_shape=0
    #tang
    for i in range(1,len(tangram)) :
        if  not issssss_solution(dict(list(tangram.items())[i:]),dict(list(tangram.items())[:i])) :
            #print(1)
            return False
    for i in range(1,len(ndict)) :
        if  not issssss_solution(dict(list(ndict.items())[i:]),dict(list(ndict.items())[:i])) :
            #print(1)
            return False 
    return True

    return True
    
def outside(point,ver) :
    ver1 = ver + ver[:1]
    for i in range(len(ver1)-1) :
        if point_in_line(point,ver1[i], ver1[i+1]) :
            return False
    cross_n = cross_number(point, ver)
    if cross_n % 2 == 1 :
        return False
    if cross_n % 2 == 0 :
        #print(point)
        #print(ver)
        
        return True
    
            
    
    
def point_in_line(a,b,c)  :
    if same_orientation(a,b,c) == "no turn" :
        if min(b[0],c[0]) <= a[0]<= max(b[0],c[0]) and min(b[1],c[1]) <= a[1]<= max(b[1],c[1]) :
            return True 
    #return False


def cross_number(point, ver) :
    point_end = (19,1e20)
    ver1 =  ver + ver[:1]
    #print('jinlaile')
    cross_n = 0
    for i in range(len(ver1)-1) :
        if cross(point, point_end, ver1[i],ver1[i+1]) :
            cross_n += 1
            #print(point)
            #print(ver[i])
            #print(ver[i+1])
    return cross_n
    

def issssss_solution(tangram, shape)  :
    #如果inside就错
    for colorrrr,verrrr in shape.items() :
        shape_ = verrrr
    #shape_ = shape.values()
        for color,ver in tangram.items() :
            for point in ver :
                if inside(point,shape_) :
                    #print('inside')
                    return False

    return True
    
def inside(point,ver) :
    ver1 = ver + ver[:1]
    for i in range(len(ver1)-1) :
        if point_in_line(point,ver1[i], ver1[i+1]) :
            return False
    cross_n = cross_number(point, ver)
    #print(cross_n)
    if cross_n % 2 == 1 :
        #print(#'c=',point)
        #print(ver1)
        return True
    if cross_n % 2 == 0 :
        return False    

def zhongdian(tangram) :
    new_ver = []
    new_dict = {}
    for col,ver in tangram.items():
        ver1 =ver +ver[:1]
        new_ver = []
        for i in range(len(ver1)-1) :
            new_ver.append([(ver1[i][0]+ver1[i+1][0])/2,(ver1[i][1]+ver1[i+1][1])/2])
        new_dict[col]=new_ver
    return new_dict
#shape = available_coloured_pieces(ff)
#tangram = available_coloured_pieces(f)
#is_solution(tangram, shape)
    


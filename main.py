from shutil import which
from flask import Flask
app = Flask(__name__)


#튜플각이다
a = 1,1
b = 2,1
c = 3,1
d = 1,2
e = 2,2
f = 3,2
g = 1,3
h = 2,3
i = 3,3

# 0또는 1로 모양 드러내자
a = [a,1]
b = [b,1]
c = [c,1]
d = [d,1]
e = [e,1]
f = [f,1]
g = [g,1]
h = [h,1]
i = [i,1]

jaryo = [a,b,c,d,e,f,g,h,i]
jaryo1 = [a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1]]

#(list(tuple))

count = 0

def onclick(a):
    count=0
    count+=1
    x1 = (a[0][0]+1)
    x2 = (a[0][0]-1)
    y1 = (a[0][1]+1)
    y2 = (a[0][1]-1)
    
    n=a[0][0]
    m=a[0][1]

    for i in jaryo:
        if i[0] == (x1,m):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (x2,m):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (n,y1):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (n,y2):
            i[1]+=1
            if i[1]==2:
                i[1]=0    



@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>bueongyi game</title>
            <style>
                h1{text-align: center;
                font-size: 5rem;}
                button{text-align: center;
                margin: auto;
                display:block
                }
                button{
                    width:35rem;
                    height: 7rem;
                    font-size: 3rem;
                }

                @media(max-width:650px){
                    button{
                        width:12rem;
                        height:3rem;
                        font-size:1rem;
                    }
                    h1{
                        font-size: 3rem;
                    }
                }

            </style>
        </head>
        <body>
            <h1>Let's play the Bueongyi Game?</h1>
            <div>
                <button onclick = "location.href = '/how_to_play/'">How to play</button>
                <br>
                <button onclick = "location.href = '/choose_stage/'">Go</button>
                <br>
                <button onclick = "location.href = '/choose_stage/'">Record</button>

            </div>
        </body>
        </html>
    '''

@app.route('/how_to_play/')
def how():
    return '''
            
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>how to play</title>
            <style>
                h1{text-align: center;
                font-size: 5rem;}

                button{text-align: center;
                margin: auto;
                display:block
                }
                button{
                    width:20rem;
                    height: 9rem;
                    font-size: 3rem;
                }
                text{
                    text-align: center;
                }

                @media(max-width:650px){
                    button{
                        width:12rem;
                        height:3rem;
                        font-size:1rem;
                    }
                    h1{
                        font-size: 3rem;
                    }
                }

                #info{
                    text-align: center;
                }

                div{text-align:center;
                margin:1rem}
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">How to play</h1>
            <div id="info">
                1. 하나의 부엉이를 클릭할 경우 그 주변의(사면) 부엉이들의 모양이 바뀐다.<br>
                2. 화면 우상단에 있는 부엉이의 모양을 보고 그대로 만들어 주시면 된다.<br>

            </div>

            <br>
            <div>
                <button style = "display:inline" onclick = "location.href = '/'"> Go back </button>
                <button style = "display:inline" onclick = "location.href = '/choose_stage/'"> Choose stage </button>
            </div>
        </body>
        </html>
    '''

@app.route('/choose_stage/')
def choose():
    return '''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>

            <style media="screen">
                    
                .wrap #a{
                width: 98vw;
                height: 40vh;
                overflow-x: auto;
                white-space:nowrap;}
                    
                h1{
                margin:3rem;
                font-size: 3rem;
                text-align:center}

                img{
                    width:30vh;
                    height:20vh;
                    border-radius: 8px;
                }
                
            </style>

        </head>
        <body>
            <h1>choose stage</h1>
            <div class="wrap">
                <div id="a">           
                <button onclick = "location.href = '/game1/'">
                    <img src="bu1.png" />
                    <br>
                    <text>record</text>
                </button>
                <button>
                    <img src="2.png.jpg" />
                    <br>
                    <text>record</text>
                </button>          
                <button>
                    <img src="3.png.jpg" />
                    <br>
                    <text>record</text>
                </button>
                <button>
                    <img src="bu1.png" />
                    <br>
                    <text>record</text>
                </button>
                <button>
                    <img src="2.png.jpg" />
                    <br>
                    <text>record</text>
                </button>          
                <button>
                    <img src="3.png.jpg" />
                    <br>
                    <text>record</text>
                </button>
                <button>
                    <img src="bu1.png" />
                    <br>
                    <text>record</text>
                </button>
                <button>
                    <img src="2.png.jpg" />
                    <br>
                    <text>record</text>
                </button>          
                <button>
                    <img src="3.png.jpg" />
                    <br>
                    <text>record</text>
                </button>
                    
                    
                </div>
            </div>

        </body>
        </html>
    '''

al='bu1.png'
bl='bu1.png'
cl='bu1.png'
dl='bu1.png'
el='bu1.png'
fl='bu1.png'
gl='bu1.png'
hl='bu1.png'
il='bu1.png'

@app.route('/game1/')
def game1():
    for data in jaryo1:
        

            
        return '''
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>game 1</title>
                <style>
                    img{
                        width:25vw;
                        height:15vw;
                    }
                    div{
                        align-content: center;
                    }
                    button{
                        width:30vw;
                        height: 17vw;
                    }
                    @media(max-width:600px){
                        button{
                            width:20vw;
                            height:20vw;
                        }
                        img{
                            width:17vw;
                            height:12vw;
                        }

                    }    
                    </style>

            </head>
            <body>

                <h1 style="text-align: center;">
                    Stage 1
                </h1>
                <div style="text-align:right;">record</div>
                
                <div>
                    <button>
                        7
                        <img src="{}">
                    </button>
                    <button>8
                        <img src="{}">
                    </button>
                    <button>9
                        <img src="{}">
                    </button>
                    <br>
                    <button>4
                        <img src="{}">
                    </button>
                    <button>5
                        <img src="{}">
                    </button>
                    <button>6
                        <img src="{}">
                    </button>
                    <br>
                    <button>1
                        <img src="{}">
                    </button>
                    <button>2
                        <img src="{}">
                    </button>
                    <button>3
                        <img src="{}">
                    </button>
                </div>

            </body>
            </html>
        '''
app.run()
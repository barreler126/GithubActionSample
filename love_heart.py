# # 版权https://github.com/royalneverwin/beating-heart

# from tkinter import * # Python 实现GUI界面的包
# from math import sin, cos, pi, log
# import random
# import time

# CANVAS_WIDTH = 640
# CANVAS_HEIGHT = 480
# CANVAS_CENTER_X = CANVAS_WIDTH / 2
# CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
# IMAGE_ENLARGE = 11


# def scatter_inside(x, y, beta=0.15): # log scatter & scatter inside
#     ratiox = - beta * log(random.random()) #*** can modify ***#
#     ratioy = - beta * log(random.random())
#     dx = ratiox * (x - CANVAS_CENTER_X)
#     dy = ratioy * (y - CANVAS_CENTER_Y)
#     return x - dx, y - dy


# def heart_function(t, enlarge_ratio: float = IMAGE_ENLARGE):
#     # heart function
#     x = 16 * (sin(t)**3)
#     y = -(13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))

#     # enlarge
#     x *= enlarge_ratio
#     y *= enlarge_ratio

#     # shift to the center of canvas
#     x += CANVAS_CENTER_X
#     y += CANVAS_CENTER_Y

#     return int(x), int(y)

# def shrink(x, y, ratio):
#     sk_range = -1 / ((x-CANVAS_CENTER_X) ** 2 + (y-CANVAS_CENTER_Y) ** 2)
#     dx = ratio * sk_range * (x-CANVAS_CENTER_X)
#     dy = ratio * sk_range * (y-CANVAS_CENTER_Y)
#     return x - dx, y - dy


# class Heart:
#     def __init__(self, frame):
#         self.points = set()
#         self.edge_points = set()
#         self.inside_points = set()
#         self.all_points = {}
#         self.build(2000) #*** can modify ***#
#         self.frame = frame
#         for f in range(frame):  # pre calculate
#             self.calc(f)

#         # for halo
#         self.random_halo = 1000



#     def build(self, number):
#         # randomly find 'number' points on the heart curve
#         for _ in range(number):
#             t = random.uniform(0, 2 * pi) # t = angle
#             x, y = heart_function(t)
#             x, y = shrink(x, y, -1000)
#             self.points.add((int(x), int(y)))

#         # randomly find points on the edge
#         for px, py in self.points:
#             for _ in range(3): #*** can modify ***#
#                 x, y = scatter_inside(px, py, 0.05) #*** can modify ***#
#                 self.edge_points.add((x, y))

#         # randomly find points inside the heart
#         pt_ls = list(self.points)
#         for _ in range(4000): #*** can modify ***#
#             x, y = random.choice(pt_ls) # choice need idx, and set has no idx, only list has
#             x, y = scatter_inside(x, y) #*** can modify ***#
#             self.inside_points.add((x, y))


#     def cal_position(self, x, y, ratio): # calculate the position of points when beating
#         # attention: the closer to the center, the bigger beating range point has
#         bt_range = 1 / ((x-CANVAS_CENTER_X) ** 2 + (y-CANVAS_CENTER_Y) ** 2)
#         dx = ratio * bt_range * (x-CANVAS_CENTER_X) + random.randint(-1, 1)
#         dy = ratio * bt_range * (y-CANVAS_CENTER_Y) + random.randint(-1, 1)
#         return x - dx, y - dy


#     def calc(self, frame): # calculate points' position for different frame
#         ratio = 800 * sin(frame / 10 * pi) #*** can modify ***# this is 30 fps
#         all_pts = []

#         # for halo
#         halo_radius = int(4 + 6 * (1 + sin(self.frame / 10 * pi)))
#         halo_number = int(3000 + 4000 * abs(sin(self.frame / 10 * pi) ** 2))
#         heart_halo_point = set()
#         for _ in range(halo_number):
#             t = random.uniform(0, 2 * pi)
#             x, y = heart_function(t, enlarge_ratio=11.6)
#             x, y = shrink(x, y, halo_radius)
#             if (x, y) not in heart_halo_point:
#                 # 处理新的点
#                 heart_halo_point.add((x, y))
#                 x += random.randint(-14, 14)
#                 y += random.randint(-14, 14)
#                 size = random.choice((1, 2, 2))
#                 all_pts.append((x, y, size))

#         # on the curve
#         for x, y in self.points:
#             x, y = self.cal_position(x, y, ratio)
#             size = random.randint(1, 3) #*** can modify ***#
#             all_pts.append((x, y, size))

#         # on the edge
#         for x, y in self.edge_points:
#             x, y = self.cal_position(x, y, ratio)
#             size = random.randint(1, 2) #*** can modify ***#
#             all_pts.append((x, y, size))

#         # inside
#         for x, y in self.inside_points:
#             x, y = self.cal_position(x, y, ratio)
#             size = random.randint(1, 2) #*** can modify ***#
#             all_pts.append((x, y, size))

#         self.all_points[frame] = all_pts


#     def render(self, canvas, frame): # draw points
#         for x, y, size in self.all_points[frame % self.frame]: # set operation
#             canvas.create_rectangle(x, y, x+size, y+size, width=0, fill='#ff7171')


# def draw(root: Tk, canvas: Canvas, heart: Heart, frame=0):
#     canvas.delete('all')
#     heart.render(canvas, frame)
#     root.after(30, draw, root, canvas, heart, frame+1)


# if __name__ == '__main__':
#     root = Tk()
#     root.title('漂亮宝贝一周年快乐')
#     canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
#     canvas.pack()
#     heart = Heart(20)
#     draw(root, canvas, heart)
#     root.mainloop()
'''
import streamlit as st
url = st.text_input('请输入网址：', 'https://www.baidu.com')
if st.button('确认'):
    st.components.v1.iframe(url, height=600)
'''
import streamlit as st
# from streamlit_chat import message
from streamlit.components.v1 import html

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

audio_path = "https://docs.google.com/uc?export=open&id=16QSvoLWNxeqco_Wb2JvzaReSAw5ow6Cl"
img_path = "https://www.groundzeroweb.com/wp-content/uploads/2017/05/Funny-Cat-Memes-11.jpg"
youtube_embed = '''
<iframe width="400" height="215" src="https://www.youtube.com/embed/LMQ5Gauy17k" title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>
'''

markdown = """
### HTML in markdown is ~quite~ **unsafe**
<blockquote>
  However, if you are in a trusted environment (you trust the markdown). You can use allow_html props to enable support for html.
</blockquote>

* Lists
* [ ] todo
* [x] done

Math:

Lift($L$) can be determined by Lift Coefficient ($C_L$) like the following
equation.

$$
L = \\frac{1}{2} \\rho v^2 S C_L
$$

~~~py
import streamlit as st

st.write("Python code block")
~~~

~~~js
console.log("Here is some JavaScript code")
~~~

"""

table_markdown = '''
A Table:

| Feature     | Support              |
| ----------: | :------------------- |
| CommonMark  | 100%                 |
| GFM         | 100% w/ `remark-gfm` |
'''

st.session_state.setdefault(
    'past', 
    ['plan text with line break',
     'play the song "Dancing Vegetables"', 
     'show me image of cat', 
     'and video of it',
     'show me some markdown sample',
     'table in markdown']
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': 'Line 1 \n Line 2 \n Line 3'},
     {'type': 'normal', 'data': f'<audio controls src="{audio_path}"></audio>'}, 
     {'type': 'normal', 'data': f'<img width="100%" height="200" src="{img_path}"/>'}, 
     {'type': 'normal', 'data': f'{youtube_embed}'},
     {'type': 'normal', 'data': f'{markdown}'},
     {'type': 'table', 'data': f'{table_markdown}'}]
)

st.title("Chat placeholder")

chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False
        )
    
    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")




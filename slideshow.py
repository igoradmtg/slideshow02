# -*- coding: utf-8 -*-
from moviepy.editor import *
from moviepy.editor import TextClip,VideoFileClip, concatenate_videoclips

dir_name = "" 
dir_output = ""
fnamemp4 = "File.mp4"
text_site = "https://github.com/igoradmtg" # Текст для интро и аутро
#fontsize_intro = 80 # Размер шрифта для интро и аутро
#W = 1920 # clip width 1920
#H = 1080 # clip height 1080 
fontsize_intro = 50 # Размер шрифта для интро и аутро
Video_type = 3 # Разрешение для видео 1 - 720х480, 2 - 854x480, 3 - 1280x720, 4 - 1920x1080
if Video_type == 1:
    W = 720 # clip width 1280
    H = 480 # clip height 720 
elif Video_type == 2:    
    W = 854 # clip width 1280
    H = 480 # clip height 720 
elif Video_type == 3:    
    W = 1280 # clip width 1280
    H = 720 # clip height 720 
elif Video_type == 4:    
    W = 1920 # clip width 1280
    H = 1080 # clip height 720 
    
DW = 1 # 1 - Up  2 - Down
DH = 1 # 1 - Left 2 - Right
K_W_H = W / H # Коэффициент ширина и высота 1920 / 1080 = 1,77777
SIZE = (W, H)
CHANGE_DIRECTION = True # Менять направление 
    
def intro() :
  global text_site, SIZE, fontsize_intro
  duration_intro = 2 # Длительность каждого текстового клипа
  logo1 = (TextClip(txt=text_site,color="#0000AA", align='West',fontsize=fontsize_intro,font = 'Arial').set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
  logo1_clip = CompositeVideoClip([logo1.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255])  
  logo2 = (TextClip(txt="present",color="#0000AA", align='West',fontsize=fontsize_intro,font = 'Arial').set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
  logo2_clip = CompositeVideoClip([logo2.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255])  
  return concatenate_videoclips([logo1_clip,logo2_clip])
  
def outro() :
  global text_site, SIZE, fontsize_intro
  duration_intro = 4 # Длительность каждого текстового клипа
  logo1 = (TextClip(txt=text_site,color="#0000AA", align='West',fontsize=fontsize_intro,font = 'Arial').set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
  return CompositeVideoClip([logo1.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255])
  
def slide_clip(fname) :
    global DW, DH, SIZE, W, H, K_W_H, CHANGE_DIRECTION
    def calc_up(t, duration, h1):
        if t<2 :
          val = 0
        elif t>14 :
          val = H-h1
        else :
          val = (H-h1)*((t-2)/duration)
        return ('center', val)
    def calc_dwn(t, duration, h1):
        if t<2 :
          val = H-h1
        elif t>14 :
          val = 0
        else :
          val = (H-h1)*(1-((t-2)/duration))
        return ('center', val)
    def calc_left(t, duration, w1):
        if t<2 :
          val = 0
        elif t>14 :
          val = W-w1
        else :
          val = (W-w1)*((t-2)/duration)
        return (val,'center')
    def calc_right(t, duration, w1):
        if t<2 :
          val = W-w1
        elif t>14 :
          val = 0
        else :
          val = (W-w1)*(1-(t-2)/duration)
        return (val,'center')
    clip = ImageClip(fname).set_duration(16)
    clip_w = clip.w # Ширина клипа (Например 4608)
    clip_h = clip.h # Высота клипа (Например 3072)
    clip_k = clip_w / clip_h # Коэффициент ширины и высоты клипа (Например 4608 / 3072 = 1,5)
    print("clip_w =", clip_w,"clip_h =", clip_h,"clip_k =", clip_k) 
    if clip_k < K_W_H : 
      clip = clip.resize(width=W)
      clip_w = clip.w # Ширина клипа (Например 4608)
      clip_h = clip.h # Высота клипа (Например 3072)
      print("clip_resize width", clip_w) 
      if CHANGE_DIRECTION == True :
        if DW==1 :
          DW=2
          return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_dwn(t,12,clip_h))],size=SIZE)
        else :
          DW=1
          return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_up(t,12,clip_h))],size=SIZE)
      else:
        return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_up(t,12,clip_h))],size=SIZE)
      
    else :
      clip = clip.resize(height=H)
      clip_w = clip.w # Ширина клипа (Например 4608)
      clip_h = clip.h # Высота клипа (Например 3072)
      print("clip_resize height", clip_h) 
      if CHANGE_DIRECTION == True :
        if DH==1 :
          DH=2
          return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_right(t,12,clip_w))],size=SIZE)
        else :
          DH=1
          return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_left(t,12,clip_w))],size=SIZE)
      else :
        return CompositeVideoClip([clip.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255]).set_pos(lambda t: calc_left(t,12,clip_w))],size=SIZE)
    

def save_clip() :
  global dir_name, fnamemp4 , SIZE , dir_output
  clip_list = []
  names = os.listdir(dir_name)
  # Сортируем 
  names.sort()
  for name in names:
    #print("File ",name)
    if name.lower().find(".jpg") == -1 :
      print("Пропуск файла ",name)
      continue
    fullname = os.path.join(dir_name, name) # получаем полное имя
    if not os.path.isfile(fullname) :
      print("Не найден файл ",fullname)
      continue
    print(fullname)
    clip_list.append(slide_clip(fullname))
  # Объеденение всех клипов в один
  final_clip_f = concatenate_videoclips(clip_list)
  # Делаем клип текстовый логотип верхний правый угол и длительностью final_clip_f.duration
  logo = (TextClip(txt=text_site, color='white', align='West',fontsize=16,font = 'Arial-Bold').set_duration(final_clip_f.duration).margin(right=8, top=8, opacity=0).set_pos(("right","top")))
  # Создаем клип с наложенным логотипом
  final_clip_f2 = CompositeVideoClip([final_clip_f,logo], size=SIZE)         
  #final_clip_f3 = concatenate_videoclips([intro(),final_clip_f2])         
  # Добавляем интро и аутро
  final_clip_f3 = concatenate_videoclips([intro(),final_clip_f2,outro()])
  # Сохранение клипа в файл
  final_clip_f3.write_videofile(dir_output+fnamemp4, fps=30, threads=4, audio = False)

def main(arg1, arg2, arg3) : 
  global dir_name, fnamemp4, dir_output
  dir_name = arg1
  fnamemp4 = arg2
  dir_output = arg3
  save_clip()
  
if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2], sys.argv[3])  
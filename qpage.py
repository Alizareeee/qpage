import os 
import shutil #Library For Work With File In High Level Like Copy
import datetime # For Adding System Time To Homepage

work_dir= os.getcwd() # Get Current Directory
image_dir = work_dir+"\\image"
doc_dir=work_dir+"\\doc"
out_dir=work_dir+"\\output"
font_dir=work_dir+"\\font"
page_name=["Home","Resume","Project","About Me"] # list of Page Title In Menu Maker
actual_name=["index","resume","project","about"] # List Of Pages Actual name like index.html
break_line="<hr></hr>\n"
homepage="http://sepandhaghighi.github.io/qpage/page.html"
version="V1.5.3"
color_box=["White","Black", "Purple", "Yellow", "Orange", "Green", "Blue"] # Color list for background and text
size_box=["50px","100px","200px","360px","500px"] # list of size of images
imformat_box=["jpg","bmp","png","gif","tiff"] # list of supported image format
fontstyle_box=["normal","italic","oblique"]
font_format=[".ttf",".woff",".svg",".eot"]
today_time=str(datetime.date.today()) # Get Tody Date By datetime module
    
#css_classes=["menu_color"]
def menu_maker(): # Top Menu Maker In each html page
    result="<center>"
    for i in range(len(page_name)):

        result=result+'\t<a href="'+actual_name[i]+'.html">'+page_name[i]+"</a>\n" #  Hyper Link To Each Page In HTML File
        result=result+"&nbsp\n"
    result=result+"</center>"
    result=result+"\t\t"+break_line # Add Break line to End Of The Menu
    return result # Return All Of The Menu
def menu_writer():  # Write menu_maker output in html file
    message=menu_maker()
    for i in range(len(page_name)):
        file=open(out_dir+"\\"+actual_name[i]+".html","a")
        file.write(message)
        file.close()
        
def html_init(name): # Create Initial Form Of each Html Page Like Title And HTML  And Body Tag
    html_name= out_dir+"\\"+name+".html"
    file=open(html_name,"w")
    file.write("<html>\n")
    file.write("\t<head>\n")
    if name=="index":
        file.write("\t\t<title>Welcome To My Homepage</title>\n")
    else:
        file.write("\t\t<title>"+name.upper()+"</title>\n")
    file.write('<link rel="stylesheet" href="styles.css" type="text/style"/>\n')
    file.write("\t</head>\n")
    file.write("\t<body>\n")
    file.close()
def html_end(name):   # Create End Of The Html file
    html_name= out_dir+"\\"+name+".html"
    file=open(html_name,"a")
    file.write("\t</body>\n")
    file.write("</html>")
    file.close()
def print_text(text_file,file,center=False,close=False): # Write Text Part Of Each Page
    text_code=""
    header_start='<h4 class="color_tag">'
    header_end="</h4>"
    space="&nbsp\n"
    for line in text_file:
        header_start='<h4 class="color_tag">'
        header_end="</h4>"
        line.strip()
        text=line
        if len(line)==1: # For Detecting White Space
            text_code=space
        else:   # Detecting Font Size
            if line.find("[L]")!=-1:
                header_start='<h2 class="color_tag">'
                header_end="</h2>"
                text=line[3:]
            elif line.find("[S]")!=-1:
                header_start='<h5 class="color_tag">'
                header_end="</h5>"
                text=line[3:]
            elif line.find("[M]")!=-1:
                text=line[3:]
        if center==True: # Centerizes Text If Condition Is True For Manual Centering
            header_start="<center>"+header_start
            header_end=header_end+"</center>"
        if text.find("[center]")!=-1: # Find Center Tag In Each Line
            header_start="<center>"+header_start
            header_end=header_end+"</center>"
            text=text[:text.find("[center]")]
        text_code=header_start+text+header_end+"\n"
        file.write(text_code)
    if close==True:   
        file.close()
def print_image(file,close=False,imformat="jpg"): # Write Image Part OF The Page
    for i in range(len(size_box)):
        print(i,"-",size_box[i])
    image_size=int(input("Please Enter Profile Image Size : ")) # Choose Profile Image Size
    image_size_string=size_box[2] # Getting Html String From size_box list default mode (Medium)
    if image_size>=0 and image_size<len(size_box):
        image_size_string=size_box[image_size]
    image_code='<center><img src="image.'+imformat+'"'+ ', width='+image_size_string+'></img></center>\n'
    file.write(image_code)
    if close==True:
        file.close()
def print_download(file,name,link,center=False,close=False): # Create Download Link In Page
    link_code="<a href="+'"'+link+'"'+">"+name+"</a>"
    if center==True:
        link_code="<center>"+link_code+"</center>"
    file.write(link_code+"\n")
    file.write(break_line)
    if close==True:
        file.close()
def print_adv(file,close=True):
    file.write(break_line)
    file.write("<center><a href="+'"'+homepage+'"'+">"+"Generated "+today_time+" By"+"QPage "+version+"</a></center>")
    if close==True:
        file.close()
def contain(name): # main fucntion That Open Each Page HTML File and call other function to write data in it
        file=open(out_dir+"\\"+name+".html","a")
        text_file=open(doc_dir+"\\"+name+".txt","r")
        resume_name=""
        image_name=""
        imformat="jpg"
        if name=="index":
            file_of_images=os.listdir(image_dir)
            for i in range(len(file_of_images)):
                for form in imformat_box: 
                    if file_of_images[i].find("."+form)!=-1:
                        image_name=image_dir+"\\"+file_of_images[i]
                        imformat=form
                        break     
            shutil.copyfile(image_name,out_dir+"\\image."+imformat)
            print_image(file,imformat=imformat)
            print_text(text_file,file)
            print_adv(file)
        elif name=="resume":
            file_of_docs=os.listdir(doc_dir)
            for i in range(len(file_of_docs)):
                if file_of_docs[i].find(".pdf")!=-1:
                    resume_name=doc_dir+"\\"+file_of_docs[i]
                    break
            shutil.copyfile(resume_name,out_dir+"\\Resume.pdf")        
            print_download(file,"Download Full Version","Resume.pdf",center=True)
            print_text(text_file,file)
            print_adv(file)
        else:
            print_text(text_file,file)
            print_adv(file)
def clear_folder(path): # This Function Get Path Of Foldr And Delte Its Contains
    list_of_files=os.listdir(path)
    for file in list_of_files:
        os.remove(path+"\\"+file)
def css_creator(): # Ask For background and text color in
    font_flag=0 # 0 If there is no font file in font_folder
    font_section=""
    for i in range(len(color_box)):
        print(i,"-",color_box[i])
    back_color_code=int(input("Please enter your background color : "))
    if back_color_code not in range(7):
        back_color_code=0
    text_color_code=int(input("Please enter your text color : "))
    if text_color_code not in range(7):
        text_color_code=1
    background_color=color_box[back_color_code] # convert code to color string in color_box
    text_color=color_box[text_color_code] # convert code to color string in color_box
    font_folder=os.listdir(font_dir)
    for i in font_folder:
        for j in range(len(font_format)):# search for other font format in font box
            if i.find(font_format[j])!=-1: # If there is a font in font folder
                shutil.copyfile(font_dir+"\\"+i,out_dir+"\\qpage"+font_format[j]) # copy font file to output folder
                font_flag=1 # Turn Flag On
                current_font_format=font_format[j] # font format of current selected font for css editing
    css_file=open(out_dir+"\\styles.css","w") # open css file
    if font_flag==1: # check flag if it is 1
        css_file.write("@font-face{\nfont-family:qpagefont;\nsrc:url(qpage"+current_font_format+");\n}") # wrtie font-face in html
        font_section="font-family:qpagefont;\n" # Update Font Section For Body Tag
        for i in range(len(fontstyle_box)):
            print(i,"-",fontstyle_box[i])
        font_style=int(input(" Please choose your font style "))
        if font_style<len(fontstyle_box):
            font_style=fontstyle_box[font_style]
        else:
            font_style="normal"
        font_section=font_section+"font-style:"+font_style+";\n"
    css_file.write("body{\n"+"background:"+background_color+";\n"+font_section+"}\n") # write body tag
    css_file.write(".color_tag{\n"+"color:"+text_color+";\n}") # write color_tag in css
    css_file.close() # close css file

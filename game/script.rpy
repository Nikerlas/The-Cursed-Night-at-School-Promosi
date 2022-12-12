#transform
transform long_shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

transform short_shake:
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
#END TRANSFORM

init python:
    renpy.music.register_channel("noise")

#BG
image bg black = "images/bg/bg black.png"
image bg district = "images/bg/scene.jpg"
image bg schoolyard = "images/bg/outschool.jpg"
image bg hallway = "images/bg/corridor.jpg"
image bg hallway2 = "images/bg/corridor2.jpg"
image bg aclass = "images/bg/inclass.jpg"
image bg library = "images/bg/perpus.png"
image bg canteen = "images/bg/canteen.jpg"
image bg osisdepan = "images/bg/bg osisdepan.jpg"
#BG RESMI
image bg council normal= "images/bg/councilnormal.png"
image bg councildimension= "images/bg/bg osis.png"

image bg schoolyard morning = "images/bg/bg schoolyard morning.png"
image bg schoolyard noon = "images/bg/bg schoolyard noon.png"
image bg schoolyard afternoon = "images/bg/bg schoolyard afternoon.png"
image bg schoolyard dimension = "images/bg/bg schoolyard dimension.png"

image bg hallway morning = "images/bg/bg hallway morning.png"
image bg hallway noon = "images/bg/bg hallway noon.png"
image bg hallway afternoon = "images/bg/bg hallway afternoon.png"
image bg hallway dimension = "images/bg/bg hallway dimension.png"

image bg classroom morning = "images/bg/bg classroom morning.png"
image bg classroom noon = "images/bg/bg classroom noon.png"
image bg classroom afternoon = "images/bg/bg classroom afternoon.png"
image bg classroom dimension = "images/bg/bg classroom dimension.png"

image bg canteen morning = "images/bg/bg canteen morning.png"
image bg canteen noon = "images/bg/bg canteen noon.png"
image bg canteen dimension = "images/bg/bg canteen dimension.png"

image bg way morning = "images/bg/bg scene morning.png"
image bg way noon = "images/bg/bg scene noon.png"
image bg way afternoon = "images/bg/bg scene afternoon.png"
image bg way dimension = "images/bg/bg scene dimension.png"

#END BG

#IMG CHARA
#ZAKY
#--------> talk
image zakyangry = "images/zaky/talk/ZakyAngry.png"
image zakyhappy = "images/zaky/talk/ZakyHappy.png"
image zakyhappy2 = "images/zaky/talk/ZakyHappy2.png"
image zakyhesitant = "images/zaky/talk/ZakyHesitant.png"
image zakynormal = "images/zaky/talk/ZakyNormal.png"
image zakysad = "images/zaky/talk/ZakySad.png"
image zakyscary = "images/zaky/talk/ZakyScary.png"
image zakyscared = "images/zaky/talk/ZakyScared.png"
image zakysmile = "images/zaky/talk/ZakySmile.png"
image zakysuprised = "images/zaky/talk/ZakySurprised.png"
image zakytalk = "images/zaky/talk/ZakyTalk.png"
image zakyworry = "images/zaky/talk/ZakyWorry.png"
#--------> idle
image idlezakyangry = "images/zaky/idle/ZakyAngry.png"
image idlezakyhappy = "images/zaky/idle/ZakyHappy.png"
image idlezakyhappy2 = "images/zaky/idle/ZakyHappy2.png"
image idlezakyhesitant = "images/zaky/idle/ZakyHesitant.png"
image idlezakynormal = "images/zaky/idle/ZakyNormal.png"
image idlezakysad = "images/zaky/idle/ZakySad.png"
image idlezakyscary = "images/zaky/idle/ZakyScary.png"
image idlezakyscared = "images/zaky/idle/ZakyScared.png"
image idlezakysmile = "images/zaky/idle/ZakySmile.png"
image idlezakysurprised = "images/zaky/idle/ZakySurprised.png"
image idlezakytalk = "images/zaky/idle/ZakyTalk.png"
image idlezakyworry = "images/zaky/idle/ZakyWorry.png"

#KEVIN
#--------> talk
image kevincheerful = "images/kevin/talk/KevinCheerful.png"
image kevinhappy = "images/kevin/talk/KevinHappy.png"
image kevinserious = "images/kevin/talk/KevinSerious.png"
image kevinsmile = "images/kevin/talk/KevinSmile.png"
image kevintalk = "images/kevin/talk/KevinTalk.png"
#--------> Idle
image idlekevintalk = "images/kevin//idle/KevinTalk.png"
image idlekevinhappy = "images/kevin/idle/KevinHappy.png"
image idlekevinserious = "images/kevin/idle/KevinSerious.png"
image idlekevinsmile = "images/kevin/idle/KevinSmile.png"
image idlekevincheerful = "images/kevin/idle/KevinCheerful.png"
#-------->

#YERI di resize anjir kegeden
#--------> talk
image yeriangry1 = "images/yeri/talk/YeriAngry.png"
image yeriangry2 = "images/yeri/talk/YeriAngry2.png"
image yericheerful = "images/yeri/talk/YeriCheerful.png"
image yerihappy = "images/yeri/talk/YeriHappy.png"
image yerinormal = "images/yeri/talk/YeriNormal.png"
image yerisad = "images/yeri/talk/YeriSad.png"
image yeriscared = "images/yeri/talk/YeriScared.png"
image yerishy = "images/yeri/talk/YeriShy.png"
image yerismile = "images/yeri/talk/YeriSmile.png"
image yerisurprised = "images/yeri/talk/YeriSurprised.png"
image yeritalk = "images/yeri/talk/YeriTalk.png"
image yeritsundere1 = "images/yeri/talk/YeriTsundere1.png"
image yeritsundere2 = "images/yeri/talk/YeriTsundere2.png"
#--------> idle
image idleyeriangry1 = "images/yeri/idle/YeriAngry.png"
image idleyeriangry2 = "images/yeri/idle/YeriAngry2.png"
image idleyericheerful = "images/yeri/idle/YeriCheerful.png"
image idleyerihappy = "images/yeri/idle/YeriHappy.png"
image idleyerinormal = "images/yeri/idle/YeriNormal.png"
image idleyerisad = "images/yeri/idle/YeriSad.png"
image idleyeriscared = "images/yeri/idle/YeriScared.png"
image idleyerishy = "images/yeri/idle/YeriShy.png"
image idleyerismile = "images/yeri/idle/YeriSmile.png"
image idleyerisurprised = "images/yeri/idle/YeriSurprised.png"
image idleyeritalk = "images/yeri/idle/YeriTalk.png"
image idleyeritsundere1 = "images/yeri/idle/YeriTsundere1.png"
image idleyeritsundere2 = "images/yeri/idle/YeriTsundere2.png"
#-------->

#CITRA
#--------> talk
image citranormal = "images/citra/talk/CitraNormal.png"
image citrahappy = "images/citra/talk/CitraHappy.png"
image citrahappy2 = "images/citra/talk/CitraHappy2.png"
image citrastartled = "images/citra/talk/CitraStartled.png"
image citrairritated = "images/citra/talk/CitraIrritated.png"
image citratalk = "images/citra/talk/CitraTalk.png"
image citrascared = "images/citra/talk/CitraScared.png"
image citrasmile = "images/citra/talk/CitraSmile.png"
#--------> idle
image idlecitranormal = "images/citra/idle/CitraNormal.png"
image idlecitrahappy = "images/citra/idle/CitraHappy.png"
image idlecitrahappy2 = "images/citra/idle/CitraHappy2.png"
image idlecitrastartled = "images/citra/idle/CitraStartled.png"
image idlecitrairritated = "images/citra/idle/CitraIrritated.png"
image idlecitratalk = "images/citra/idle/CitraTalk.png"
image idlecitrascared = "images/citra/idle/CitraScared.png"
image idlecitrasmile = "images/citra/idle/CitraSmile.png"
#NPC
#-------->
image satpam_a = "images/npc/satpam.png"
image satpam_b = "images/npc/satpam_a.png"
#-------->
#Yuki
#--------> talk
image kuntinormal = "images/ghost/talk/kunti.png"
image kuntiangry = "images/ghost/talk/marah.png"
image kuntilaugh = "images/ghost/talk/laugh.png"
#--------> idle
image idlekuntinormal = "images/ghost/idle/kunti.png"
image idlekuntiangry = "images/ghost/idle/marah.png"
image idlekuntilaugh = "images/ghost/idle/laugh.png"
#END IMG CHARA

# CHARACTER
#YERI
define y = Character('Yeri')
define y_shout = Character("Yeri", what_size=50)
define y_whisper = Character("Yeri", what_size=22)
#ZAKY
define z = Character('Zaky')
define z_shout = Character("Zaky", what_size=50)
define z_whisper = Character("Zaky", what_size=22)
#KEVIN
define k = Character('Kevin')
define k_shout = Character("Kevin", what_size=50)
define k_whisper = Character("Kevin", what_size=22)
#CITRA
define c = Character('Citra')
define c_shout = Character("Citra", what_size=50)
define c_whisper = Character("Citra", what_size=36)
#MC
define u = Character('???')
define u_shout = Character("???", what_size=50)
define u_whisper = Character("???", what_size=22)
define p = Character('[name]')
define p_shout = Character("[name]", what_size=50)
define p_whisper = Character("[name]", what_size=22)
#Mix
define kyc = Character("Kevin, Yeri, dan [name]")
define zc = Character("[name] dan Zaky")
define yc = Character("Yeri dan Citra")
define zc_shout = Character("[name] dan Zaky", what_size=50)
#PENJAGA KANTIN
define pk = Character("Penjaga Kantin")
#SECRET
#HANTU
define g = Character("Yuki")
define g_shout = Character("Yuki", what_size=50)
define g_whisper = Character("Yuki", what_size=22)
#-------->
define s_a = Character("Satpam A")
define s_b = Character("Satpam B")
#GAME START
#-------->

label start:
    scene bg black
    with dissolve

    python:
        diary01 = Item("Diary 01", image="gui/inventory/inv_diary01.png")  
        diary02 = Item("Diary 02", image="gui/inventory/inv_diary02.png")  
        diary03 = Item("Diary 03", image="gui/inventory/inv_diary03.png")  
        diary04 = Item("Diary 04", image="gui/inventory/inv_diary04.png")  
        diary05 = Item("Diary 05", image="gui/inventory/inv_diary05.png")  
        diary06 = Item("Diary 06", image="gui/inventory/inv_diary06.png")  
        diary07 = Item("Diary 07", image="gui/inventory/inv_diary07.png")  
        diary08 = Item("Diary 08", image="gui/inventory/inv_diary08.png")  
        diary09 = Item("Diary 09", image="gui/inventory/inv_diary09.png")  
        inventory = Inventory()

    #field name
    python:
        name = renpy.input("Siapa namamu: ")

        name = name.strip() or "You"

    scene bg district
    with dissolve

    python:
        renpy.notify("Distrik A")

    stop music fadeout 1.0

    "Pagi hari ini terasa sangat cerah tidak seperti biasa."
    "Dengan semangat pagi yang membara aku pergi menuju sekolahku."

    show idlekevinserious with dissolve

    "Dari kejauhan aku melihat Kevin sedang berjalan dipinggir jalan."

    p 'Hello Kevin. Bagaimana kabarmu?'

    hide idlekevinserious 

    show kevincheerful at short_shake, center

    k 'Hai [name], baik kok! bagaimana denganmu?'

    hide kevincheerful
    show idlekevincheerful

    p 'Baik seperti biasa kok ahahahaha...'

    hide idlekevincheerful
    show kevincheerful

    k 'Kamu mau menuju sekolah?'

    hide kevincheerful
    show idlekevincheerful

    p 'Iyalah! Aku sudah memakai pakaian kek gini.'
    p 'Masak ga pergi sekolah.'

    hide idlekevincheerful
    show kevinhappy at short_shake,center

    k 'Ahahaha... Maaf aku cuma bercanda tadi.'

    scene bg schoolyard morning with dissolve
    python:
        renpy.notify("Halaman Sekolah")

    stop noise fadeout 1.0

    "Kami berdua berjalan menuju sekolah."
    "Sesampainya disekolah, Kevin mengingatkanku tentang rapat OSIS sehabis pulang sekolah nanti."

    show kevintalk with dissolve

    k 'Eh... Jangan lupa nanti ya! Sehabis pulang sekolah buat rapat untuk acara Ulang Tahun sekolah kita.'

    hide kevintalk
    show idlekevintalk

    p 'Okay... Pasti aku datang kok.'
    p 'Aku kan anak rajin.'

    hide idlekevintalk
    show kevinhappy at short_shake, center

    k 'Heleh ahahahaha.'

    hide kevin
    scene bg hallway morning with dissolve
    python:
        renpy.notify("Lorong Sekolah")


    "Aku menuju ke ruang kelasku."
    "Saat di pertengahan perjalanan aku dan Kevin bertemu Yeri lalu menyapanya."

    show idleyerinormal with dissolve

    p 'Hai Yeri. Bagaimana kabarmu?'
 
    hide idleyerinormal
    show yerihappy at short_shake, center

    y 'Hai [name], baik kok. Bagaimana denganmu?'

    hide yerihappy
    show idleyerihappy

    p 'Baik kok.'
    p "Aku dan Kevin ke kelas duluan dulu ya!"
    
    hide idleyerihappy
    show yerihappy
    
    y 'Okei!'

    hide yerihappy with dissolve

    scene bg classroom morning with dissolve
    python:
        renpy.notify("Kelas 2-A")

    "Sesampainya dikelas, aku langsung menuju ke tempat dudukku."
    "Saat aku sedang melamun. Tiba-tiba Zaky datang untuk menyapaku."
    
    show zakyhappy at long_shake, center

    z "[name]. Kamu kenapa melamun saja?" 
    z "Apa ada masalah dengan dirimu?"

    hide zakyhappy
    show idlezakyhappy

    p 'Tidak ada, aku cuma berpikir bernapas itu menyenangkan ya..'

    hide idlezakyhappy
    show zakyworry at short_shake, center

    z "Eh... "
    z "Iyadeh yang penting jangan lupa untuk ikut rapat nanti sepulang sekolah ya!"

    hide zakyworry
    show idlezakyworry

    p 'Iya... Santai aja. Aku inget kok.'

    hide idlezakyworry with dissolve

    "Tidak lama kemudian guru pun masuk kedalam ruangan untuk memulai pelajaran di pagi yang cerah ini."


    scene bg hallway with dissolve
    python:
        renpy.notify("Lorong Sekolah")

    "Bel istirahat pun berbunyi."
    "Lalu beberapa saat kemudian Yeri menghampiriku didepan kelasku."
    "Aku, Zaky, dan Kevin langsung keluar dari ruang kelas dan menghampiri posisi Yeri."

    show idlekevintalk with dissolve:
        xalign 0.0
        yalign 1.0

    show idleyerismile with dissolve:
        xalign 0.5
        yalign 1.0

    show idlezakyhappy with dissolve:
        xalign 1.0
        yalign 1.0

    hide idleyerismile
    show yerismile:
        xalign 0.5
        yalign 1.0

    y 'Hei [name], Kevin, Zaky yuk ke kantin. Mau ga?' 

    hide idlekevintalk
    show kevintalk:
        xalign 0.0
        yalign 1.0

    hide yerismile
    show idleyerismile:
        xalign 0.5
        yalign 1.0
    k "Kalau aku serah sih."
    hide kevintalk
    show idlekevintalk:
        xalign 0.0
        yalign 1.0
    hide idlezakyhappy
    show zakyhappy:
        xalign 1.0
        yalign 1.0
    z 'Aku oke aja.'
    z "Kalau [name] mau ga?"

    hide zakyhappy
    show idlezakyhappy:
        xalign 1.0
        yalign 1.0
    
    p 'Boleh saja sih... Tapi...'

    hide idlekevintalk
    show kevintalk at short_shake:
        xalign 0.0
        yalign 1.0

    k 'Ga usah pake tapi-tapian. Ayo gas berangkat.'

    hide kevintalk
    show idlekevinserious:
        xalign 0.0
        yalign 1.0

    p 'Tapi aku tu males banget coy...'

    hide idlezakyhappy
    show zakytalk:
        xalign 1.0
        yalign 1.0
    
    z 'Sudahlah ikut saja...'

    hide zakytalk
    show idlezakytalk:
        xalign 1.0
        yalign 1.0

    menu:
        "Aku akan ikut.":
            jump kantin_yes

        "Aku tidak ingin ikut.":
            jump kantin_no

#--------------------
#CANTEEN ROUTE
#-------------------
    label kantin_yes:

        $ menu_flag = True

        p 'Iya deh aku ikut. Yuk ke kantin.'
        
        hide idlekevinserious
        show kevincheerful at short_shake:
            xalign 0.0
            yalign 1.0

        k 'Nah gitu donk... Lama bet mikirnya dah ni anak.' 

        hide kevincheerful
        show idlekevinsmile:
            xalign 0.0
            yalign 1.0

        hide idleyerismile
        show yericheerful at short_shake, center

        y "Hahaha"
        y 'Yaudah yokkk berangkat!' 

        # 3 chara hilang bersamaan
        hide idlekevinsmile
        hide yericheerful
        hide idlezakytalk
        with dissolve

        "Kami berempat pergi menuju kantin bersama."
        "Dalam perjalanan menuju kantin, mereka bertiga membicarakan tentang rapat OSIS yang akan diadakan sore ini."
        "Aku terdiam sejenak, dan berpikir." 
        "Sejujurnya..." 
        
        menu:

            "Aku sangat antusias dengan rapat nanti.":
                jump choice2_yes
       
            "Aku kurang tertarik dengan rapat kali ini.":
                jump choice2_no

                label choice2_yes:

                    $ menu_flag = True

                    "Tiba-tiba Kevin memanggilku dengan keras dan itu membuatku terkejut." 
                    "Ternyata aku tertinggal jauh dari mereka. Lalu, aku menyusul mereka dengan cepat." 

                    scene bg canteen morning with dissolve
                    python:
                        renpy.notify("Kantin")

                    "Kami berempat telah tiba dikantin."
                    "Kevin dan Zaky lalu menuju tempat makanan, sedangkan aku dan Yeri mencari tempat duduk." 
                    "Kami berdua berhasil mendapatkan tempat duduk." 
                    "Lalu kami mendudukinya untuk menunggu Kevin dan Zaky." 
                    

                    show yerinormal with dissolve
                    
                    y 'Kamu tadi mengapa melamun?' 
                    y 'Apa yang sedang kamu pikirkan?' 

                    hide yerinormal
                    show idleyerinormal

                    p 'Ga ada apa-apa sih.' 

                    hide idleyerinormal
                    show yerinormal

                    y 'Ah boong kamu.'
                    p 'Beneran kok.'

                    hide yerinormal
                    show idleyerinormal

                    "Yeri menatapku dengan tatapan serius dicampur kesal."
                    "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

                    p "Aku cuma terlalu antusias aja untuk ikut rapat nanti."
                    
                    hide idleyerinormal
                    show yerismile
                
                    y 'Ya ampun kukira kamu mikirin apaan.' 
                    y 'Ternyata mikirin hal kayak gitu aja.' 

                    hide yerismile
                    show idleyerismile

                    p 'Ahahaha... Maaf ya...' 
                    
                    hide idleyerismile
                    show yericheerful at short_shake, center
                    
                    y 'Ga apa-apa.' 
                    y 'Kamu harus ikut rapat itu walaupun suka atau engga.'
                    
                    hide yericheerful
                    show yerismile

                    y 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 

                    hide yerismile
                    show idleyerismile

                    p 'Iya aku tau kok.' 

                    hide idleyerismile with dissolve

                    jump choice2_done

                label choice2_no:

                    $ menu_flag = False

                    "Tiba-tiba Kevin memanggilku dengan keras dan itu membuatku terkejut." 
                    "Ternyata aku tertinggal jauh dari mereka. Lalu, aku menyusul mereka dengan cepat." 

                    scene bg canteen morning with dissolve
                    python:
                        renpy.notify("Kantin")

                    "Kami berempat telah tiba dikantin."
                    "Kevin dan Zaky lalu menuju tempat makanan, sedangkan aku dan Yeri mencari tempat duduk." 
                    "Kami berdua berhasil mendapatkan tempat duduk." 
                    "Lalu kami mendudukinya untuk menunggu Kevin dan Zaky." 
                    

                    show yerinormal with dissolve
                    
                    y 'Kamu tadi mengapa melamun?' 
                    y 'Apa yang sedang kamu pikirkan?' 

                    hide yerinormal
                    show idleyerinormal

                    p 'Ga ada apa-apa sih.' 

                    hide idleyerinormal
                    show yerinormal

                    y 'Ah boong kamu.'
                    p 'Beneran kok.'

                    hide yerinormal
                    show idleyerinormal

                    "Yeri menatapku dengan tatapan serius dicampur kesal."
                    "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

                    p "Bukan masalah besar si, hanya saja aku kurang tertarik dengan rapat nanti."
                    
                    hide idleyerinormal
                    show yerismile
                
                    y 'Ya ampun kukira kamu mikirin apaan.' 
                    y 'Ternyata mikirin hal kayak gitu aja.' 

                    hide yerismile
                    show idleyerismile

                    p 'Ahahaha... Maaf ya...' 
                    
                    hide idleyerismile
                    show yericheerful at short_shake, center
                    
                    y 'Ga apa-apa.' 
                    y 'Kamu harus ikut rapat itu walaupun suka atau engga.'
                    
                    hide yericheerful
                    show yerismile

                    y 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 

                    hide yerismile
                    show idleyerismile

                    p 'Iya aku tau kok.' 

                    hide idleyerismile with dissolve

                    jump choice2_done
                
        label choice2_done:
         
            "Tak lama kemudian Kevin datang ke tempat dudukku dengan Citra." 

            show kevincheerful with dissolve

            k 'Kalian lagi membahas apa nih?' 

            show kevincheerful with move:
                xalign 0.3
                yalign 1.0 
            
            hide kevincheerful
            show idlekevincheerful:
                xalign 0.3
                yalign 1.0

            show yericheerful at right with dissolve:
                xalign 0.8
                yalign 1.0

            y "Ga ada apa-apa sih."

            hide yericheerful
            show idleyericheerful:
                xalign 0.8
                yalign 1.0

            p "Iya, ga ada apa-apa."

            hide idlekevincheerful
            show kevincheerful:
                xalign 0.3
                yalign 1.0

            k "Yang bener?"

            hide kevincheerful
            show idlekevincheerful:
                xalign 0.3
                yalign 1.0
            
            hide idleyericheerful
            show yeriangry2 at short_shake, right:
                xalign 0.8
                yalign 1.0

            y "Ga ada Kevin..."
            hide yeriangry2
            hide idlekevincheerful
            show kevinhappy at short_shake:
                xalign 0.3
                yalign 1.0

            show idleyeriangry2:
                xalign 0.8
                yalign 1.0
            k "Iya deh iya."

            hide idleyeriangry2
            hide kevinhappy
            with dissolve

            "Kevin mulai duduk di kursi meja kantin yang aku duduki."
            "Saat Kevin telah duduk."
            "Datanglah Citra dan Zaky."

            show citrahappy with dissolve:
                xalign 0.3
                yalign 1.0 
            show zakyhappy at right with dissolve:
                xalign 0.8
                yalign 1.0
            
            c "Nyahaloo..."
            z "Halo halo"

            hide citrahappy
            hide zakyhappy
            with dissolve

            show yerismile with dissolve

            y "Haii, Bagaimana kabarmu Cit?"

            show yerismile with move:
                xalign 0.3
                yalign 1.0 

            hide yerismile
            show idleyerismile:
                xalign 0.3
                yalign 1.0

            show citrahappy at right with dissolve:
                xalign 0.8
                yalign 1.0

            c "Baik kok!"

            hide idleyerismile
            show yericheerful at short_shake:
                xalign 0.3
                yalign 1.0 

            hide citrahappy
            show idlecitrahappy:
                xalign 0.8
                yalign 1.0

            y "Sini dong, kalian berdua ikut duduk!"
            
            hide idlecitrahappy
            show citrahappy:
                xalign 0.8
                yalign 1.0

            c "Okeiiii!"

            hide yericheerful
            hide citrahappy
            with dissolve

            "Citra dan Zaky mulai duduk di kursi meja kantin yang kutempati."
            "Saat mereka berempat sedang berbincang."
            

            jump promosi

#---------------
#LIBRARY ROUTE
#--------------

    label kantin_no:

        $ menu_flag = False
        p 'Ga dulu deh. Aku mau ke kamar mandi aja.' 

        hide kevinserious
        show kevintalk at short_shake, left

        k 'Yah ga asik lu!' 
        hide kevintalk
        
        hide idleyerismile
        show yeriangry2 at short_shake, center

        y 'Iya nih... Ga asik.' 
        hide yeriangry2
        show idleyeriangry2
        p 'Aku bilang ngga ya ngga anjir!'
        hide idlezakytalk
        show zakytalk:
            xalign 1.0
            yalign 1.0
        z 'Sudah deh biarin aja dia...' 
        hide zakytalk
        show idlezakynormal:
            xalign 1.0
            yalign 1.0
        hide idlekevinserious
        show kevintalk:
            xalign 0.0
            yalign 1.0
        k 'Yaudah deh... Yuk Yeri Zaky, Kita ke kantin.' 

        hide kevintalk
        hide idleyeriangry2 
        hide idlezakynormal 
        with dissolve

        "Mereka bertiga mulai berjalan menjauhiku." 
        "Sejujurnya aku tidak ingin pergi kekamar mandi." 
        "Tetapi, aku ingin ke Perpustakaan untuk menenangkan diri sebelum menghadapi rapat nanti." 
        "Karena perpustakaan adalah tempat yang tenang dan sunyi." 
        "Karena hal itulah aku ingin pergi ke perpustakaan." 

        scene bg library with dissolve
        python:
            renpy.notify("Perpustakaan")

        "Sesampainya di perpustakaan."
        "Hawa ketenangan mulai dirasakan oleh benakku."
        "Aku berpikir ini merupakan pilihan terbaik daripada pergi kekantin yang tempatnya sangat ramai."
        "Aku ingin mengambil salah satu buku di rak buku." 
        "Saat aku ingin mengambil buku tersebut. Tiba-tiba ada seseorang yang menepuk pundakku dan menyapaku." 

        u '"Halo..."'

        show idlecitrasmile with dissolve

        "Ternyata itu Citra." 

        p 'Ahhh Citra. Ada apa?'
        
        hide idlecitrasmile
        show citrahappy2 at short_shake, center

        c 'Aku boleh minta tolong ga?' 

        hide citrahappy2
        show idlecitrasmile

        p 'Minta tolong apa?'

        hide idlecitrasmile
        show citrasmile

        c 'Tolong ambilin buku itu donk.' 

        "Citra menunjuk buku diatas pojok kanan."

        menu:
            "Oke deh!":
                jump choice5_a
            "Engga ah.":
                jump choice5_b
        label choice5_a:

        hide citrasmile
        show idlecitrasmile

        p "Oke deh!"
        p "Bentar ya."

        hide idlecitrasmile
        show citrahappy

        c "Iya!"

        hide citrahappy
        show idlecitrahappy

        "Aku mengambilkan buku tersebut."
        "Ternyata buku itu adalah buku novel romance yang akhir-akhir ini terkenal dikalangan remaja."
        "Saat aku memberikan buku tersebut kepada Citra."
        "Dirinya agak malu-malu."

        hide idlecitrahappy
        show citrahappy2 at short_shake, center

        jump choice5_done  

        label choice5_b:

        p "Engga ah."

        hide citrasmile
        show citrairritated at short_shake, center

        c 'Ya ampun... Itu tinggi banget. Ambilin donk.' 

        hide citrairritated
        show idlecitrairritated

        p 'Iya deh iya.'

        "Aku mengambilkan buku tersebut."
        "Ternyata buku itu adalah buku novel romance yang akhir-akhir ini terkenal dikalangan remaja."
        "Saat aku memberikan buku tersebut kepada Citra."
        "Dirinya agak malu-malu."

        hide idlecitrairritated
        show citrahappy2 at short_shake, center

        jump choice5_done
        
        label choice5_done:

        c 'Makasih ya!' 

        hide citrahappy2
        show idlecitrahappy2

        p 'Iya okay...'

        hide idlecitrahappy2
        show citratalk

        c 'Btw... kamu ikut rapat nanti sore ngga?'

        hide citratalk
        show idlecitranormal 

        p 'Mungkin iya sih... Kan itu wajib untuk anggota OSIS.'
        p 'Emang kamu ga mau ikut?'

        hide idlecitranormal
        show citratalk

        c 'Bukan begitu.' 
        c 'Aku hanya bertanya saja.'

        hide citratalk
        show idlecitranormal

        p 'Baiklah... Btw buku yang kamu baca itu lumayan terkenal ya.'

        hide idlecitranormal
        show citrasmile

        c 'Iya sih bener... Aku mau baca dulu ya...'
        p 'Oke deh...'

        hide citrasmile with dissolve
        
        "Citra pergi meninggalkanku untuk mencari tempat duduk yang nyaman."
        "Aku mulai mencari buku untuk dibaca."
        "Aku telah menemukan buku yang ingin kubaca."
        "Buku tersebut ialah novel misteri yang judulnya cukup menarik perhatianku."
        "Dan juga cover buku itu cukup menarik bila diperhatikan."
        "Saat aku ingin mengambil buku tersebut."
        "Ada satu buku aneh yang terjatuh."
        "Buakkkk!!!!"
        "Buku aneh tersebut terjatuh dilantai."
        "Buku itu terjatuh dalam keadaan terbuka dan di dalamnya terdapat secarik kertas."

        python:
            renpy.notify("Mendapatkan Diary 1")
            inventory.add(diary01)

        "Aku mengambil kertas itu."
        "Dan tiba-tiba ada yang memanggil ku."

        c 'Hei...[name].'

        show idlecitranormal with dissolve

        p 'Ada apa Cit?'

        hide idlecitranormal
        show citratalk

        c 'Kamu mau ikut ke kantin ga?'

        hide citratalk
        show idlecitranormal

        p 'Eh...'  

        "Ternyata Citra mengajakku ke kantin."
        "Aku bingung ingin ikut atau tidak."
        "Padahal beberapa waktu lalu aku menolak ajakan Kevin, Zaky, dan Yeri."
        
        hide idlecitranormal
        show citratalk

        c 'Ayo donk ikut...'

        hide citratalk
        show idlecitranormal

        p 'Tapi tuh, beberapa waktu yang lalu aku diajak ke kantin sama Kevin, Zaky, dan Yeri.'
        p 'Tapi aku menolaknya.' 

        hide idlecitranormal
        show citratalk

        c 'Kok gitu? Kenapa kamu menolaknya?'

        hide citratalk
        show idlecitranormal

        p 'Ya... karena aku males buat ikut.'

        hide idlecitranormal
        show citratalk

        c 'Nah... Yok ikut sekalian.'
        c 'Nanti sekalian juga untuk membahas masalah rapat nanti sore.' 

        hide citratalk
        show idlecitranormal

        "Aku kebingungan ingin mengikutinya atau tidak."
        "Ya... mungkin ikut bukan sesuatu yang buruk."

        hide idlecitranormal
        show citratalk

        c 'Gimana?'

        hide citratalk
        show idlecitranormal

        p 'Iya deh iya...'

        hide idlecitranormal
        show citrahappy at short_shake, center

        c 'Nah gitu donk...'

        hide citrahappy with dissolve

        "Aku mengembalikan buku yang kuambil dari ke rak buku."
        "Citra mulai meninggalkan ruangan perpustakaan."
        "Lalu, aku ikut meninggalkan ruangan perpustakaan dan mengikuti Citra."

        #kantin
        scene bg canteen morning with dissolve
        python:
            renpy.notify("Kantin")

        "Sesampainya disana Citra langsung menuju ke tempat pembelian."
        "Disana aku melihat Yeri sedang sendirian."
        "Aku menghampirinya dan menyapanya."

        show idleyerinormal with dissolve

        p "Hai Yeri... Kamu lagi ngapain?"

        hide idleyerinormal
        show yerisurprised at short_shake, center

        y "Eh [name]... Kenapa kamu kesini?"

        hide yerisurprised
        show yerismile at short_shake, center

        y "Katanya ngga mau ikut ke kantin?"
        hide yerismile
        show idleyerismile
        p "Aku ikut Citra tadi." 
        p "Dipaksa sih."
        
        hide idleyerismile 
        show yericheerful at short_shake, center
        
        y "Hahahaha... Dipaksa yaa."
        hide yericheerful
        show idleyericheerful
        p "Ya mau gimana lagi."
        
        hide idleyericheerful with dissolve
        
        "Saat kita berdua sedang mengobrol datang Kevin, Zaky, dan Citra."
        show kevincheerful at left with dissolve:
            xalign 0.0
            yalign 1.0
        
        show idlecitranormal at center with dissolve:
             
        show idlezakynormal at right with dissolve:
            xalign 0.9
            yalign 1.0
        
        k "Hai..."

        hide kevincheerful
        show kevinhappy at short_shake:
            xalign 0.0
            yalign 1.0

        k "Eh... Ada [name], katanya kamu ga mau ikut ke kantin sama kita."
        hide kevinhappy
        show idlekevinhappy at left:
            xalign 0.0
            yalign 1.0
        show zakytalk at right:
            xalign 0.9
            yalign 1.0
        z "Iya... Kenapa tadi ga mau ikut?"
        hide zakytalk
        show idlezakynormal at right:
            xalign 0.9
            yalign 1.0
        show citratalk
        c "Tadi [name] bareng sama aku dari perpustakaan."
        hide citratalk
        hide idlezakynormal
        show zakytalk at right:
            xalign 0.9
            yalign 1.0
        z "Jadi gitu ya."
        hide zakytalk
        show zakyworry at right:
            xalign 0.9
            yalign 1.0
        z "Katanya tadi kamu mau ke kamar mandi."
        hide zakyworry
        show idlezakynormal at right:
            xalign 0.9
            yalign 1.0
        p "Iya tadi aku ke kamar mandi sih."
        p "(Sebenarnya aku berbohong.)"
        hide idlekevinhappy
        show kevinhappy at left:
            xalign 0.0
            yalign 1.0
        k "Begitu ya..."

        hide kevinhappy
        hide idlecitranormal
        hide idlezakynormal
        with dissolve
        
        "Kevin, Citra, dan Zaky mulai duduk di kursi meja kantin yang aku duduki."

        jump promosi

        label promosi:

            show zakytalk at short_shake,center:
                xalign 0.8
                yalign 1.0

            show idlekevinsmile:
                xalign 0.2
                yalign 1.0

            z "Eh Yeri, kamu main apa sih??"

            hide idlekevinsmile
            show kevinsmile:
                xalign 0.2
                yalign 1.0

            hide zakytalk
            show idlezakytalk:
                xalign 0.8
                yalign 1.0

            k "Iyaa kamu main apa sih Yer??"
            k "Kok kayaknya seru banget.."

            hide idlezakytalk
            hide kevinsmile
            with dissolve

            show yericheerful

            y "Ini lo.. game visual novel"

            show yericheerful with move:
                xalign 0.2
                yalign 1.0
            hide yericheerful
            show idleyericheerful:
                xalign 0.2
                yalign 1.0

            show citratalk:
                xalign 0.8
                yalign 1.0

            c "Novel tentang apa? Seru ngga?"

            hide citratalk
            show idlecitratalk:
                xalign 0.8
                yalign 1.0

            hide idleyericheerful
            show yericheerful at long_shake,center:
                xalign 0.2
                yalign 1.0

            y "Seruu bangett.."

            hide yericheerful
            show yeritalk:
                xalign 0.2
                yalign 1.0

            y "Ini tuh game visual novel tentang misteri di sekolah"
            y "Serunya kita bisa memilih rute ending sendiri.. jadi ending dari novel ini itu ada banyak"

            hide yeritalk
            show idleyeritalk:
                xalign 0.2
                yalign 1.0

            hide idlecitratalk
            show kevintalk:
                xalign 0.8
                yalign 1.0

            k "Memang judulnya apa? Sepertinya menarik"

            hide kevintalk
            hide idleyeritalk
            show yeritalk

            y "Judul game nya {b}Cursed Night at School{/b}"
            y "Kalau mau main gamenya, game ini bisa didapatkan secara gratis di web {a=https://cursed-night.netlify.app/} Cursed Night {/a} pada tanggal 24 Desember 2022"

            hide yeritalk with dissolve

            "Terima kasih sudah memainkan versi DEMO game ini"
            "Sampai jumpa lagi setelah game ini resmi di rilis hehehe"

        return

label variabels:
    $ Inventory[0] = Items("Diary", 1, 1, 0, 0)
    
    return 
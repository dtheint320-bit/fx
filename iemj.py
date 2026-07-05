import streamlit as vc
import pandas as xc
import altair as nc

vc.title("Here You Can Download Ai Videos and Images")


uv, rt = vc.tabs(["Download Ai videos, Images and prompts", "Ai Uses Graph"])

with uv:
    gh, df = vc.columns(2)
    with gh:
        
        vc.video("uh.mp4")

        with open("uh.mp4", "rb") as vb:
            vc.download_button(data= vb, 
                               file_name= "Ai-1.mp4", 
                               label= "Download This Video")

    with df:
        vc.video("aq.mp4")

        with open("aq.mp4", "rb") as cd:
            vc.download_button(label= "Download This Video",
                                file_name= "Ai-2.mp4",
                                  data= cd)

    
    df, nm = vc.columns(2)
    with df:
        vc.video("fd.mp4")
        with open("fd.mp4", "rb") as vk:
            vc.download_button(label= "Download",
                                data= vk, 
                                file_name= "Ai-3.mp4")
            
    with nm:
        vc.video("rt.mp4")
        with open("rt.mp4", "rb") as vr:
            vc.download_button(label= "Download",
                                data= vr, 
                                file_name= "Ai-4.mp4")

    re, gc = vc.columns(2)

    vc.write("Photos")

    hj, fd = vc.columns(2)

    with hj:
        vc.image("k.png")
        with open("k.png", "rb") as z:
            vc.download_button(label= "Download this File",
                                data= z, 
                                file_name= "Ai/image1", key= "kjff")
            
    
    with fd:
        vc.image("z1.png")
        with open("z1.png", "rb") as p:
            vc.download_button(label= "Download this File",
                                data= p, 
                                file_name= "Ai/image2", key= "zxs")
    

    mg, bv = vc.columns(2)

    with mg:
        vc.image("vc.png")
        with open("vc.png", "rb") as a:
            vc.download_button(label= "Download this File",
                                data= a, 
                                file_name= "Ai/image1")
    
    with bv:
        vc.image("e.png")
        with open("e.png", "rb") as ws:
            vc.download_button(label= "Download this File",
                                data= ws, 
                                file_name= "Ai/image1", key= "jjyy")
    vc.title("And Prompts too")


    d = vc.multiselect("Choose Your Ai Prompts", ["Photos", "Videos"])
    for g in d:
        if g == "Photos":
            vc.code("Beautiful dark angel with enormous black wings standing in a ruined cathedral, moonlight streaming through broken stained glass, " \
            "gothic atmosphere, ultra detailed feathers"
            " cinematic shadows, photorealistic", language= None)
            vc.code("Powerful pharaoh sitting on a golden throne inside an enormous pyramid," 
            " torches, hieroglyphics, cinematic realism," 
            " ultra detailed", language= None)
            vc.code("Genius inventor inside a giant steampunk laboratory" 
            " filled with gears, clocks, " 
            "steam engines, brass machinery," 
            " cinematic lighting", language= None)
            vc.code("Ancient Japanese shrine during autumn, red maple leaves," 
            " stone lanterns, mist, peaceful atmosphere," 
            " cinematic realism", language= None)
            vc.code("Majestic white wolf standing on frozen cliffs under the northern lights," 
            " ultra realistic wildlife photography")
        if g == "Videos":
            vc.code("The samurai slowly raises the glowing katana while rain falls heavily. Neon signs flicker, steam rises from street vents, holograms animate around him, " \
            "his coat and hair sway naturally in the wind," 
            " the camera slowly pushes forward before orbiting "
            "around him with smoot")

            vc.code("The samurai slowly raises the glowing katana while rain falls heavily. Neon signs flicker, steam rises from street vents, holograms animate around him, " \
            "his coat and hair sway naturally in the wind, " 
            "the camera slowly pushes forward before orbiting" 
            " around him with smoot")
            vc.code("The dragon spreads its wings and launches into the sky. Snow blows across the mountain peaks, clouds move dramatically," 
            " the rider grips the reins while the dragon breathes smoke," 
            " the camera circles around them before diving alongside the dragon during flight.")
            vc.code("Schools of fish swim past, jellyfish pulse with bioluminescent light, mermaids gracefully glide through the palace," 
            " sunlight rays shimmer through the water while the" 
            " camera slowly floats into the grand entrance.")
            vc.code("Holographic interfaces animate around the AI. Robotic arms assemble futuristic devices, " 
            "glowing data streams" 
            " flow through transparent displays," 
            " the AI opens its eyes as the camera" 
            " slowly dollies toward its face.")

with rt:
    fd = xc.DataFrame({"Years": [ 2023, 2024, 2025, 2026],
                       "Most Used Months": ["September", "October", "November", "December"],
                       "Most wastes of 2023": [13.5, 13.8, 13.9, 14.0],
                       "Most wastes of 2024": [20.2, 20.5, 20.8, 21.0],
                       "Most wastes of 2025": [27.3, 27.6, 27.8, 28.0],
                       "Most wastes of 2026": [40.5, 41.0, 41.5, 42.0]})
    
    vh = fd.melt(id_vars= ["Years", "Most Used Months"],
                 value_vars= ["Most wastes of 2023", "Most wastes of 2024", "Most wastes of 2025","Most wastes of 2026"
                 ], var_name= "Year Of Wastes Costs For Ai",
                 value_name= "Costs For Ai")

    
    gc = nc.Chart(vh).mark_line(color= "skyblue").encode(x= nc.X("Years:O", 
                                                 title= "Years"), y= nc.Y("Costs For Ai:Q", title= "Wastes Money For Artifical Intelligent Technology",
                                                                            axis= nc.Axis(labelExpr= "datum.value + 'Billion'")),
                                                                            tooltip= nc.Tooltip("Most Used Months:N",
                                                                                                 title= "Most Used with Months")).properties(
                                                                                width= 350,
                                                                                  height = 400)
    vc.altair_chart(gc, use_container_width= True)
                                                                             
    

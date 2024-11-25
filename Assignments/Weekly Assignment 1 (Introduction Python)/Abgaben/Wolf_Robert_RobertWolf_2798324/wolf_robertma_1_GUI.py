import math
import matplotlib.pyplot as plt #use the library as GUI
from matplotlib.widgets import Slider #Documentation used
#Main Function
def main():
    #bool for Unit toggle
    global meter_bool,ax,slider_width,slider_height,slider_depth
    meter_bool = True

    # Square dimensions
    start_width = 5
    start_depth = 5
    start_height = 3

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))


    # slider to control the height offset
    ax_height = fig.add_axes([0.25, 0.15, 0.65, 0.03])#axis on which the slider is
    slider_height = Slider(
        ax=ax_height,
        label="Height in m",
        valmin=0.0,
        valmax=20,
        valinit=start_height,
        )

    # Slider to control the width
    ax_width = fig.add_axes([0.25, 0.1, 0.65, 0.03])#axis on which the slider is
    slider_width = Slider(
        ax=ax_width,
        label="Width in m",
        valmin=0,
        valmax=20,
        valinit=start_width,
        )

    # Slider to control the depth
    ax_depth = fig.add_axes([0.25, 0.05, 0.65, 0.03])#axis on which the slider is
    slider_depth = Slider(
        ax=ax_depth,
        label="Depth in m",
        valmin=0,
        valmax=20,
        valinit=start_depth,
    )
    ax_button = fig.add_axes([0.75, 0.3, 0.15, 0.07])#axis on which the button is
    unit_swap_button=plt.Button(ax_button,label= "Unit mm/m")
    # Create the initial plot
    update_graph(start_height)
    # Update the plot when the slider values change
    slider_height.on_changed(update_graph)
    slider_width.on_changed(update_graph)  
    slider_depth.on_changed(update_graph)  
    unit_swap_button.on_clicked(unit_swapper)
    # Display the plot
    plt.show()

#Move points so they represent an isometric square (called in update_graph)
def iso_view(x, y):
    dx = (math.sqrt(3) / 2) * x - (math.sqrt(3) / 2) * y #isometric transformation equation
    dy = (1 / 2) * x + (1 / 2) * y
    return dx, dy

# update the graph based on the height offset and square dimensions (called in main)
def update_graph(width_depth_height_change):#takes argument so .onchange method works
    


    ax.cla()  #ClearAll
    # Base Square Dimensions
    global area,volume
    width = slider_width.val
    depth = slider_depth.val
    height = slider_height.val
    square1_vertices = [
        (width/2, depth/2),   #back right Vertex
        (width/2, -depth/2),  #front right Vertex
        (-width/2, -depth/2), #front left Vertex
        (-width/2, depth/2)   #back left Vertex
    ]



    #build string to Show the Results of ARea and Volume

    if meter_bool==True:
        area = round(width*depth,2)
        string1_area = "Area:"
        string2_area = str(area)
        string3_area = "m²"
        combined_string_area = string1_area + string2_area + string3_area



        volume = round(width*depth*height,2)
        string1_volume = "Volume:"
        string2_volume = str(volume)
        string3_volume = "m³"
        combined_string_volume = string1_volume + string2_volume + string3_volume
    else:
        area = int(width*depth*1000*1000)
        string1_area = "Area:"
        string2_area = str(area)
        string3_area = "mm²"
        combined_string_area = string1_area + string2_area + string3_area

        volume = int(width*depth*height*1000*1000*1000)
        string1_volume = "Volume:"
        string2_volume = str(volume)
        string3_volume = "mm³"
        combined_string_volume = string1_volume + string2_volume + string3_volume




    
    
    
    

    # Convert square vertices to isometricly translated coordinates
    isometric_square1 = [iso_view(x, y) for x, y in square1_vertices]
    # Close the shape for plotting by adding the first point to the end
    isometric_square1.append(isometric_square1[0])
    # duplicate
    isometric_square2 = isometric_square1


    # create individual list for x and y coordinates for both squares

    #Square1
    iso_x1_coords = []
    for coord in isometric_square1:
        iso_x1_coords.append(coord[0])
    
    iso_y1_coords = []
    for coord in isometric_square1:
        iso_y1_coords.append(coord[1])


    #Square Two (translated in height)

    iso_x2_coords = []
    for coord in isometric_square2:
        iso_x2_coords.append(coord[0])

    iso_y2_coords = []
    for coord in isometric_square2:
        iso_y2_coords.append(coord[1] + (height)) #add height to y coordinates


 
    

    # Plot the first square
    ax.plot(iso_x1_coords, iso_y1_coords,'black', label= combined_string_area )
    ax.plot(iso_x2_coords, iso_y2_coords, 'black',label=combined_string_volume)

    # Connect corresponding points (same x-coordinates) between the two squares

    for i in range(len(iso_x1_coords)):
        ax.plot([iso_x1_coords[i], iso_x2_coords[i]], [iso_y1_coords[i], iso_y2_coords[i] ], 'black')

    #show dominant direction
    decide_dominant()
    dominant_label = ax.text(
    40, -23,
    str(msg_dominant_dim),
    fontsize=12,
    ha="right"
    )  
    # Draw the new Graph
    plt.draw() 

    ax.set_aspect('equal', adjustable='box')

    #Set limits of axes so graph doesnt resize
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)

    # title 
    ax.set_title('Visualisation of Room')
    ax.legend()
    

    # deactivate tick labels
    ax.set_xticks([])
    ax.set_yticks([])
    # Remove the border (spines) of the plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

#Swap units between m and mm (called in main)
def unit_swapper(clicked):
    global meter_bool
    meter_bool = not meter_bool

    update_graph(slider_depth)#rebuild the whole graph with a random slider as argument


# decide dominant dimension (called in update_graph)
def decide_dominant():
    global msg_dominant_dim
   
    msg_dominant_dim=""
    if slider_height.val > slider_width.val and slider_height.val > slider_depth.val:
        msg_dominant_dim = "The room is higher than it is wide and deep"
    if slider_width.val > slider_height.val and slider_width.val > slider_depth.val:
        msg_dominant_dim = "The room is wider than it is high and deep"
    if slider_depth.val > slider_height.val and slider_depth.val > slider_width.val:
        msg_dominant_dim = "The room is deeper than it is wide and high"

if __name__=="__main__":
    main()
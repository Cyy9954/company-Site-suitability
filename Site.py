#%%
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:25:07 2023

@author: 肉松
"""

import tkinter as tk
import matplotlib
import my_modules.io as io
import my_modules.calculate as cal
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.filedialog import asksaveasfilename 
       

# Define the function to calculate and display the result raster
def calculate_result_raster(save_image=False):
    """
    calculates a weighted sum based on the current weight factor for each raster data and rescales the result to the [0, 255] range.
    The image of the resultant raster data is then displayed in the interface and the resultant raster data is finally saved to a file.
    ----------
    save_image : bool, optional
        A flag indicating whether to save the resulting image to a file. 
        Default is False.
    ----------
    """
    # Multiply each raster by its weight factor
    weighted_geology = cal.multiply_raster(geology_raster, geology_slider.get())
    weighted_transport = cal.multiply_raster(transport_raster, transport_slider.get())
    weighted_population = cal.multiply_raster(population_raster, population_slider.get())
    
    # Add the weighted rasters together
    total_raster = cal.add_rasters(weighted_geology, weighted_transport, weighted_population)
    
    # Rescale the resulting raster to have values in the range [0, 255]
    rescaled_raster = cal.rescale_raster(total_raster, 0, 255)
    # Create an image from the rescaled raster
    
    # Create an image from the rescaled raster
    axs[3].imshow(rescaled_raster)
    axs[3].set_title('Weighted Raster')
    
    # Save the resulting raster to a file if specified
    if save_image:
        save_result_image(rescaled_raster)

            
def update_weights(event=None):
    # Get current values of each slider
    geology_val = geology_weight.get()
    transport_val = transport_weight.get()
    population_val = population_weight.get()

    # Calculate the sum of all slider values
    total = geology_val + transport_val + population_val

    # If the sum is greater than 1, adjust the sliders accordingly
    if total > 1:
        scale_factor = 1 / total
        geology_slider.set(geology_val * scale_factor)
        transport_slider.set(transport_val * scale_factor)
        population_slider.set(population_val * scale_factor)
    
    # Update the total again
    geology_val = geology_weight.get()
    transport_val = transport_weight.get()
    population_val = population_weight.get()
    total = geology_val + transport_val + population_val

    # If the sum is less than 1, adjust the sliders to increase the total to 1
    if total < 1 and total !=0:
        scale_factor = 1 / total
        geology_slider.set(geology_val * scale_factor)
        transport_slider.set(transport_val * scale_factor)
        population_slider.set(population_val * scale_factor)
        
    # Update the total again
    geology_val = geology_weight.get()
    transport_val = transport_weight.get()
    population_val = population_weight.get()
    total = geology_val + transport_val + population_val

    # Update the result raster
    calculate_result_raster()
    canvas.draw()
    

def save_result_image(rescaled_raster):
    """
    Saves a grayscale image and text file of the resulting raster data.
    ----------
    rescaled_raster : 2D numpy array
        Rescale the raster data to the range [0, 255].
    ----------
    """
    # Write the resulting raster to a file
    file1=asksaveasfilename(title='Save txt',initialdir='unnamed.txt',filetypes=[('txt','*.txt')],defaultextension='txt')
    if  file1:
        io.write_raster(file1,rescaled_raster)
    else:
        return

    # Choose the path and filename to save the image
    file2=asksaveasfilename(title='Save As',initialdir='unnamed.jpg',filetypes=[('jpg','*.jpg')],defaultextension='jpg')
   
    # Draw the raster data image and save it
    plt.close()# Close any previously open windows
    plt.imshow(rescaled_raster)
    plt.title('Weighted Raster')
    plt.savefig(file2)

    

# Define the GUI window and widgets
window = tk.Tk()
window.title("Raster Calculator")
window.geometry("1800x1200")

# Read three raster data files
geology_raster = io.read_raster_data("Datas/Geology.txt")
transport_raster = io.read_raster_data("Datas/Transport.txt")
population_raster = io.read_raster_data("Datas/Population.txt")

# Display the image in a label widget
fig,axs = plt.subplots(nrows=1,ncols=4,figsize=(16, 8))
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

axs[0].imshow(geology_raster)
axs[0].set_title('Geology')
axs[1].imshow(transport_raster)
axs[1].set_title('Transport')
axs[2].imshow(population_raster)
axs[2].set_title('Population')
canvas.draw()

# Define the default value of the weighting factor for each raster
geology_weight = tk.DoubleVar(value=0.5)
transport_weight = tk.DoubleVar(value=0.3)
population_weight = tk.DoubleVar(value=0.2)
    

#Use the tk.Scale() function to create three sliders to control the weight factor of each raster data, and call calculate_result_raster() to calculate and display the initial result raster data, and then start the GUI event loop
geology_slider = tk.Scale(window, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Geology Weight", variable=geology_weight, command=lambda event=None:update_weights(), length=400,font=("Helvetica", 15))
transport_slider = tk.Scale(window, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Transport Weight", variable=transport_weight, command=lambda event=None:update_weights(), length=400 , font=("Helvetica", 15))
population_slider = tk.Scale(window, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Population Weight", variable=population_weight, command=lambda event=None:update_weights(), length=400,font=("Helvetica", 15))

# Pack the sliders into the GUI window
geology_slider.pack()
transport_slider.pack()
population_slider.pack()

# Define the save button and add it to the GUI window
a=True
save_button = tk.Button(window, text="Save Image and Text", command  =lambda a=a :calculate_result_raster(True),font=("Helvetica", 18))
save_button.pack(side="right", anchor="nw")


# Call the function to calculate and display the initial result raster
calculate_result_raster()

# Start the GUI event loop
window.mainloop()

# %%

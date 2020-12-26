from discord.ext import commands
from nasapy import Nasa
import numpy as np
from datetime import datetime
import requests
import random


nasa = Nasa(key="insert key here")
# or use nasa = Nasa() for the demo key


client = commands.Bot(command_prefix="/")
#all comands will start with /

@client.command(name="potd")
#establishes a new comand which will be called with /potd
async def version(context):
    # nasa picture of the day

    Date = datetime.today().strftime('%Y-%m-%d')
# gets the curent date

    picture_of_the_day = nasa.picture_of_the_day(Date, hd=True)
# asks the api for all the data

    potd_explanation = picture_of_the_day.get("explanation", "none")
    potd_url = picture_of_the_day.get("url", "none")
# isolates the explanation and url from the data received from the API
    await context.message.channel.send(potd_explanation)
    await context.message.channel.send(potd_url)
# sends the info we got from the API to the user as requested

@client.command(name="mars")
# establishes a new command which will be called with /mars
async def version(context):
    # random image from the mars rover

    sol = np.random.randint(0, 2869) + 1
# generates the random number that is used to pick a mars day(sol)
    rover_cam = nasa.mars_rover(sol=sol)
# asks the API for the data useing the sol date that was randomly picked
    rover_cam_list = (rover_cam[1])
    rover_cam_list_camera = rover_cam_list.get("camera", "none")
    rover_cam_list_rover = rover_cam_list.get("rover", "none")
# isolates data
    mars_image_link = rover_cam_list.get("img_src", "none")
    mars_image_date = rover_cam_list.get("earth_date", "none")
    mars_image_camera = rover_cam_list_camera['full_name']
    mars_rover_name = rover_cam_list_rover['name']
# isolates data some more
    mars_image_message = "This image was taken on " + mars_image_date + \
                         " with the " + mars_image_camera + " on the mars " + mars_rover_name + " rover."
# sets up the message that's going to be sent to the user along with the link
    # mars_image_link
    await context.message.channel.send(mars_image_message)
    await context.message.channel.send(mars_image_link)
# sends the messages with the info as requested

@client.command(name="poster")
# establishes a new comand which will be called with /poster
async def version(context):
    # random poster
    poster_1 = "https://i.imgur.com/75xnLYc.png"
    poster_2 = "https://i.imgur.com/0GNcXJx.png"
    poster_3 = "https://i.imgur.com/YNDyV2m.png"
    poster_4 = "https://i.imgur.com/9zLfiWi.png"
    poster_5 = "https://i.imgur.com/PAEUV8X.png"
    poster_6 = "https://i.imgur.com/uB3kyui.png"
    poster_7 = "https://i.imgur.com/Hjj4UkR.png"
    poster_8 = "https://i.imgur.com/GFX8OJ4.jpg"
    poster_9 = "https://i.imgur.com/CPPzfMl.png"
    poster_10 = "https://i.imgur.com/hYgiCsK.png"
    poster_11 = "https://i.imgur.com/O1xJg1u.png"
    poster_12 = "https://i.imgur.com/cCIYCyS.jpg"
    poster_13 = "https://i.imgur.com/pAgnj3R.png"
    poster_14 = "https://i.imgur.com/mVWpt63.png"
    poster_15 = "https://i.imgur.com/ZSJpTuw.png"
    poster_16 = "https://i.imgur.com/6szcLQ7.png"
# these are a list of all the cool posters credit goes to Courtesy NASA/JPL-Caltech for these
    vars = [poster_1, poster_2, poster_3, poster_4, poster_5,
            poster_6, poster_7, poster_8, poster_9, poster_10,
            poster_11, poster_12, poster_13, poster_14, poster_15,
            poster_16]
    random_poster = random.sample(vars, 1)
# picks a random poster
    # "To get a list of all the posters in high quality go to https://www.jpl.nasa.gov/visions-of-the-future/"
    poster_link = random_poster[0]
    await context.message.channel.send("To download the high quality version of any of these posters do /info ")
    await context.message.channel.send(poster_link)
# sends the poster that was picked and a pre made message

@client.command(name="info")
# establishes a new comand which will be called with /info
async def version(context):
    await context.message.channel.send("There are four comands they are /potd /mars /poster and /info")
    await context.message.channel.send("/potd stands for picture of the day and shows you the NASA picture/video of the day and an explanation")
    await context.message.channel.send("/mars shows a random image from the mars rovers (usally the Curiosity Rover)")
    await context.message.channel.send("/poster shows a random poster from the jpl visions of the Future posters")
    await context.message.channel.send("/info is what you just called it lists all the comands and what they do")
    await context.message.channel.send("Credit: Nasa API, Courtesy NASA/JPL-Caltech")
    await context.message.channel.send("This bot was made for fun and I may or may not add more stuff to it later")
# sends a bunch of pre made messages including all the comands and what they do

client.run("insert token here")

#Objective: Utilize conditional statements to guide program execution 
# based on user input regarding weather conditions.

#Task Description:

#Create a Python script named weather_advice.py. 
# This script will ask the user about the current weather conditions 
# and provide clothing recommendations based on the input. 
# This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

#Instructions:

#Prompt User for Weather Input:

#Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
#Use the prompt: What's the weather like today? (sunny/rainy/cold):.
#weather = ['sunny','rainy','cold']
recommedation = {'sunny':'Wear a t-shirt and sunglasses',
                 'rainy' : "Don't forget your umbrella and a raincoat",
                 'cold' : 'Make sure to wear a warm coat and a scarf'}

#print(recommedation.keys())


weather = (input("What's the weather like today? (sunny/rainy/cold): ")).lower()
#Provide Clothing Recommendations:

if weather in recommedation.keys():
    if weather == 'sunny':
       # print(recommedation.get('sunny'))
       print('Wear a t-shirt and sunglasses.')
    if weather == 'rainy':
        #print(recommedation.get('rainy'))
        print("Don't forget your umbrella and a raincoat.")
    if weather == 'cold' :
        #print (recommedation.get('cold'))
        print("Make sure to wear a warm coat and a scarf.")

else: 
    print("Sorry, I don't have recommendations for this weather.")

#Based on the user’s input, your program will recommend different types of clothing:
#If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
#If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
#If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
#Include an else statement that handles unexpected 
# input by printing: Sorry, I don't have recommendations for this weather.
#Output the Recommendation:

#Print the clothing recommendation based on the weather condition provided by the user.
#Example Interaction:

#What's the weather like today? (sunny/rainy/cold): sunny
#Wear a t-shirt and sunglasses.
#Or, for an unexpected input scenario:

#What's the weather like today? (sunny/rainy/cold): windy
#Sorry, I don't have recommendations for this weather.
#Repo:

#GitHub repository: alx_be_python
#Directory: control-flow
#File: weather_advice.py
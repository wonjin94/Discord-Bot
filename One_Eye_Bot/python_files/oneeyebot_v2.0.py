# One Eye Bot v2.0



import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

# dictionary for Dark World Tree quests
dict_Dark_world_Tree = {
    "elisap": {
        "difficulty" : "Very Easy",
        "name": "Bottom Tier - Eliminate Sap"
    },
    "elipol": {
        "difficulty" : "Very Easy",
        "name": "Bottom Tier - Eliminate Polluted Tree Sap"
    },

    "elidef" : {
        "difficulty" : "Very Easy",
        "name": "Bottom Tier - Eliminate Defiled Tree Sap"
    },

    "colswo" : {
        "difficulty" : "Easy",
        "name": "Middle Tier - Collect Swords"
    },

    "colaxe" : {
      "difficulty" : "Easy",
      "name": "Middle Tier - Collect Axes"
    },

    "eliswo" : {
        "difficulty" : "Easy",
        "name": "Middle Tier - Eliminate the Swordmen"
    },

    "eliaxe" : {
        "difficulty" : " Medium",
        "name": "Middle Tier - Eliminate the Axemen"
    },

    "colshi" : {
        "difficulty" : "Hard",
        "name": "Top Tier - Collect Shields"
    },

    "colfan" : {
        "difficulty" : "Midium",
        "name": "Top Tier - Collect Fangs"
    },

    "elishi" : {
        "difficulty" : "Hard",
        "name": "Top Tier - Eliminate the Shieldbearers"
    },

    "eliwol" : {
        "difficulty" : "Hard",
        "name": "Top Tier - Eliminate the Wolfriders"
    }
}
# dictionary for Heaven quests
dict_haven = {
    "havcrap": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Collection 1',
        "new_name" : "Haven: Collect Red Antenna Piece",
        "map" : "Scrapyard Hill 4"
    },
    "havcrcp": {
        "difficulty" : 'Easy',
        "name" : 'Haven: Collection 2',
        "new_name" : "Haven: Collect Red Chipset Piece",
        "map" : "Scrapyard Entrance"
    },
    
    "havcgcp": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Collection 3',
        "new_name" : "Haven: Collect Green Chipset Piece",
        "map" : "Scrapyard Hill 2"
    },
    
    "havcbcp": {
        "difficulty" : 'Hard',
        "name" : 'Haven: Collection 4',
        "new_name" : "Haven: Collect Blue Chipset Piece",
        "map": "Scrapyard Lot"
    },

    "havdhr": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Patrol 1',
        "new_name" : "Haven: Defeat Hunterizer Red",
        "map" : "Scrapyard Hill 4"
    },
    
    "havdr": {
        "difficulty" : 'Very Easy',
        "name" : 'Haven: Patrol 2',
        "new_name" : "Haven: Defeat Repairoid",
        "map": ""
    },

    "havdoge": {
        "difficulty" : 'Easy',
        "name" : 'Haven: Patrol 3',
        "new_name" : "Haven: Defeat Outer Guard EX",
        "map" : "Black Heaven Entrance -> Black Heaven Deck 3"
    },
    
    "havdige": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Patrol 4',
        "new_name" : "Haven: Defeat Inner Guard EX",
    },
    
    "scrdcr": {
        "difficulty" : 'Easy',
        "name" : 'Scrapyard: Defense 1',
        "new_name" : "Scrapyard: Defeat Chaseroid Red",
        "map" : "Scrapyard Hill 3"
    },
    
    "scrdcb": {
        "difficulty" : 'Medium',
        "name" : 'Scrapyard: Defense 2',
        "new_name" : "Scrapyard: Defeat Chaseroid Blue",
    },
    
    "scrdhb": {
        "difficulty" : 'Medium',
        "name" : 'Scrapyard: Defense 3',
        "new_name" : "Scrapyard: Defeat Hunterizer Blue",
         "map" : "Scrapyard Hill 5"
    },

    "scrdbap" :{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Delivery 1',
        "new_name" : "Scrapyard: Deliver Blue Antenna Piece",
        "map" : "Scrapyard Hill 5"
    },

    "scrdbas":{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Delivery 2',
        "new_name" : "Scrapyard: Deliver Blue Android Scope",
        "map" : "Scrapyard Hill 5"
    },

    "scrr" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Repair',
        "new_name" :'Scrapyard: Repair',
        
    },

    "scrftms" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Liberation 1',
        "new_name" : "Scrapyard: Free the Modded Scaredroid",
        "map" : "Scrapyard Hill 1"
        
    },
    
    "scrftmba" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Liberation 2',
        "new_name" : "Scrapyard: Free the Modded Broken Android",
        "map" : "Scrapyard Hill 2"
    },
    
    "scrftml" :{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Liberation 3',
        "new_name" : "Scrapyard: Free the Modded Laseroid",
        "map" : "Scrapyard Hill 2"
    },

    "skydmb" :{
        "difficulty" : 'Very Hard',
        "name" :'Skyline: Defense 1',
        "new_name" : "Skyline: Defeat Modded Buffroid"
    },
    
    "skydsr" :{
        "difficulty" : 'Very Easy',
        "name" :'Skyline: Defense 2',
        "new_name" : "Skyline: Defeat Salvoroid Red"
        "map" : "Skyline 2"
    },
    
    "skycpp" :{
        "difficulty" : 'Easy',
        "name" :'Skyline: Collection',
        "new_name" : "Skyline: Collect Pipe Piece"
    },
    
    "skyftmd":{ 
        "difficulty" : 'Hard',
        "name" : 'Skyline: Liberation'
        "new_name" : "Skyline: Free the Modded Deliverbot"
    },

    "skyr" :{
        "difficulty" : 'Very Hard',
        "name" :'Skyline: Repair'
        "new_name" : "Skyline: Repair"
    },

    "skydrbs" :{
        "difficulty" : 'Easy',
        "name" :'Skyline: Delivery 1',
        "new_name" : "Skyline: Deliver Red Blid Shell"
        "map" : "Skyline 2"
    },

    "skydpkp" :{
        "difficulty" : 'Hard',
        "name" :'Skyline: Delivery 2',
        "new_name" : "Skyline: Deliver Prison Key Piece"
    },

    "bhddsb" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Haven Deck: Defense 1',
        "new_name" : "Black Haven Deck: Defeat Salvoroid Blue"
    },
    
    "bhddr" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Haven Deck: Defense 2',
        "new_name" : "Black Haven Deck: Defeat Repairoid"
    },
    
    "bhddd" :{
        "difficulty" : 'Easy',
        "name" :'Black Haven Deck: Defense 3',
        "new_name" : "Black Haven Deck: Defeat Demolishizer",
        "map" : "Black Haven Deck 3"
    },

    "bhdcstd" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Deck: Collection',
        "new_name" : "Black Haven Deck: Collect Steel Drill",
        "map" : "Black Haven Deck 3"
    },

    "bhddfs" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Deck: Delivery 1',
        "new_name" : "Black Haven Deck: Deliver Field Siren"
    },
    
    "bhddbbs" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Haven Deck: Delivery 2',
        "new_name" : "Black Haven Deck: Deliver Blue Blind Shell",
        "map" : "Black Haven Deck 1"
    },
    
    "bhidaxd" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Inside: Defense 1',
        "new_name" : "Black Haven Inside: Defeat Alloy Xenoroid DX"
    },
    
    "bhidstxd" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Inside: Defense 2',
        "new_name" : "Black Haven Inside: Defeat Steel Xenoroid DX"
    },

    "bhidscxd" :{
        "difficulty" : 'Hard',
        "name" :'Black Haven Inside: Defense 3',
        "new_name" : "Black Haven Inside: Defeat Scrap Xenoroid DX"
    },
    
    "bhidaxe" :{
        "difficulty" : 'Mediuim',
        "name" :'Black Heaven Inside: Defense 4',
        "new_name" : "Black Haven Inside: Defeat Alloy Xenoroid EX"
    },
    
    "bhidstxe" :{
        "difficulty" : 'Hard',
        "name" :'Black Haven Inside: Defense 5',
        "new_name" : "Black Haven Inside: Defeat Steel Xenoroid EX"
    },
    
    "bhidscxe" :{
        "difficulty" : 'Easy',
        "name" :'Black Haven Inside: Defense 6',
        "new_name" : "Black Haven Inside: Defeat Scrap Xenoroid EX"
    },
    
    "bhidmm" :{
        "difficulty" : 'Very East',
        "name" :'Black Haven Inside: Defense 7',
        "new_name" : "Black Haven Inside: Defeat Modded Megaroid"
    },

    "bhicis" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Collect 1',
        "new_name" : "Black Haven Inside: Collect Internal Siren"
    },
    
    "bhicaip" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Inside: Collect 2',
        "new_name" : "Black Haven Inside: Collect Alloy ID Plate"
    },

    "bhicstip" :{
        "difficulty" : 'Hard',
        "name" :'Black Haven Inside: Collect 3',
        "new_name" : "Black Haven Inside: Collect Steel ID Plate"
    },

    "bhicscip" :{
        "difficulty" : 'Easy',
        "name" :'Black Haven Inside: Collect 4',
        "new_name" : "Black Haven Inside: Collect Scrap ID Plate"
        "map" : "Black Haven Maze 2",

    },

    "bhir" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Haven Inside: Repair',
        "new_name" : "Black Haven Inside: Repair"
        "map" : "Black Haven Maze 7"
    },

    "bhidaxc" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Inside: Delivery 1',
        "new_name" : "Black Haven Inside: Deliver Alloy Xenoroid Chipset",
        "map" : "Black haven Maze 7"
    },
    
    "bhidstxc" :{
        "difficulty" : 'Medium',
        "name" :'Black Haven Inside: Delivery 2',
        "new_name" : "Black Haven Inside: Deliver Steel Xenoroid Chipset"
    },
    
    "bhidscxc" :{
        "difficulty" : 'Hard',
        "name" :'Black Haven Inside: Delivery 3',
        "new_name" : "Black Haven Inside: Deliver Scrap Xenoroid Chipset"
    },
}
# command for Haven quests
@client.command()
async def haven(ctx,*,args):
        names = args.split(" ")
        for name in names:
            if name in dict_haven:
                await ctx.send("{} : {}".format(dict_haven[name]["new_name"],dict_haven[name]["difficulty"]))
            else:
                await ctx.send("{} is invalid name".format(name))


# command for Dark World Tree quests
@client.command()
async def tree(ctx,*,args):
        names = args.split(" ")
        for name in names:
            if name in dict_Dark_world_Tree:
                await ctx.send("{} : {}".format(dict_Dark_world_Tree[name]["name"],dict_Dark_world_Tree[name]["difficulty"]))
            else:
                await ctx.send("{} is invalid name".format(name))

client.run('NzA1MDYzNzc2OTEwNzA0Njcw.XqmRIQ.mA5uBRLH6k6pUEdrFF0OIN0sHwE')
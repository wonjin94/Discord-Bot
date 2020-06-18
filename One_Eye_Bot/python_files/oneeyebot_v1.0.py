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
    "havcol1": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Collection 1'
    },
    "havcol2": {
        "difficulty" : 'Easy',
        "name" : 'Haven: Collection 2'
    },
    
    "havcol3": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Collection 3'
    },
    
    "havcol4": {
        "difficulty" : 'Hard',
        "name" : 'Haven: Collection 4'
    },

    "havpat1": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Patrol 1'
    },
    
    "havpat2": {
        "difficulty" : 'Very Easy',
        "name" : 'Haven: Patrol 2'
    },

    "havpat3": {
        "difficulty" : 'Easy',
        "name" : 'Haven: Patrol 3'
    },
    
    "havpat4": {
        "difficulty" : 'Medium',
        "name" : 'Haven: Patrol 4'
    },
    
    "scrdef1": {
        "difficulty" : 'Easy',
        "name" : 'Scrapyard: Defense 1'
    },
    
    "scrdef2": {
        "difficulty" : 'Medium',
        "name" : 'Scrapyard: Defense 2'
    },
    
    "scrdef3": {
        "difficulty" : 'Medium',
        "name" : 'Scrapyard: Defense 3'
    },

    "scrdel1" :{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Delivery 1'
    },

    "scrdel2":{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Delivery 2'
    },

    "scrrep" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Repair'
    },

    "scrlib1" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Liberation 1'
    },
    
    "scrlib2" :{
        "difficulty" : 'Easy',
        "name" :'Scrapyard: Liberation 2'
    },
    
    "scrlib3" :{
        "difficulty" : 'Medium',
        "name" :'Scrapyard: Liberation 3'
    },

    "skydef1" :{
        "difficulty" : 'Very Hard',
        "name" :'Skyline: Defense 1'
    },
    
    "skydef2" :{
        "difficulty" : 'Very Easy',
        "name" :'Skyline: Defense 2'
    },
    
    "skycol" :{
        "difficulty" : 'Easy',
        "name" :'Skyline: Collection'
    },
    
    "skylib":{ 
        "difficulty" : 'Hard',
        "name" : 'Skyline: Liberation'
    },

    "skyrep" :{
        "difficulty" : 'Very Hard',
        "name" :'Skyline: Repair'
    },

    "skydel1" :{
        "difficulty" : 'Easy',
        "name" :'Skyline: Delivery 1'
    },

    "skydel2" :{
        "difficulty" : 'Hard',
        "name" :'Skyline: Delivery 2'
    },

    "bhddef1" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Heaven Deck: Defense 1'
    },
    
    "bhddef2" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Heaven Deck: Defense 2'
    },
    
    "bhddef3" :{
        "difficulty" : 'Easy',
        "name" :'Black Heaven Deck: Defense 3'
    },

    "bhdcol" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Deck: Collection'
    },

    "bhddel1" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Deck: Delivery 1'
    },
    
    "bhddel2" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Heaven Deck: Delivery 2'
    },
    
    "bhidef1" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Defense 1'
    },
    
    "bhidef2" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Defense 2'
    },

    "bhidef3" :{
        "difficulty" : 'Hard',
        "name" :'Black Heaven Inside: Defense 3'
    },
    
    "bhidef4" :{
        "difficulty" : 'Mediuim',
        "name" :'Black Heaven Inside: Defense 4'
    },
    
    "bhidef5" :{
        "difficulty" : 'Hard',
        "name" :'Black Heaven Inside: Defense 5'
    },
    
    "bhidef6" :{
        "difficulty" : 'Easy',
        "name" :'Black Heaven Inside: Defense 6'
    },
    
    "bhidef7" :{
        "difficulty" : 'Very East',
        "name" :'Black Heaven Inside: Defense 7'
    },

    "bhicol1" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Collect 1'
    },
    
    "bhicol2" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Collect 2'
    },

    "bhicol3" :{
        "difficulty" : 'Hard',
        "name" :'Black Heaven Inside: Collect 3'
    },

    "bhicol4" :{
        "difficulty" : 'Easy',
        "name" :'Black Heaven Inside: Collect 4'
    },

    "bhirep" :{
        "difficulty" : 'Very Easy',
        "name" :'Black Heaven Inside: Repair'
    },

    "bhidel1" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Delivery 1'
    },
    
    "bhidel2" :{
        "difficulty" : 'Medium',
        "name" :'Black Heaven Inside: Delivery 2'
    },
    
    "bhidel3" :{
        "difficulty" : 'Hard',
        "name" :'Black Heaven Inside: Delivery 31'
    },
}
# command for Haven quests
@client.command()
async def heaven(ctx,*,args):
        names = args.split(" ")
        for name in names:
            if name in dict_haven:
                await ctx.send("{} : {}".format(dict_haven[name]["name"],dict_haven[name]["difficulty"]))
            else:
                await ctx.send("{} is invalid name".format(name))


# command for Haven quests
@client.command()
async def tree(ctx,*,args):
        names = args.split(" ")
        for name in names:
            if name in dict_Dark_world_Tree:
                await ctx.send("{} : {}".format(dict_Dark_world_Tree[name]["name"],dict_Dark_world_Tree[name]["difficulty"]))
            else:
                await ctx.send("{} is invalid name".format(name))

client.run('NzA1MDYzNzc2OTEwNzA0Njcw.XqmRIQ.mA5uBRLH6k6pUEdrFF0OIN0sHwE')

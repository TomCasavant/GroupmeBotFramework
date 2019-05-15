# Groupme Bot Framework (With plugins)
The goal of this project is to create a easily modifiable groupme bot using a (very) simple plugin system.

The intention is for these bots to be hosted in a heroku instance

## Setup
1. Clone this repository locally
2. Use heroku to set the GROUPME_BOT_NAME and GROUPME_BOT_ID. You can get these from [here](https://dev.groupme.com/bots).
3. Clone any plugins you want into the 'plugins/' directory
4. Push the project to heroku

## Building your own plugins
- Every plugin contains at least 2 files. The main plugin file and an info file. An example plugin is available in this repository under plugins/ExamplePlugin

#### Main Plugin File
- The main plugin file must import IPlugin from yapsy.IPlugin
- Then the plugin must have a class that implements IPlugin
- Finally, the plugin must include a process(data) function that takes input from the Groupme API. In process(data) the plugin will return the message that will be sent from the bot.

#### Plugin Info file
- This file will be saved as PluginName.yapsy-plugin where 'PluginName' is the name of your plugin. It has this format:

~~~~
[Core]
Name = The name of your plugin
Module = The name of the class that implements IPlugin

[Documentation]
Author = Your name
Version = Version Number
Website = Optional info about the author
Description = A brief description of your plugin
~~~~


# TODO
- Add ability to use other Groupme API methods

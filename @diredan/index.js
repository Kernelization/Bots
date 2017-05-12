/*
 * importing discord.js module, creating client object,
 * and getting config file :D
 */
const Discord = require("discord.js");
const Client = new Discord.Client();
const Config = require("./config.json");

// run our event loader :)
require("./eventloader/loader.js").run(Client);

// log into the bot
Client.login(Config.token);


/*
 * importing discord.js module, creating client object,
 * and getting config file :D
 */
const Discord = require("discord.js");
const Client = new Discord.Client();

// run our event loader :)
require("./eventloader/loader.js").run(Client);

const fs = require("fs");
var Config = require("./config.json");
if (Config.token === "INSERT_TOKEN" || Config.prefix === "INSERT_PREFIX" ||
    Config.owner === "INSERT_YOUR_USER_ID") {
  let readline = require("readline");
  let rl = readline.createInterface({input: process.stdin, output: process.stdout });
  rl.question("Enter bot token: ", token => {
    rl.question("Enter bot prefix: ", prefix => {
      rl.question("Enter your user id: ", userid => {
        Config.token = token;
        Config.prefix = prefix;
        Config.owner = userid;
        fs.writeFile("./config.json", JSON.stringify(Config, null, 2), () => {
          // log into the bot
          Client.login(Config.token);
        });
      });
    });
  })
} else {
  // log into the bot
  Client.login(Config.token);
}

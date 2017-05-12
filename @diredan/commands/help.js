const Discord = require("discord.js");
const fs = require("fs");
const Config = require("../config.json");

module.exports = {
  /*
   * really bad code but meh it works xD
   */
  run : (args, Client, msg) => {
      if (args[0]) {
        try {
          const command_file = require("./" + args[0]);
          const usage = command_file.usage();
          const description = command_file.description();
          var embed = new Discord.RichEmbed();
          embed.setColor(0xff00ff)
          embed.setTitle("COMMAND: " + args[0]);
          embed.addField("Usage:", Config.prefix + usage);
          embed.addField("Description:", description);
          msg.channel.send("", { embed: embed });
        } catch (err) {
          msg.channel.send("```Command: \"" + args[0] + "\" does not exist!```");
        }
      } else {
        var message = "```\nCommands:\n";
        fs.readdir("./commands/", (err, files) => {
          files.forEach(file => {
            message += file.replace(".js", "") + ", ";
          });
          message += "\n```";
          msg.channel.send(message);
        });
      }
  },
  usage : () => {
    return "help <command>";
  },
  description : () => {
    return "Used for getting help with commands.";
  }
}

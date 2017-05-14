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
          message = "```\nCommand: " + args[0] + "\n\n";
          message += "Usage: " + Config.prefix + usage;
          message += "\n";
          message += "Description: " + description;
          message += "```";
          msg.channel.send(message);
        } catch (err) {
          msg.channel.send("```Command: \"" + args[0] + "\" does not exist!```");
        }
      } else {
        var message = "```\nCommands:\n";
        fs.readdir("./commands/", (err, files) => {
          files.forEach(file => {
            message += file.replace(".js", "") + " ->:<- " + require("./" + file).description() + "\n";
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

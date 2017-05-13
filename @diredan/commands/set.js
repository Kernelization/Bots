const Config = require("../config.json");
const fs = require("fs");

module.exports = {
  /*
   * TODO: make it so users can be added to a whitelist not just 1 in the config.json
   */
  run : (args, Client, msg) => {
    if (args[0] === "game") {
      if (msg.author.id === Config.owner) {
        args.shift();
        if (args[0]) {
          Client.user.setGame(args.join(" "));
        } else {
          Client.user.setGame(null);
        }
        msg.reply("Game updated!");
      }
    }
    else if (args[0] === "avatar") {
      if (msg.author.id === Config.owner) {
        args.shift();
        if (args[0]) {
          Client.user.setAvatar(args[0]);
          msg.reply("Avatar updated!");
        }
      }
    }
    else if (args[0] === "prefix") {
      if (msg.author.id === Config.owner) {
        args.shift();
        if (args[0]) {
          var temp_config = require("../config.json");
          temp_config.prefix = args[0];
          fs.writeFileSync("./config.json", JSON.stringify(temp_config, null, 2), () => {
            msg.reply("Prefix updated!");
          });
        }
      }
    }
    else {
      msg.channel.reply("Invalid arguments!");
    }
  },
  usage : () => {
    return "set <game/avatar/prefix> <arguments>";
  },
  description : () => {
    return "Used for setting different bot information.";
  }
}

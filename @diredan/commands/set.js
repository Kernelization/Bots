const Config = require("../config.json");

module.exports = {
  /*
   * TODO: make it so users can be added to a whitelist not just 1 in the config.json
   */
  run : (args, Client, msg) => {
    if (!args[0]) {
      msg.channel.send("```\nCommands:\n\n" +
                      "<prefix>set game <game> -> used for setting bots game\n```");
    }
    else if (args[0] === "game") {
      if (msg.author.id === Config.owner) {
        args.shift();
        if (args[0]) {
          Client.user.setGame(args.join(" "));
        } else {
          Client.user.setGame(null);
        }
      }
    }
  },
  usage : () => {
    return "<prefix>set <game> <arguments>";
  },
  description : () => {
    return "Used for setting different bot information.";
  }
}

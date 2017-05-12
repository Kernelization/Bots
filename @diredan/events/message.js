const Config = require("../config.json");

module.exports = {
  run : (msg, Client) => {
    /*
     * if the author is a bot or the message doesnt start with the prefix
     * then return as we don't want any spam or errors thrown due to prefix
     * issues...
     */
    if (msg.author.bot || !msg.content.startsWith(Config.prefix)) return;

    /*
     * assigned cmd equal to whats after the prefix so for example
     * "<prefix>help example" it would be "help"
     * assigned args equal to an array/list of all arguments added
     * "<prefix>help arg1 arg2 arg3" it would be [arg1, arg2, arg3]
     */
    let cmd = msg.content.split(" ")[0].substr(Config.prefix.length);
    let args = msg.content.split(" ").slice(1);

    /*
     * try and run the default code from a command file
     * so if user entered "<prefix>help" it would find the file
     * located "../commands/help.js" and run the function "run"
     * from module exports, with the arguments, client and messsage
     * as arguments, an error will occur if the command/file doesn't
     * exist so thats why the try and catch is ran
     */
    try {
      require("../commands/" + cmd).run(args, Client, msg);
    } catch(err) {
      // console.log(err);
    }
  }
}

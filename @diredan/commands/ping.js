module.exports = {
  /*
   * classic old ping command!
   */
  run : (args, Client, msg) => {
    msg.reply("Pong!");
  },
  usage : () => {
    return "<prefix>ping";
  },
  description : () => {
    return "Pong!";
  }
}

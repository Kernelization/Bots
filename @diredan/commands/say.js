module.exports = {
  /*
   * A simple command for making the bot say
   * any message you want it to
   */
  run : (args, Client, msg) => {
    msg.channel.send(args.join(" "));
  },
  usage : () => {
    return "say <text>";
  },
  description : () => {
    return "Used to make the bot say text.";
  }
}

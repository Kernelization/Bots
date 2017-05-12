module.exports = {
  /*
   * used for reloading command files so we dont
   * have to restart the bot to have the effects take
   * place
   */
  run : (args, Client, msg) => {
    if (args[0]) {
      try {
        delete require.cache[require.resolve("./" + args[0] + ".js")];
        msg.channel.send("```Reloaded command " + args[0] + " with success!```");
      } catch (err) {
        msg.channel.send("```Error reloading command " + args[0] + "...```");
      }
    }
  },
  usage : () => {
    return "reload <command>";
  },
  description : () => {
    return "Used for reloading commands so the bot doesn't need restarting.";
  }
}

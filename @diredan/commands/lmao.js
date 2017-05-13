module.exports = {
  /*
   * just to send lmao in chat
   */
  run : (args, Client, msg) => {
    msg.delete();
    msg.channel.send(":regional_indicator_l: :regional_indicator_m: :regional_indicator_a: :regional_indicator_o: :joy: :joy:");
  },
  usage : () => {
    return "lmao";
  },
  description : () => {
    return "Used to make the bot say lmao.";
  }
}

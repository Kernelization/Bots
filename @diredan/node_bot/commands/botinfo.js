const Discord = require("discord.js");

module.exports = {
  /*
   * a basic command for sending information about
   * the bot into a text channel
   */
  run : (args, Client, msg) => {
    var embed = new Discord.RichEmbed();
    embed.setColor(0xff00ff);
    embed.setAuthor(Client.user.username, Client.user.displayAvatarURL, "https://github.com/Kernelization/Bots/tree/master/%40diredan");
    embed.setThumbnail(Client.user.displayAvatarURL);
    embed.addField("Server Count", Client.guilds.size, true);
    var text_channels = 0, voice_channels = 0;
    Client.channels.array().forEach(channel => {
      if (channel.type == 'text') {
        text_channels += 1;
      } else if (channel.type == 'voice') {
        voice_channels += 1;
      }
    });
    embed.addField("Text channels", text_channels, true);
    embed.addField("Voice Channels", voice_channels, true);
    embed.addField("Creator", "<@229708305570856960>", true);
    msg.channel.send("", {embed: embed});
  },
  usage : () => {
    return "botinfo";
  },
  description : () => {
    return "Used to get info about the bot.";
  }
}

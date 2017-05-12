// just a small little function to make life a bit easier
function load_event(event) {
  return require("../events/" + event);
}

module.exports = {
  run : Client => {
    // just discord events, loading their functions from their specified files
    Client.on("message", msg => { load_event("message").run(msg, Client); });
    Client.on("ready", () => { load_event("ready").run(); });
    Client.on("disconnect", () => { load_event("disconnect").run(); });
    Client.on("reconnecting", () => { load_event("reconnecting").run(); });
  }
}

# Status-Stalker
 A discord bot that check the status of minecraft servers and send them in a discord channel.

 # How to make it a bot ?

 # Create an app with the Discord developer portal:
 - Go to the "bot" section and reset the token so you'll have one.
 - toggle on the public bot, presence intents, server members intents, message content intents ( I think just message contents intents will work but not sure )
 - go to the OAuth2 section, in OAuth2 URL Generator, toggle bot, then in bot permission toggle send messages
 - pick the url that was generate and copy-paste it in the browser to add the bot in your server.

 # some changes in the scripts:
 - Change "TOKEN" by the token of the bot
 - change "Channel id" by the channel id where you want your bot to send messages
 - change the servers name and their ip in the "servers" var.

 Then run it, it will work fine !


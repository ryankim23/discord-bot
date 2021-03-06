import discord

from bot.utils.logger import error, info


class TextChannelTemplate:
    name: str
    id: int

    def __init__(self, name: str, _id: int):
        self.name = name
        self.id = _id

    def find(self, client) -> discord.TextChannel:
        from bot.bot_client import CPUBotClient

        client: CPUBotClient

        for channel in client.guild.channels:
            if isinstance(channel, discord.TextChannel):
                if self.id == channel.id:
                    info(
                        f"Text channel with id {self.id} has been found",
                        header=f"[{self.name}]",
                    )
                    return channel

        error(f"Text channel with id {self.id} not found", header=f"[{self.name}]")


new_members = TextChannelTemplate("new-members", 480366530404548608)


async def setup_guild_channels(client):
    from bot.bot_client import CPUBotClient

    client: CPUBotClient

    client.new_members_channel = new_members.find(client)

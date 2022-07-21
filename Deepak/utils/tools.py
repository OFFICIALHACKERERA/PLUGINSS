from telethon.tl import functions
from telethon.tl.types import ChatAdminRights


async def create_supergroup(group_name, client, botusername, descript):
    admin_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        result = await client(
            functions.channels.CreateChannelRequest(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_id = result.chats[0].id
        result = await client(
            functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            )
        )
        await client(
            functions.channels.InviteToChannelRequest(
                channel=created_chat_id,
                users=[botusername],
            )
        )
        await client(
            functions.channels.EditAdminRequest(
                created_chat_id, botusername, admin_rights, "Assistant"
            )
        )
    except Exception as e:
        return "error", str(e)
    if not str(created_chat_id).startswith("-100"):
        created_chat_id = int(f"-100{str(created_chat_id)}")
    return result, created_chat_id

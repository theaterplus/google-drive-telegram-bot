class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize', 'link']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke', 'unlink']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash', 'clearbin']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**• G-Drive Uploader**\nI can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.\n\nI have many more features too... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
        
        f"**• Authenticating Google Drive**\nSend the /{BotCommands.Authorize[0]} commmand and follow the instructions. Use /{BotCommands.Revoke[0]} to revoke your Google Drive Account.",
        
        f"**• Direct Links**\nSend me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.\n\n**Format:**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```.\n\n• Telegram Files**\nTo Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account.\n**Note:** Telegram Files Downloading is slow. it may take longer for big files.",
        
        f"**• Custom Folder for Upload**\nWant to upload in custom folder or in **TeamDrive** ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder. All the files are uploaded in the custom folder you provide.",
        
        f"**• Delete Google Drive Files**\nUse /{BotCommands.Delete[1]} (File/Folder URL) to delete it.\n\n**• Clear Google Drive Bin**\nUse /{BotCommands.EmptyTrash[1]} to clear it.\n**Note**: Files are deleted permanently. This process cannot be undone.\n\n**• Copy Google Drive Files/Folders**\nUse /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.",
        
        "**⬇️ Please follow this Rules ⬇️**\n1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n\n2. Send One request at a time unless bot will stop all processes.\n\n3. Don't send slow links @transload it first.\n\n4. Don't misuse, overload or abuse this free service.",
        
        # Dont remove this ↓ if you respect developer.
        "**Hosted & Maintained By @Neil_Projects**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "⚠️ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "⚠️ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "⚠️ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"⚠️ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Google Drive account Successfully Authorized.**'
    
    INVALID_AUTH_CODE = '⚠️ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "**To Authorize your Google Drive account visit this [LINK]({}) and send the generated code here.**\n\n**Process** : Visit the Link > Allow permissions > you will get a code > copy the code > Paste & send it here"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Google Drive Account Revoked Successfully.**\nSend /{BotCommands.Authorize[0]} command to authenticate again."
    
    NOT_FOLDER_LINK = "⚠️ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**⚠️ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "⚠️ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "🛑 **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️**Bin Cleared Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"

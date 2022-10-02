
#boot file
from source.boot import *

#fun_commands
from source.fun_commands.chappal_code import *
from source.fun_commands.thusky import *
from source.fun_commands.yo_introduction import *
from source.fun_commands.shoot import *
##jokes disabled
from source.fun_commands.dance import *
#spam_dm disabled
from source.fun_commands.hack import *

#welcome
from source.misc.welcome import *     #server  
from source.misc.welcoming import *   #on_message


#dm_messages
from source.misc.dm_messages import *
from source.misc.give_roles import *
##ping_pong disabled

#administration_commands
from source.administration_commands.clear_messages import *
from source.administration_commands.dm import *
from source.administration_commands.kick import *
from source.administration_commands.ban import *
from source.administration_commands.unban import *
from source.administration_commands.channel_msg_send import *
from source.administration_commands.show_mod_commands import *
from source.administration_commands.reply import *

#utilites
#from source.utilities.roles import *
from source.utilities.wolfram import *
from source.utilities.message_edit import *
from source.utilities.avatar import *


#voice
from source.voice_commands.voice import *
from source.voice_commands.yt_play import *
from source.voice_commands.music import *
#from source.voice_commands.music_menu import *
from source.voice_commands.text_to_speech import *

#tests
from source.tests.image import *
from source.tests.friend_request import *
from source.tests.search_on_message import *

run()
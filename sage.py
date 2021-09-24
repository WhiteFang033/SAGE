
#boot file
from source.boot import *

#test_command
from source.ping import *
from source.administration_commands.ping import *

#fun_commands
from source.fun_commands.chappal_code import *
from source.fun_commands.thusky import *
from source.fun_commands.yo_introduction import *
from source.fun_commands.shoot import *
 ##jokes disabled
from source.fun_commands.dance import *

#welcome
from source.welcome import *     #server  
from source.welcoming import *   #on_message


#dm_messages
from source.dm_messages import *

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
from source.utilities.roles import *


#voice
from source.voice_commands.voice import *
from source.voice_commands.music_menu import *
from source.voice_commands.music import *

run()
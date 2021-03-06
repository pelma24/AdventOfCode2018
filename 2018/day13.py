input = """            /--------------------------------------------------------\\                           /------------------------------------------------\\   
            |             /------------------------------------------+---------------------------+--------------------------\\                     |   
            |             |                             /------------+---------------------------+----------\\    /--------\\ |                     |   
            |             |   /-------------------------+---\\        |                           |          |    |        | |                     |   
            |             |   |                         |   |        |            /--------------+----------+----+--------+-+---------------------+-\\ 
 /----------+-------\\     |   |                         |   |        |     /------+--------------+----------+----+----\\   | |                     | | 
 |          |       |     |   |                         | /-+--------+-----+------+--------------+----------+----+----+---+-+----\\                | | 
 |  /-------+-------+-----+-\\ |                         | | |        |     |      |              |          |    |    |   | |    |                | | 
 |  |      /+-------+-----+-+-+\\     /------------------+-+-+--------+-----+-----\\|              |          |    |    |   | |    |                | | 
 | /+------++-\\     |     | | ||     |                /-+-+-+--------+-----+-----++------\\       |          |    |    |   | |    |                | | 
 | ||      || |     |     |/+-++-----+----------------+-+-+-+--------+-----+-----++------+----\\  \\----------+----+----+---+-+----+----------------/ | 
 | ||      || |     |    /+++-++-----+----------------+-+-+-+--------+-----+----\\||      |    |             |    |    |   | |    |                  | 
 | ||      || |     |    |||| ||   /-+----------------+-+-+-+--------+-----+----+++------+----+-------------+----+----+---+-+----+-------\\          | 
 | ||      || |     |    |||| ||/--+-+----------------+-+-+-+--------+-----+----+++------+->--+-------------+----+--\\ |   | |    |       |          | 
 | ||      || |     |  /-++++-+++--+-+----------------+-+-+\\|        |     \\----+++------+----+-------------+----+--+-/   | |    |       |          | 
 | ||     /++-+-----+--+-++++-+++--+-+----------------+-+-+++--------+----------+++------+----+-----\\       |    |  |     | |    |       |          | 
 | ||     ||| |     |  | |||| |||  | |                | | |||        |          |||    /-+----+-----+-------+----+--+-----+-+----+-----\\ |          | 
 | ||     ||| |     |  | |||| |||/-+-+----------------+-+-+++--------+----------+++--\\ | |    |     |       |    \\--+-----/ |    |     | |          | 
 | ||     ||| |     |/-+-++++-++++-+-+----------------+-+-+++--------+----------+++--+-+-+----+-----+-------+-------+\\      |    |     | |          | 
 | ||     ||| |     || | |||| |||| | |               /+-+-+++--------+----------+++-\\| | |    |     |       |       ||      |    |     | |          | 
 | ||     ||| |/----++-+-++++-++++-+-+------\\     /--++-+-+++------<-+----------+++-++-+-+----+-----+-------+-------++-----\\|    |     | |          | 
 | ||     |\\+-++----++-+-++++-+/|| | |      |     |  || | |||/-------+-------\\  ||| || | | /--+-----+-------+-------++-----++----+-----+-+---\\      | 
 | |\\-----+-+-++----++-+-+++/ | || | |      |    /+--++-+-++++-------+-------+--+++-++-+-+-+--+-----+-------+-----\\ ||     ||    |     | |   |      | 
 | |      | | ||    || | |||  | || | |    /-+----++--++-+-++++------\\|       |  ||| || | |/+--+-----+---\\   |     | ||     ||    |     | |   |      | 
 | |      | | ||    || \\-+++--+-++-+-+----+-+----++--++-+-+/||      ||       |  ||| || | |||  |     |   | /-+-----+-++---\\ ||    |     | |   |      | 
 | |      | | ||  /-++---+++--+-++-+-+-\\  | |    ||  || | | ||      ||/------+--+++-++-+-+++--+-----+---+-+-+-----+-++---+-++----+--\\  | |   |      | 
 | |      | | ||  | ||   |||  | || | | |  | |    || /++-+-+-++------+++------+--+++-++-+-+++--+-----+---+-+-+--\\  | ||   | ||    |  |  | |   |      | 
 | |      | |/++--+-++---+++\\ | || | | | /+-+----++-+++-+-+-++------+++------+--+++-++-+-+++--+-----+---+-+-+--+--+-++---+-++----+--+--+-+---+-----\\| 
 | |      | ||||  | ||   |||| | || | | | || |    ||/+++-+-+-++------+++------+--+++-++-+-+++--+-----+---+-+-+--+--+\\||   | ||    |  |  | |   |     || 
 | |      | ||||  | ||   |||| | || | | | || |    |\\++++-+-+-++------+++------+--+++-++-+-+++--+-----+---+-+-+--+--++++---+-/|    |  |  | |   |     || 
 | |      | ||||  | ||   |||| | || | | | || |    | |||| | | ||      |||    /-+--+++-++-+-+++--+-----+---+-+-+--+--++++--\\|  |    |  |  | |   |     v| 
 | |      | ||||  | ||   |||| | \\+-+-+-+-++-+----+-++++-+-+-++------+++----+-+--+++-++-+-+++--+-----+---+-+-+--+--++/|  ||  |    |  | /+-+---+--\\  || 
 | |      | ||||  | ||   |||| | /+-+-+-+-++-+----+-++++-+-+-++------+++----+-+--+++-++-+-+++--+-----+---+-+-+--+--++-+--++--+----+--+-++-+-\\ |  |  || 
 | |      | ||||  | ||   |||| | || | | | || |    |/++++-+-+-++------+++----+-+--+++-++-+-+++--+-----+---+-+-+--+--++-+\\ ||  |    |  | || | | |  |  || 
 | |      | ||||  | ||   |||| | || | | | || | /--++++++-+-+-++------+++----+\\|  ||| || | |||  |  /--+---+-+-+--+--++-++-++--+----+--+-++\\| | |  |  || 
 | |    /-+-++++--+-++---++++-+-++-+-+-+-++-+-+--++++++-+-+-++------+++----+++-\\||| || | |||  |  |  |   | | |  |  || || ||  |    |  | |||| | |  |  || 
 | |    | | ||||  | ||   |||| | || | | | || | |  |||||| | | ||      |||    |||/++++-++-+-+++--+--+--+---+-+-+--+--++-++-++--+\\   |  | |||| | |  |  || 
 | |    | | ||||  | ||   |||| | || | | ^ || | |  |||||| | | ||      |||/---++++++++-++-+-+++--+--+--+---+-+-+--+--++-++-++--++\\  |  | |||| | |  |  || 
 | \\----+-+-++/|  | ||   |||| | || | | | || | |  |||||| | | ||      ||||   |||||||| || | ||| /+--+--+-\\ | | |  |  || || ||  |||  |  | |||| | |  |  || 
 |      | | || |  |/++---++++-+-++-+-+-+-++-+-+--++++++-+-+-++------++++---++++++++-++-+-+++-++-\\|  | | | | |  |  || || ||  |||  |  | |||| | |  |  || 
 |      | | || |  ||||   |||| | || | | |/++-+-+--++++++-+-+-++------++++---++++++++-++-+-+++-++-++--+-+-+-+-+-\\|  || || ||  |||  |  | |||| | |  |  || 
 |      | | || |  ||||   |||| | \\+-+-+-++++-+-+--++++++-+-+-++------++++---++++++++-++-+-+++-++-++--+-+-+-+-+-++--++-++-++--+++--+--+-++++-/ |  |  || 
 |      | | || |  ||||   |||| |  | | | |||| | |  |||||| | | ||/-----++++---++++++++-++-+-+++-++-++\\ | | | | | ||  || || ||  |||  |  | ||||   |  |  || 
 |      | | || |  |||\\---++++-+--+-+-+-++++-+-+--++++++-+-+-+++-----++++---++++++++-++-+-+++-++-+++-+-+-+-+-+-++--++-/| ||  |||  |  | |^||   |  |  || 
 |      | | || |  |||  /-++++-+--+-+-+-++++-+-+--++++++-+-+-+++-----++++---++++++++-++\\| ||| || ||| | | | | | ||  ||  | ||  ||| /+--+-++++---+--+\\ || 
 |      | | || |  |||  | |||| |  | |/+-++++-+-+--++++++-+-+-+++-----++++---++++++++-++++-+++\\|| ||| | | | | | ||  ||  | ||  ||| ||  | ||||   |  || || 
 |      | | || |  |||  | |||| |  | ||| |||\\-+-+--++++++-+-+-+++-----/|||   |||||||| |||| |||||| ||| | | | | | ||  ||  | ||  ||| ||  | ||||   |  || || 
 |      | | \\+-+--+++--+-++++-+--+-+++-+++--+-+--++++++-+-+-+++------/||   |||||||| |||| |||||| ||| | | | | | ||  ||  | ||  ||| ||  | ||||   |  || || 
 |      | |  | |  |||  |/++++-+--+-+++-+++--+-+--++++++-+-+-+++-------++---++++++++-++++-++++++-+++-+-+-+-+\\| ||  ||  | ||  ||| ||  | ||||   |  || || 
 |      | |  | |  \\++--++++++-+--+-+++-/||  | |  |||||| | | |||  /----++---++++++++-++++-++++++-+++-+-+-+-+++-++--++--+-++--+++\\||  | ||||   |  || || 
 |      | |  | |   ||  |||||| |  \\-+++--++--+-+--++++++-+-+-+++--+----++---++++++++-+/|| |||||| ||| | | | \\++-++--++--+-+/  ||||||  | ||||   |  || || 
 |      | |  | |   ||  |||||| |    |||  ||  | |  |||||| | | |||  |    ||   |||||||| | || |||||| ||| | | |  || ||  ||  | |   ||||||  | ||||   |  || || 
 |      | |  | |   ||  |||||| |    |||  ||  | |  ||||||/+-+-+++--+----++---++++++++-+-++-++++++-+++-+-+-+--++-++--++--+-+-\\ ||||||  | ||||   |  || || 
 |      | |  | |   ||  |||||| |    |||  ||  | |  |||||||| | |||  |    ||   |||\\++++-+-++-++++++-+++-+-+-+--++-++--++--+-+-+-+/||||  | ||||   |  || || 
 |      | |  |/+---++--++++++-+----+++--++--+-+--++++++++-+-+++--+----++---+++-++++-+-++-++++++-+++-+\\| |  || ||  ||  | | | | ||||  | ||||   |  || || 
 |      | \\--+++---++--++++++-+----+++--++--+-+--++++++++-+-+++--+----++---+++-++++-+-++-++++++-+++-/|| |  || ||  ||  | | | | ||||  | ||||   |  || || 
 |      |    |||   ||  \\+++++-+----+++--++--+-+--++++++++-+-+++--+----++---+++-++++-+-/| |||||| |||  || |  || ||  ||  | | | | ||||  | ||||   |  || || 
 \\------+----+++---+/ /-+++++-+----+++--++--+-+--++++++++-+-+++--+----++---+++-++++-+--+-++++++-+++-\\|| |  ||/++--++--+-+\\| | ||||  | ||||   |  || || 
        |    |||   |  | ||||| |    |||  ||  | |  |||||||| | |||  | /--++---+++-++++-+--+-++++++-+++<+++-+--+++++--++\\ | ||| | ||||  | ||||   |  || || 
        |    |||   |  | ||||| |    |||  ||/-+-+--++++++++-+-+++--+-+--++---+++-++++-+--+-++++++-+++-+++-+--+++++--+++-+-+++-+-++++--+-++++---+\\ || || 
        |    |||   |/-+-+++++-+----+++--+++-+-+--++++++++-+-+++--+-+\\ ||   ||| |||| |  | |||||| ||| ||| |  |||||  ||| | ||| | ||||  | ||||   || || || 
        |    |||   || | ||||| |    |||  ||| | |  |||||||| | |||/-+-++-++---+++-++++-+--+-++++++-+++-+++-+--+++++--+++-+-+++-+-++++-\\| ||||   || || || 
        |    |||   || | ||||| |    |||  ||| | |  |||||||| | |||| | || ||   ||| |||| |  | |||||| ||| ||| |  |||||  ||| | ||| | |||| || ||||   || || || 
 /------+----+++---++-+-+++++-+----+++--+++-+-+--++++++++-+-++++-+-++-++\\  ||| |||| |  | |||||| ||| ||| |  |||||  ||| | ||| | |||| || ||||   || || || 
 |      |    |||   || | ||||| |    ||\\--+++-+-+--++++++++-+-++++-+-++-+++--+++-++/| |  \\-++++++-+++-+++-+--+++++--+++-+-+++-+-++++-++-+/||   || || || 
 |      |    \\++---++-+-++++/ |    ||   ||| | |  |||||||| | |||| | || |||  ||| || | |    |||||| ||| ||| |  |||||  ||| | ||| | |||| || \\-++---++-/| || 
 |      |     ||   || | ||||  |/---++---+++-+-+--++++++++-+-++++-+-++-+++--+++-++-+-+----++++++-+++-+++-+--+++++--+++-+-+++-+-++++-++--\\||   ||  | || 
 |      |     ||   || | ||||  ||   ||   ||| | |  ||||||\\+-+-++++-+-++-+++--+++-++-+-+----++++++-+++-+++-+--+++++--+++-+-++/ | |||| ||  |||   ||  | || 
 |      |     ||   || | ||||  ||   ||   ||| | |  |||\\++-+-+-++++-+-++-+++--+++-++-+-+----++++++-+++-+++-+--++++/  ||| | ||  | |||| ||  |||   ||  | || 
 |      |  /--++---++-+-++++--++---++---+++-+-+--+++-++-+-+-++++-+-++-+++--+++-++-+-+---\\|\\++++-+++-+++-/  ||||   ||| | ||  | |||| ||  |||   ||  | || 
 |      |  |  ||   || | ||||  ||   ||   |\\+-+-+--+++-++-+-+-++++-+-++-+++--+++-++-+-+---++-++++-+++-+++----++++---+++-+-++--+-++++-++--+++---++--+-/| 
 |      |  |  ||   || | ||||  ||   ||   | |/+-+--+++-++-+-+-++++-+-++-+++--+++-++-+-+---++-++++-+++-+++----++++---+++-+-++-\\| |||| ||  |||   ||  |  | 
 |      |  |  ||   || | ||||  || /-++->-+-+++-+--+++-++-+\\| |||| | || |||  ||| || | |   || |||| ||| |||    ||||   ||| | || || |||| ||  |||   ||  |  | 
 |      |  |  ||   || | ||||  || | ||   | ||| |  ||| |\\-+++-++++-+-++-+++--+++-++-+-+---+/ |||| ||| |||    ||||   ||| | || || |||| ||  |||   ||  |  | 
 |      |  |  ||   || | |||| /++-+-++---+-+++-+\\ ||| |  ||| ||||/+-++-+++--+++-++-+-+---+--++++-+++-+++----++++---+++>+\\|| || |||| ||  |||   ||  |  | 
 |      |  |  ||   || | |||| ||| | ||   | ||| || ||| |  ||| |||||| || |||  ||| || | |  /+--++++-+++-+++----++++---+++-++++-++-++++-++--+++---++--+--+\\
 |      |  |  ||   || | |||\\-+++-+-++---+-+++-++-+++-+--+++-++++++-++-+++--+++-++-+-+--++--+++/ ||| |||    ||||   ||| |||| || |||| ||  |||   ||  |  ||
 | /----+--+--++---++-+-+++--+++-+-++---+-+++-++-+++-+--+++-++++++-++-+++--+++-++-+-+--++--+++--+++-+++--\\ ||\\+---+++-+++/ || |||| ||  |||   ||  |  ||
 | |    |  |  ||   || | |||  ||| | ||   | ||| || ||| |  ||| |||\\++-++-+++--+++-++-+-+--++--+++--+++-+++--+-++-+---+++-+++--++-++++-/|  |||   ||  |  ||
 | |    |  |  ||   || | |||  ||| | ||   | ||| || ||| |  ||| ||| || || |||  ||| || | |  ||  |||  ||| ||| /+-++-+---+++-+++--++-++++--+\\ |||   ||  |  ||
 | |  /-+--+--++---++-+-+++--+++-+\\||   | ||| || ||| |  ||| ||\\-++-++-+++--+++-++-+-+--++--+++--++/ ||| || || |   ||| |||  || |||| /++-+++---++--+\\ ||
 | |  | |  |  ||   || | |||  ||| ||||   | ||| || ||| |  ||| ||  || || |||  ||| || | |  ||  ||\\--++--++/ || || |   ||| |||  || |||| ||| |||   ||  || ||
 | |  | |  |  ||   || | |||  ||| ||||   | ||| || ||| |  ||| ||  || || |||  ||| || | |  ||  ||   ||  ||  || || |   ||| |||  || |||| ||| |||   ||  || ||
 | |  | |/-+--++---++-+-+++--+++-++++---+-+++-++-+++-+--+++-++\\ || || |||  \\++-++-+-+--++--++---++--++--++-++-+---+++-++/  || |||| ||| |||   ||  || ||
 | |  | || |  ||   || | |||  |\\+-++++---+-+++-++-+++-+--+++-/|| || || |||   || || | |  ||  ||   ||  ||  || || |   ||| ||   || |||| ||| |||   ||  || ||
 | |  | || |  ||   || | |||  | | ||||   | ||| \\+-+++-+--+++--++-++-++-+++---/| || | |  ||  ||   ||  ||  || || |   ||| ||   || |||| ||| |||   ||  || ||
 | |  | || |  ||   || | |||  | | ||||   | |||  | ||| |  |||  || || || |||    v || | |  ||  ||   ||  ||  || || |   ||| ||   || ||\\+-+++-+++---++--/| ||
 | |  | || |  ||   || | |||  | | ||||   | |||  | ||| |  ||\\--++-++-++-+++----+-++-+-+--++--++---++--++--++-++-+---+++-++---++-++-/ ||| |||   ||   | ||
 | |  | || |  ||   \\+-+-+++--+-+-++++---+-+++--+-+++-+--++---++-++-++-+++----+-++-+-+--++--++---/|  ||  || || |   ||| ||   || ||   ||| |||   ||   | ||
 | |  | || |  ||    | | |||  | | ||||   | |\\+--+-+++-+--++---++-++-++-+++----+-++-+-+--++--++----+--++--++-++-+---+++-++---/| ||   ||| |||   ||   | ||
/+-+--+-++-+--++---\\| | |||  | | ||||   | | |  | ||| \\--++---++-++-++-+++----+-++-+-/  ||  ||    |  ||  || || |   ||| ||    | ||   ||| |||   ||   | ||
|| |  | || |  \\+---++-+-+++--+-+-++++---+-+-+--+-+++----++---++-++-++-+++----+-++-+----++--++----+--+/  || || |   ||| ||    | ||   ||| |||   ||   | ||
|| |  | || |   |   || | ||\\--+-+-++++---+-+-+--+-+++----++---++-++-++-+++----+-++-+----++--++----+--+---++-++-+---+++-++----/ ||   ||| |||   ||   | ||
|| |  | || |   |   || | ||   | | ||||   | | |  | |||    ||   || || || |||    | || \\----++--++----+--+---++-++-+---+++-++------++---+++-+++---++---+-/|
|| |  | || |   |   || | ||   | \\-++++---+-+-+--+-+++----++---++-++-++-+++----+-++------++--++----+--+---++-++-+---+++-++------++---+++-/||   ||   |  |
|| |  | || |   |   || | ||   |   ||||   |/+-+--+-+++----++---++-++-++-+++----+-++------++--++----+--+---++-++-+---+++-++-<----++--\\|||  ||   ||   |  |
|| |  | || |   |   || | ||   |   ||||   ||| |  | |||    ||   || || || |||    | ||      \\+--++----+--+---++-++-+---+++-++------++--++++--++---++---+--/
|| |  | || |   |   || | ||   |   ||||  /+++-+--+-+++----++---++-++-++-+++----+-++-------+--++----+--+---++-++-+--<+++-++------++\\ ||||  ||   ||   |   
|| |  | || |   |   || | ||   |   ||||  |||| |  | |||    ||   || || ||/+++----+-++-------+--++----+--+---++-++-+---+++-++----\\ ||| ||||  ||   ||   |   
|| |  | || |   |   || | ||   |   |||| /++++-+--+\\|||    \\+---++-++-++++++----+-++-------+--++----+--+---++-+/ |   ||| ||    | ||| ||||  ||   ||   |   
|| |  | || |   |   || | \\+---+---++++-+++++-+--+++++-----+---++-++-++++++----+-++-------+--++----+--+---++-/  |   ||| ||    | ||| ||||  ||   ||   |   
|| |  \\-++-+---+---++-+--+---+---+/|| ||||| |  |||\\+-----+---++-++-++++++----+-++-------+--++----+--+---++----+---+++-/|    | ||| ||||  ||   ||   |   
|| |    || |  /+---++-+--+---+---+-++-+++++-+--+++-+----<+---++-++-++++++----+-++\\   /--+--++----+--+---++----+---+++--+-\\  | ||| ||||  ||   ||   |   
|| |/---++-+--++---++\\|  \\---+---+-++-+++++-+--+++-+-----+---++-++-++++++----+-+/|   |  |  ||    |  |   \\+----+---+++--+-+--+-+++-+++/  ||   ||   |   
|| ||   || |  ||   ||||      |   | || ||||| |  ||| |     |   || || ||||||    | | |   |  |  ||    |  |    |    |   |||  | |  | ||| |||   ||   ||   |   
|| ||   |\\-+--++---++++------+---+-++-+++++-+--+++-+-----+---+/ || ||||||    | | |   |  |  ||    |  |    |   /+---+++-\\| |  | ||| |||   ||   ||   |   
|| ||   |/-+--++---++++------+---+-++-+++++-+--+++-+-----+---+--++-++++++----+-+-+---+--+--++----+--+-\\  |   ||   ||| || |  |/+++-+++--\\||   ||   |   
|| ||   || |  ||   |||\\------+---+-++-+++++-+--+++-+-----+---+--++-++++++----+-+-+---+--+--++----+--/ |  |   ||   ||| || |  ||||| |||  |||   ||   |   
||/++---++-+--++---+++----\\  |   | || ||||| |  ||| | /---+---+--++-++++++----+-+-+---+--+--++----+----+--+---++---+++-++-+--+++++-+++\\ |||   ||   |   
|||||   || |  ||   |||    |  |   | \\+-+++++-+--+++-+-+---+---+--++-++++++----+-+-+---+--+--++----+----+--+---++---+++-++-+--+++++-++++-++/   ||   |   
|||||   || |  ||   |||    |  |   |  | ||\\++-+--+++-+-+---+---+--++-++++++----+-+-+---+--+--++----+----+--+---+/   ||| || |  ||||| |||| ||    ||   |   
||||| /-++-+--++---+++-\\  |  |   \\--+-++-++-+--+++-+-+---/   |  || |||||| /--+-+-+---+--+--++----+----+--+---+----+++-++-+--+++++-++++-++----++---+--\\
\\++++-+-++-+--++---/|| |  |  |      | || || |  ||| | |       |  || |||\\++-+--+-+-+---+--+--++----+----+--+---+----+++-++-+--+++++-++/| ||    ||   |  |
 |||| | || |  ||    || |  |  |      | || || |  ||| \\-+-------+--++-+++-++-+--+-+-+---+--+--++----+----+--+---+----+/| || |  ||||| || | ||    ||   |  |
 |||| | || |  ||    || |  |  |      | || || |  |||   |       |  || ||| || |  | | |   |  |  ||    |    |  |   \\----+-+-/| |  ||||| || | ||    ||   |  |
 |||| | || |  ||    || |  |  |      | || || |  |||   |       |  || ||| \\+-+--+-+-+---+--+--++----+----+--+--------+-+--+-+--++/|| || | ||    ||   |  |
 ||\\+-+-++-+--++----++-+--+--+------+-++-++-+--+++---+-------+--++-+++--+-+--+-+-+---+--+--++----+----+--/        | |  | |  || || || | ||    ||   |  |
 || \\-+-++-+--++----+/ |  |  |      | || || |  |||   |       |  || |||  | |  | | |   |  |  ||  /-+----+-----------+-+--+-+--++-++\\|| | ||    ||   |  |
 ||   | \\+-+--++----+--+--+--+------+-++-++-+--+++---+-------+--++-+++--+-+--+-/ |   |  |  \\+--+-+----+<----------+-+--+-+--++-+++++-+-++----/|   |  |
 ||   |  | |  |\\----+--+--+--+------+-++-++-/  |||   |       |/-++-+++--+\\|  |   |   |  |   |  | |    |           | |  | |  || ||||| | ||     |   |  |
 ||   |  | |  |     |  |  |  |      | || ||    |||   |       \\+-++-+++--+++--/   |   |  |   |  | |    |           | |  | |  || ||||| | ||     |   |  |
 v|   |  | |  \\-----+--+--+--+------+-++-++----+++---+--------+-++-+++--+++------/   |  |   |  | |  /-+-----------+-+--+-+--++-+++++\\| ||     |   |  |
 |\\---+--+-+--------+--+--/  |      | || ||    |||   |        | || |||  |||          |  |   |  | \\--+-+-----------+-+--+-+--++-+++++++-+/     |   |  |
 |    |  | |        |  |     |      | || ||    |||   |        | || |||  |||          |  |   |  |    | |   /-------+-+--+-+--++-+++++++-+------+-\\ |  |
 |    |  | |        |  |     |      | |\\-++----+++---+--------+-++-+++--+++----------+--+---+--+----+-+---+-------+-+--+-+--++-+/||||| |      | | |  |
 |    \\--+-+--------+--/     |      | \\--++----+/|   |        | || ||\\--+++------<---+--+---+--+----+-+-<-+-------+-+--+-+--/| | ||||| |      | | |  |
 |       | |   /----+-----\\  |      |    \\+----+-+---+--------+-++-++---+++----------+--+---+--+----+-+---+-------+-+--+-+---+-+-+/||| |      | | |  |
 |       | |   |    |     |  |      |     |    | |   |        | || \\+---+++----------+--+---+--+----+-+---+-------+-/  | |   | | | ||| |      | | |  |
 |       | |   |    |     |  |      \\-----+----+-+---+--------+-++--+---+++----------+--+---/  \\----+-+---+-------+----+-+---+-+-/ ||| |      | | |  |
 |       | |   |    |     |  |            |    | |   |        | |\\--+---+++----------+--+-----------+-+---+-------+----+-+---+-/   ||| |      | | |  |
 |       | |   |    |     |  |            |    | \\---+--------+-+---+---+++----------+--+-----------+-+---+-------/    | |   |     ||| |      | | |  |
 |/------+-+---+----+-----+--+------------+----+-----+--------+-+---+---+++----------+--+------\\    \\-+---+------------+-+---+-----+/| |      | | |  |
 ||      | |   |    \\-----+--+------------+----+-----+--------+-+---/   |||          | /+------+------+---+------------+-+---+-----+-+-+------+-+\\|  |
 ||      | |   |    /-----+--+------------+----+-----+--------+-+-------+++----------+-++------+------+---+------\\     | |   \\-----+-+-/      | |||  |
 ||      | |   |    |     |  |            \\----+-----+--------+-+-------+++----------+-++------+------+---+------+-----+-+---------+-+--------/ |||  |
 ||      | |   |    |     |  |                 |     |        | |       |||          \\-++------+------+-->+------+-----+-/         | |          |||  |
 \\+------+-+---+----+-----+--+-----------------+-----+--------+-+-------/||            ||      |      |   |      |     |           | |          |||  |
  |      \\-+---+----+-----+--+-----------------+-----+--------+-+--------++------------++------+------/   |      |     |           | |          |||  |
  |        |   |    |     |  |                 |     |        | |        ||            ||      |          |      |     |           | |          |||  |
  |        |   \\----+-----/  \\-----------------/     |        | |        ||            ||      |          |      |     |           | |          |||  |
  |        |        |                                |        | |        ||            ||      |          |      |     |           | |          |||  |
  |        |        |                                \\--------+-+--------++------------++------+----------+------+-----+-----------+-/          |||  |
  |        |        |                                         | |        |\\------------++------+----------+------+-----+-----------+------------+++--/
  |        |        |                                         | |        |             ||      |          |      |     |           \\------------++/   
  |        |        |                                         | |        |             ||      |          |      |     |                        ||    
  |        \\--------+-----------------------------------------+-+--------+-------------+/      |          \\------+-----+------------------------/|    
  |                 |                                         | \\--------+-------------+-------+-----------------+-----/                         |    
  \\-----------------+-----------------------------------------+----------+-------------+-------/                 |                               |    
                    \\-----------------------------------------+----------+-------------+-------------------------/                               |    
                                                              \\----------/             \\---------------------------------------------------------/    """


from collections import namedtuple
from enum import Enum

class Cart():
    def __init__(self, posX, posY, direction, turns):
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.turns = turns
    
    def move(self, m):
        if self.direction == Direction.UP:
            self.posY -= 1
            newPosition = m[self.posY][self.posX]
            if  newPosition == '/':
                self.direction = Direction.RIGHT
            elif newPosition == '\\':
                self.direction = Direction.LEFT
            elif newPosition == '+':
                if self.turns == 0:
                    self.direction = Direction.LEFT
                elif self.turns == 2:
                    self.direction = Direction.RIGHT
                self.turns = (self.turns + 1) % 3
        elif self.direction == Direction.DOWN:
            self.posY += 1
            newPosition = m[self.posY][self.posX]
            if  newPosition == '/':
                self.direction = Direction.LEFT
            elif newPosition == '\\':
                self.direction = Direction.RIGHT
            elif newPosition == '+':
                if self.turns == 0:
                    self.direction = Direction.RIGHT
                elif self.turns == 2:
                    self.direction = Direction.LEFT
                self.turns = (self.turns + 1) % 3
        elif self.direction == Direction.LEFT:
            self.posX -= 1
            newPosition = m[self.posY][self.posX]
            if  newPosition == '/':
                self.direction = Direction.DOWN
            elif newPosition == '\\':
                self.direction = Direction.UP
            elif newPosition == '+':
                if self.turns == 0:
                    self.direction = Direction.DOWN
                elif self.turns == 2:
                    self.direction = Direction.UP
                self.turns = (self.turns + 1) % 3
        elif self.direction == Direction.RIGHT:
            self.posX += 1
            newPosition = m[self.posY][self.posX]
            if  newPosition == '/':
                self.direction = Direction.UP
            elif newPosition == '\\':
                self.direction = Direction.DOWN
            elif newPosition == '+':
                if self.turns == 0:
                    self.direction = Direction.UP
                elif self.turns == 2:
                    self.direction = Direction.DOWN
                self.turns = (self.turns + 1) % 3

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

def prepareInput():
    splitInput = input.split('\n')

    m = []
    for line in splitInput:
        m.append([x for x in line])

    return m

def samePositions(carts):
    samePosition = []
    for cart in carts:
        indexCart = carts.index(cart)
        test = [carts.index(x) for x in carts if (x.posX == cart.posX and x.posY == cart.posY and carts.index(x) != indexCart)]
        if test != []:
            samePosition.append(test)
    return samePosition

def cartsort(cart):
    return cart.posY + float(cart.posX) / 1000

def do():
    m = prepareInput()

    carts = []

    for line in m:
        found = True
        while(found):
            if '<' in line:
                index = line.index('<')
                indexList = m.index(line)

                carts.append(Cart(index, indexList, Direction.LEFT, 0))

                line[index] = '-'

            elif '>' in line:
                index = line.index('>')
                indexList = m.index(line)

                carts.append(Cart(index, indexList, Direction.RIGHT, 0))

                line[index] = '-'

            elif 'v' in line:
                index = line.index('v')
                indexList = m.index(line)

                carts.append(Cart(index, indexList, Direction.DOWN, 0))

                line[index] = '|'

            elif '^' in line:
                index = line.index('^')
                indexList = m.index(line)

                carts.append(Cart(index, indexList, Direction.UP, 0))

                line[index] = '|'             
            else:
                found = False

    while(True):
        carts.sort(key=cartsort)
        for cart in carts.copy():
            cart.move(m)
            samePositionCart = samePositions(carts)
            if samePositionCart != []:
                cart1 = carts[samePositionCart[0][0]]
                cart2 = carts[samePositionCart[1][0]]
                carts.remove(cart1)
                carts.remove(cart2)
        if len(carts) == 1:
                return [carts[0].posX, carts[0].posY]
  
print(do())



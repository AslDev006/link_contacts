from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")
PHONE_NUMBER = env.str('phone_number')
FIRST_NAME = env.str('first_name')
LAST_NAME = env.str('last_name')
COURSE_1 = env.str('course_1')
PHONE = env.str('phone')

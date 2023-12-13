import datetime
import random
import  sqlite3
from .query_db import *


lorem_ipsum = (
    'ab', 'accusamus', 'accusantium', 'ad', 'adipisci', 'alias', 'aliquam', 'aliquid', 'amet', 'animi', 'aperiam',
    'architecto', 'asperiores', 'aspernatur', 'assumenda', 'at', 'atque', 'aut', 'autem', 'beatae', 'blanditiis',
    'commodi', 'consectetur', 'consequatur', 'consequuntur', 'corporis', 'corrupti', 'culpa', 'cumque', 'cupiditate',
    'debitis', 'delectus', 'deleniti', 'deserunt', 'dicta', 'dignissimos', 'distinctio', 'dolor', 'dolore', 'dolorem',
    'doloremque', 'dolores', 'doloribus', 'dolorum', 'ducimus', 'ea', 'eaque', 'earum', 'eius', 'eligendi', 'enim',
    'eos', 'error', 'esse', 'est', 'et', 'eum', 'eveniet', 'ex', 'excepturi', 'exercitationem', 'expedita', 'explicabo',
    'facere', 'facilis', 'fuga', 'fugiat', 'fugit', 'harum', 'hic', 'id', 'illo', 'illum', 'impedit', 'in', 'incidunt',
    'inventore', 'ipsa', 'ipsam', 'ipsum', 'iste', 'itaque', 'iure', 'iusto', 'labore', 'laboriosam', 'laborum',
    'laudantium', 'libero', 'magnam', 'magni', 'maiores', 'maxime', 'minima', 'minus', 'modi', 'molestiae', 'molestias',
    'mollitia', 'nam', 'natus', 'necessitatibus', 'nemo', 'neque', 'nesciunt', 'nihil', 'nisi', 'nobis', 'non',
    'nostrum', 'nulla', 'numquam', 'occaecati', 'odio', 'odit', 'officia', 'officiis', 'omnis', 'optio', 'pariatur',
    'perferendis', 'perspiciatis', 'placeat', 'porro', 'possimus', 'praesentium', 'provident', 'quae', 'quaerat',
    'quam', 'quas', 'quasi', 'qui', 'quia', 'quibusdam', 'quidem', 'quis', 'quisquam', 'quo', 'quod', 'quos', 'ratione',
    'recusandae', 'reiciendis', 'rem', 'repellat', 'repellendus', 'reprehenderit', 'repudiandae', 'rerum', 'saepe',
    'sapiente', 'sed', 'sequi', 'similique', 'sint', 'sit', 'soluta', 'sunt', 'suscipit', 'tempora', 'tempore',
    'temporibus', 'tenetur', 'totam', 'ullam', 'unde', 'ut', 'vel', 'velit', 'veniam', 'veritatis', 'vero', 'vitae',
    'voluptas', 'voluptate', 'voluptatem', 'voluptates', 'voluptatibus', 'voluptatum',
)

lorem_terms = [w for w in lorem_ipsum if len(w) > 7]


def generate_title(word_count=3):
    while True:
        sentence = ' '.join(random.choices(lorem_ipsum, k=word_count))
        yield sentence.title()


def generate_term():
    while True:
        yield random.choice(lorem_terms).capitalize()


def generate_caption(word_count=8):
    while True:
        sentence = ' '.join(random.choices(lorem_ipsum, k=word_count))
        yield f'{sentence.capitalize()}.'


def generate_amount(min=1000, max=10000):
    while True:
        yield f'{random.randint(min, max):,}'


def generate_dollars(min=1000, max=9000):
    d = max - min
    while True:
        yield f'${min + d * random.random():,.2f}'


def generate_percent(min=-10, max=10):
    d = max - min
    while True:
        yield f'{min + d * random.random():.2f}%'


def generate_random_choice(choices):
    while True:
        yield random.choice(choices)


def generate_sequence(choices):
    k = len(choices) - 1
    i = 0
    while True:
        yield choices[i]
        i = 0 if i == k else i + 1


def generate_time_series(days: int):
    d = datetime.datetime.utcnow() - datetime.timedelta(days=days - 1)
    day = datetime.timedelta(days=1)
    while True:
        d += day
        yield f'{d.isoformat()}Z'


def generate_random_walk(min=0, max=100, variation=0.1):
    dx = (max - min) * variation
    x = random.randint(min, max)
    while True:
        x += int((random.random() - 0.5) * dx)
        if not min <= x <= max:
            x = random.randint(min, max)
        yield x
#------------------
## Chủng loại xi măng sản xuất của nhà máy
type_cement = ['ASTM C150- Bao 50kg', 'ASTM C150- Roi', 'Power- Bao 50kg', 'Green PC40 - Bao 50kg', 'Green PC40 - Roi', 'PCB40- Bao Jumbo', 'ASTM C150 Type I- Bao Jumbo','PCB50 - Bao 50kg' ,'PCB50 - Roi']
def generate_type_cement(type_cement):
    # while True:
    #     yield random.choice(type_cement)
    while True:
        for cement_type in type_cement:
            yield cement_type
## Dữ liệu sửa chữa của nhà máy
### (label='Sửa chữa cơ', value='35%', fraction=0.90, color='#2cd0f5', aux_value='100 giờ')
repair_info = [
    ['Cối đập',"250 giờ", "120 giờ", "67.57%", "32.43%", 0.68, 0.32, "#b74341", "#48bcbe"],
    ['Nghiền Bột Sống',"90 giờ", "80 giờ", "52.94%", "47.06%", 0.53, 0.47, "#782969", "#87d696"],
    ['Lò Nung',"140 giờ", "167 giờ", "45.60%", "54.40%", 0.46, 0.54, "#06849b", "#f97b64"],
    ['Nghiền Xi Măng',"34 giờ", "59 giờ", "36.56%", "63.44%", 0.37, 0.63, "#a25b30", "#5da4cf"],
    ['Máy Đóng Bao',"80 giờ", "100 giờ", "44.44%", "55.56%", 0.44, 0.56, "#e914de", "#16eb21"],
    ['Xuất Xi Măng Rời',"300 giờ", "150 giờ", "66.67%", "33.33%", 0.67, 0.33, "#8c39ad", "#3caef7"],
]
## Dữ liệu môi trường
env_nghien_than = [51,66,  49,  15,  67,  39,  13,  45,  32,  16]
env_lo_nung = [59,  52,  53,  19,  56,  62,  54,  31,  30,  24]
env_lam_nguoi = [12,  23,  33,  65,  57,  29,  34,  22,  43,  55]
env_xi_mang = [14,  41,  38,  25,  42,  48,  68,  60,  69,  63]
env_month = ["T1",	"T2",	"T3",	"T4",	"T5",	"T6",	"T7",	"T8",	"T9",	"T10"]
def env_value(area=None):
    if area == 'nghien_than':
        data_env = env_nghien_than
    elif area == 'lo_nung':
        data_env = env_lo_nung
    elif area == 'lam_nguoi':
        data_env = env_lam_nguoi
    elif area == 'xi_mang':
        data_env = env_xi_mang
    elif area == 'month':
        data_env = env_month
    while True:
        for data in data_env:
            yield data

## Dữ liệu lò nung
# #------------------
# distinct_data = get_distinct_data(table='kiln', name_col='tag')
# tag_list_kiln = []
# for tag in distinct_data:
#     tag_list_kiln.append(tag[0])
# def tag_name_kiln():
#     while True:
#         yield random.choice(tag_list_kiln)


#------------------
sample_title = generate_title()
sample_term = generate_term()
sample_caption = generate_caption()
sample_amount = generate_amount()
sample_dollars = generate_dollars()
sample_percent = generate_percent()
sample_icon = generate_sequence(['ExerciseTracker', 'Glasses', 'Cafe', 'Bullseye', 'Guitar', 'Game', 'Headset'])
sample_color = generate_sequence(['$blue', '$red'])

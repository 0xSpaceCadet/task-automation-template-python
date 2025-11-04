import random
from idlelib.run import capture_warnings
from pathlib import Path as m_path

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
    'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
                'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
                'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for k, v in capitals.items():
    print(k, '--', v)

for q_num in range(5):
    q_file_path=f'q_file_{q_num+1}.txt'
    q_file = open(file=q_file_path, mode='w', encoding='UTF-8')

    a_file_path = f'a_file_{q_num+1}.txt'
    a_file = open(file=a_file_path, mode='w', encoding='UTF-8')

    q_file.write('UUID:\n\nPassphrase:')

    state = list(capitals.keys())
    random.shuffle(state)

    for num in range(50):
        c_ans = capitals[state[num]]
        w_ans = list(capitals.values())
        del w_ans[w_ans.index(c_ans)] # actual c_ans
        w_ans = random.sample(w_ans, 3)
        a_options = w_ans+[c_ans]
        random.shuffle(a_options)

    q_file.close()
    a_file.close()












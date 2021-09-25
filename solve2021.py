import requests, json, heapq
from collections import deque

def get_auth_key(problem_num):
    
    headers = {
        'X-Auth-Token' : 'ae0b74befcf2c8937261c92b32587630',
        'Content-Type' : 'application/json'
    }

    params = {
        'problem' : problem_num
    }

    r = requests.post(base_url + '/start', headers=headers, data=json.dumps(params))

    return json.loads(r.text)['auth_key']

def get_locations():

    headers = {
        'Authorization' : auth_key,
        'Content-Type' : 'application/json'
    }

    r = requests.get(base_url + '/locations', headers=headers)

    locations = json.loads(r.text)['locations']

    board = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(25):
        r, c = get_rc(i)
        board[r][c] = locations[i]['located_bikes_count']

    return board

def get_trucks():

    headers = {
        'Authorization' : auth_key,
        'Content-Type' : 'application/json'
    }

    r = requests.get(base_url + '/trucks', headers=headers)

    trucks = json.loads(r.text)['trucks']

    truck_pos = []
    
    for idx, truck in enumerate(trucks):
        pos = get_rc(truck['location_id'])
        pos.append(truck['loaded_bikes_count'])
        truck_pos.append(pos)
    
    return truck_pos
 
def search():
    result = []
    
    for mod in range(4):
        command = {}
        search_range = [(0,3,0,3), (0,3,2,5), (2,5,0,3), (2,5,2,5)]
        r1, r2, c1, c2 = search_range[mod]
        ori = False
        move = False
        on_truck = False
        for r in range(r1,r2):
            for c in range(c1,c2):
                if locations[r][c] < 2:
                    move = True
                    needs = 2 - locations[r][c]
                    target = [r,c]
                if move:
                    break
            if move:
                break
        
        if move:
            if needs > trucks[mod][2]:
                for r in range(r1,r2):
                    for c in range(c1, c2):
                        if locations[r][c] >= 2 + needs:
                            origin = [r,c]
                            ori = True
                        if ori:
                            break
                    if ori:
                        break

            else:
                on_truck = True


        cr, cc = trucks[mod][0], trucks[mod][1]
        
        if ori:

            command['truck_id'] = mod
            command['command'] = []
            
            # 트럭 현재 위치
            

            # 자전거를 실을 정류소까지 이동하는 명령
            ori_r, ori_c = origin[0], origin[1]

            rep = abs(cr - ori_r)
            if cr > ori_r:
                for _ in range(rep):
                    command['command'].append(1)
            
            else:
                for _ in range(rep):
                    command['command'].append(3)
            
            rep = abs(cc - ori_c)
            if cc > ori_c:
                for _ in range(rep):
                    command['command'].append(4)
            
            else:
                for _ in range(rep):
                    command['command'].append(2)

            
            for _ in range(needs):
                command['command'].append(5)
            
            # 자전거를 갖다줄 정류소까지 이동하는 명령
            tr, tc = target

            rep = abs(ori_r - tr)
            if ori_r > tr:
                for _ in range(rep):
                    command['command'].append(1)
            else:
                for _ in range(rep):
                    command['command'].append(3)

            rep = abs(ori_c - tc)
            if ori_c > tc:
                for _ in range(rep):
                    command['command'].append(4)
            
            else:
                for _ in range(rep):
                    command['command'].append(2)

            # 자전거 하역
            for _ in range(needs):
                command['command'].append(6)
            
            command['command'] = command['command'][:10]
            result.append(command)

        if on_truck:

            command['truck_id'] = mod
            command['command'] = []

            tr, tc = target

            rep = abs(cr - tr)
            if cr > tr:
                for _ in range(rep):
                    command['command'].append(1)
            else:
                for _ in range(rep):
                    command['command'].append(3)

            rep = abs(cc - tc)
            if cc > tc:
                for _ in range(rep):
                    command['command'].append(4)
            
            else:
                for _ in range(rep):
                    command['command'].append(2)

            # 자전거 하역
            for _ in range(needs):
                command['command'].append(6)

            command['command'] = command['command'][:10]
            result.append(command)

    return result if result else None




def simulate():
    headers = {
        'Authorization' : auth_key,
        'Content-Type' : 'application/json'
    }


    params = {
        'commands' : [
        ]
    }

    
    result = search() 
    if result:
        # print("result: ", result)
        params['commands'].extend(result)

    r = requests.put(base_url + '/simulate', headers=headers, data=json.dumps(params))

    return json.loads(r.text)

def get_score():

    headers = {
        'Authorization' : auth_key,
        'Content-Type' : 'application/json'
    }

    r = requests.get(base_url + '/score', headers=headers)

    return json.loads(r.text)['score']


def get_rc(idx):

    r, c = N - idx % N - 1, idx // N
    return [r, c]


N = 5

base_url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'

auth_key = get_auth_key(1)

for _ in range(720):
    locations = get_locations()
    trucks = get_trucks()
    result = simulate()
score = get_score()

# locations[0][0] = 1
# locations[0][4] = 1
# trucks[0][2] = 1

# print(auth_key)
# print(locations)
# print(trucks)
print(result)
print(score)

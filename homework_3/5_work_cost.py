def team_costs(func):
    def wrapper(team_size, overtime_hours):
        price_dict = {'BA': 700, 'QA': 900, 'AQA': 1500, 'DevOps': 1400, 'Dev': 2000, 'PM': 1300,
                      'TL': 2000}  # cost for month
        team_cost = 0
        worker_count_dict = func(team_size, overtime_hours)
        team = ''
        for position in worker_count_dict.keys():
            workers_cost = get_cost(price_dict[position], worker_count_dict[position], overtime_hours)
            team_cost += workers_cost
            team += ' ' + str(worker_count_dict[position]) + '-' + position
        return 'Team with' + team + ' costs ' + str(team_cost) + ' parrots.'

    return wrapper


@team_costs
def get_team_cost(team_size, overtime_hours=0):
    worker_count_dict = {}
    count = 0
    while count < team_size:
        entered_data = input('Enter position and workers quantity on this position: ').split()
        position = entered_data[0]
        workers_count = int(entered_data[1])
        count += workers_count
        worker_count_dict.update({position: workers_count})

    return worker_count_dict


def get_cost(position, workers, overtime_hours):
    average_count_work_days_in_month = 22
    overtime_coefficient = 2
    work_day_hours = 8
    position_cost_in_day = position // average_count_work_days_in_month
    position_cost_one_hour = position_cost_in_day // work_day_hours
    return position * workers + position_cost_one_hour * overtime_coefficient * overtime_hours


if __name__ == '__main__':
    team_size = int(input('Enter team size: '))
    overtime_hours = int(input('Enter overtime for every team worker for this month (in hours): '))
    print(get_team_cost(team_size, overtime_hours))

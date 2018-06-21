# set_covering_radios_and_states.py

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

def best_set_of_stations(states_needed, stations):
    final_stations = set()
    states_covered = set()
    
    while states_needed:
        best_station = None
        covered = set()
        
        for station_name, station_states in stations.items():
            if len(states_needed & station_states) > len(covered):
                covered = states_needed & station_states
                best_station = station_name
            
        final_stations.add(best_station)
        states_needed = states_needed - covered

    print(final_stations)

best_set_of_stations(states_needed, stations)
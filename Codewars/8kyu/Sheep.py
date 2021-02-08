def warn_the_sheep(queue: list):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'

    queue.reverse()
    wolf_index = queue.index('wolf')
    return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolf_index)